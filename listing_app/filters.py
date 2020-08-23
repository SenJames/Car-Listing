import django_filters
from django import forms
from django_filters import CharFilter, RangeFilter
from .models import Car

class CarFilter(django_filters.FilterSet):
    # car_name = CharFilter(field_name='car_name', label='Product', lookup_expr='icontains',)
    # # car_name = ModelChoiceFilter(queryset=Car.objects.all(), lookup_expr='icontains',)
    # # # CharFilter(field_name='car_name', label='Product', lookup_expr='icontains',)
    # car_price = RangeFilter(field_name='car_price')
    # # car_status = CharFilter(field_name='car status', )
    # car_status = django_filters.ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple)
        # car_price__gt = django_filters.NumberFilter(field_name='car_price', label='Price From', lookup_expr='car_price__gt')
    # car_price__lt = django_filters.NumberFilter(field_name='car_price', label='Price To', lookup_expr='car_price__lt')
        # car_status = django_filters.BooleanFilter(field_name='car_status', lookup_expr='in')

    # car_status = django_filters.ModelChoiceFilter(widget=forms.SelectMultiple, label='Car Status', queryset=Car.objects.all())

    class Meta:
        model = Car
        fields = ['car_make','car_year', 'car_transmission']

class CarIndexFilter(django_filters.FilterSet):
    car_name = CharFilter(field_name='car_name', label='Product', lookup_expr='icontains')
    car_price__gt = django_filters.NumberFilter(field_name='car_price', label='Price From', lookup_expr='gte')
    car_price__lt = django_filters.NumberFilter(field_name='car_price', label='Price To', lookup_expr='lte')
    car_year__gt = django_filters.NumberFilter(field_name='car_year', label='From Year:', lookup_expr='gte')
    car_year__lt = django_filters.NumberFilter(field_name='car_year', label='To Year:', lookup_expr='lte')
    
    class Meta:
        model = Car
        fields = ['car_make']

