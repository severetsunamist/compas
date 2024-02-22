from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = '__all__'
        exclude = {
            'publication_date', # CHECK exclude
        }
        labels = {
            'name': '',
            'lat': '',
            'lng': '',
            'address': '',
            'publication_date': '',

            'contact_name': '',
            'contact_phone': '',
            'contact_tg': '',

            'tapu': '',
            'iskan': '',
            'project_status': '',
            'comment': '',

            'sale_offered': '',
            'sale_price': '',

            'rent_offered': '',
            'rental_price': '',
            'deposit': '',
            'condo_fee': '',

            'gross_area': '',
            'net_area': '',
            'floor': '',
            'total_floors': '',
            'heating': '',

            'bedrooms': '',
            'bathrooms':'',
            'wc': '',
            'balcony': '',

            'furnitured':'',
            'internet': '',
            'conditioner':'',
            'fridge': '',
            'cooker':'',
            'washer':'',
            'dish_washer':'',
            'sea_view': '',

            'private_territory': '',
            'security': '',
            'parking': '',
            'pool': '',
            'playground': '',
            'reserve_generator': '',
            'gym': '',
            'spa': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Шикарная 3+1 в Соли'}),
            'lat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: 36.7727692'}),
            'lng': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: 34.5670689'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Например: Merkez, Eğriçam Mah, 2201. Sk. NO:14, 33333 Yenişehir/Mersin'}),
            'property_type': forms.Select(attrs={'class': 'form-select'}),

            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_tg': forms.TextInput(attrs={'class': 'form-control'}),

            'tapu': forms.CheckboxInput(
                attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_tapu', 'autocomplete': 'off',
                       'checked': False}),
            'iskan': forms.CheckboxInput(
                attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_iskan', 'autocomplete': 'off',
                       'checked': False}),
            'project_status': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Например: Очень светлая, дышется свободно, хочется жить'}),

            'sale_offered': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_sale_offered','autocomplete': 'off', 'checked': True}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),

            'rent_offered': forms.CheckboxInput(
                attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_rent_offered',
                       'autocomplete': 'off', 'checked': False}),
            'rental_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'condo_fee': forms.NumberInput(attrs={'class': 'form-control'}),

            'gross_area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '150'}),
            'net_area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '125'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control col-1', 'placeholder': '1'}),
            'total_floors': forms.NumberInput(attrs={'class': 'form-control col-1', 'placeholder': '10'}),
            'heating': forms.Select(attrs={'class': 'form-select'}),

            'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
            'wc': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
            'balcony': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2'}),

            'furnitured': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_furnitured', 'autocomplete': 'off', 'checked': False}),
            'internet': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_internet','autocomplete': 'off', 'checked': False}),
            'conditioner': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_conditioner', 'autocomplete': 'off', 'checked': False}),
            'fridge': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_fridge', 'autocomplete': 'off', 'checked': False}),
            'cooker': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_cooker', 'autocomplete': 'off', 'checked': False}),
            'washer': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_washer', 'autocomplete': 'off', 'checked': False}),
            'dish_washer': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_dish_washer', 'autocomplete': 'off', 'checked': False}),
            'sea_view': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_sea_view','autocomplete': 'off', 'checked': False}),

            'private_territory': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_private_territory','autocomplete': 'off', 'checked': False}),
            'security': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_security','autocomplete': 'off', 'checked': False}),
            'parking': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_parking','autocomplete': 'off', 'checked': False}),
            'pool': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_pool', 'autocomplete': 'off', 'checked': False}),
            'playground': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_playground','autocomplete': 'off', 'checked': False}),
            'reserve_generator': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_reserve_generator','autocomplete': 'off', 'checked': False}),
            'gym': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_gym','autocomplete': 'off', 'checked': False}),
            'spa': forms.CheckboxInput(attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': 'check_spa','autocomplete': 'off', 'checked': False}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['img']
        label = {
            'img': '',
        }
        widgets = {
            'flat_id': forms.Select(attrs={}), # 'style': 'display: none;'
            'img': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Подтверждение пароля'})


