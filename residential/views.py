from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FlatForm, PhotoForm, CustomUserCreationForm
from .models import Flat, Photo
from datetime import date
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import FlatFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def createflat_view(request):
    form = FlatForm()
    new_imgs = PhotoForm()
    if request.method == 'POST':
        form = FlatForm(request.POST)
        new_imgs = PhotoForm(request.POST, request.FILES)
        if form.is_valid() and new_imgs.is_valid():
            flat = form.save()
            all_images = request.FILES.getlist('img')
            for image in all_images:
                if image:
                    pic = Photo.objects.create(flat_id=flat, img=image)
                    pic.save()
            return redirect('flat', flat.pk)
    context = {
        'form': form,
        'new_imgs': new_imgs,
    }
    return render(request, 'new_flat.html', context)


def updateflat_view(request, pk):

    preloaded_data = Flat.objects.get(id=pk)
    current_imgs = Photo.objects.filter(flat_id=pk)
    form = FlatForm(instance=preloaded_data)
    new_imgs = PhotoForm()

    if request.method == 'POST':
        form = FlatForm(request.POST, instance=preloaded_data)

        if form.is_valid():
            form.save()
            all_images = request.FILES.getlist('img')
            for image in all_images:
                if image:
                    pic = Photo.objects.create(flat_id=preloaded_data, img=image)
                    pic.save()
            return redirect('flat', pk)
    else:
        print('NOT POST _______________________________________________')

    context = {
        'preloaded_data': preloaded_data,
        'form': form,
        'new_imgs': new_imgs,
        'current_imgs': current_imgs,
        'pk': pk,
    }
    return render(request, 'update_flat.html', context)


def deleteflat_view(request, pk):
    delete_data = Flat.objects.get(id=pk)
    if request.method == 'POST':
        delete_data.delete()
        return redirect('listing')

    context = {
        'delete_data': delete_data,
        'pk': pk
    }
    return render(request, 'detele_flat.html', context)


def deletephoto_view(request, pk):
    delete_data = Photo.objects.get(id=pk)
    flat_id = delete_data.flat_id.id
    to_url = f'/updateflat/{flat_id}/'
    if request.method == 'POST':
        delete_data.delete()
        return redirect(to_url)

    context = {
        'delete_data': delete_data,
        'pk': pk
    }
    return render(request, 'detele_photo.html', context)


def listing_view(request):
    my_filter, paginated_objects, property_type = _search_results(request)
    context = {
        'my_filter': my_filter,
        "paginated_objects": paginated_objects,
        "property_type": property_type,
        "is_search_view": False
    }
    return render(request, 'listing.html', context)


def search_view(request):
    my_filter, paginated_objects, property_type = _search_results(request)
    context = {
        'my_filter': my_filter,
        "paginated_objects": paginated_objects,
        "property_type": property_type,
        "is_search_view": True # do I actually need it?
    }
    return render(request, 'search_results.html', context)


def _search_results(request):
    page = request.GET.get("page")

    property_type = request.GET.get("property_type")
    sale_offered = request.GET.get("sale_offered")
    rent_offered = request.GET.get("rent_offered")


    my_filter = FlatFilter(request.GET, queryset=Flat.objects.all())
    paginator = Paginator(my_filter.qs, 4)

    try:
        paginated_objects = paginator.get_page(page)
    except PageNotAnInteger:
        paginated_objects = paginator.page(1)
    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)

    return my_filter, paginated_objects, property_type

def flat_view(request, pk):
    flat = Flat.objects.get(id=pk)
    flat.save()
    images = Photo.objects.filter(flat_id=pk)

    context = {
        'flat': flat,
        'images': images,
    }
    return render(request, 'flat.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Добро пожаловать, вы успешно зарегестрировались!')
            # return redirect('login')
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('listing')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listing')
        else:
            messages.error(request, ('Неверный пароль или логин, попробуйте снова...'))
            return redirect('login')

    else:
        return render(request, 'login.html', {})