import django_filters
from .models import Leason,Product


class ProductFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model= Product
        fields=('name','author')