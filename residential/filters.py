import django_filters
from .models import *
from django import forms
OFFERED_CHOICES = [
    (True, 'Да'),
    (False, 'Нет'),
]

class FlatFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact', widget=forms.TextInput(
    attrs={
      "class": "form-control",
      "placeholder": "Поиск по ID",
    }))

    sale_offered = django_filters.ChoiceFilter(field_name='sale_offered', choices=OFFERED_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))
    rent_offered = django_filters.ChoiceFilter(field_name='rent_offered', choices=OFFERED_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))

    sale_price__gte = django_filters.NumberFilter(field_name='sale_price', lookup_expr='gte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    sale_price__lte = django_filters.NumberFilter(field_name='sale_price', lookup_expr='lte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    rental_price__gte = django_filters.NumberFilter(field_name='rental_price', lookup_expr='gte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    rental_price__lte = django_filters.NumberFilter(field_name='rental_price', lookup_expr='lte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))


    gross_area__gte = django_filters.NumberFilter(field_name='gross_area', lookup_expr='gte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    gross_area__lte = django_filters.NumberFilter(field_name='gross_area', lookup_expr='lte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    property_type = django_filters.ChoiceFilter(field_name='property_type', choices=dropdowns.property_types, widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))

    floor__gte = django_filters.NumberFilter(field_name='floor', lookup_expr='gte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    floor__lte = django_filters.NumberFilter(field_name='floor', lookup_expr='lte', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))


    heating = django_filters.ChoiceFilter(field_name='heating', choices=dropdowns.heating_types, widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))
    project_status = django_filters.ChoiceFilter(field_name='project_status', choices=dropdowns.project_status, widget=forms.Select(
        attrs={
            'class': 'form-select',
        }
    ))
    # furnitured = django_filters.BooleanFilter(field_name='furnitured')
    # internet = django_filters.BooleanFilter(field_name='internet')
    # conditioner = django_filters.BooleanFilter(field_name='conditioner')
    # fridge = django_filters.BooleanFilter(field_name='fridge')
    # cooker = django_filters.BooleanFilter(field_name='cooker')
    # washer = django_filters.BooleanFilter(field_name='washer')
    # dish_washer = django_filters.BooleanFilter(field_name='dish_washer')
    # sea_view = django_filters.BooleanFilter(field_name='sea_view')
    # private_territory = django_filters.BooleanFilter(field_name='private_territory')
    # security = django_filters.BooleanFilter(field_name='security')
    # parking = django_filters.BooleanFilter(field_name='parking')
    # pool = django_filters.BooleanFilter(field_name='pool')
    # playground = django_filters.BooleanFilter(field_name='playground')
    # reserve_generator = django_filters.BooleanFilter(field_name='reserve_generator')
    # gym = django_filters.BooleanFilter(field_name='gym')
    # spa = django_filters.BooleanFilter(field_name='spa')


    class Meta:
        model = Flat
        fields = [
            'id',
            'sale_offered',
            'rent_offered',
            'sale_price',
            'rental_price',
            'property_type',
            'gross_area',
            'floor',
            'heating',
            'project_status',
            # 'furnitured',
            # 'internet',
            # 'conditioner',
            # 'fridge',
            # 'cooker',
            # 'washer',
            # 'dish_washer',
            # 'sea_view',
            # 'private_territory',
            # 'security',
            # 'parking',
            # 'pool',
            # 'playground',
            # 'reserve_generator',
            # 'gym',
            # 'spa',
        ]
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Шикарная 3+1 в Соли'}),
            'property_type': forms.Select(attrs={'class': 'form-select'}),
            'sale_offered': forms.CheckboxInput(
                attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': '',
                       'autocomplete': 'off', 'checked': True}),
            'rent_offered': forms.CheckboxInput(
                attrs={'style': 'display:none;', 'class': 'btn btn-check', 'id': '',
                       'autocomplete': 'off', 'checked': True}),
            'gross_area': forms.NumberInput(attrs={'class': 'form-control'}),

            'rental_price__gte': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price__lte': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price__gte': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price__lte': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor__gte': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor__lte': forms.NumberInput(attrs={'class': 'form-control'}),
            'project_status': forms.Select(attrs={'class': 'form-select'}),
            'heating': forms.Select(attrs={'class': 'form-select'}),

        }
