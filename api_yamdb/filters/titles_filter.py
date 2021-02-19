import django_filters

from api_yamdb.models import Titles


class TitlesFilter(django_filters.FilterSet):
    genre__slug = django_filters.CharFilter(lookup_expr='iexact')
    category__slug = django_filters.CharFilter()
    year = django_filters.NumberFilter()
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Titles
        fields = '__all__'
