from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateFilter(field_name='time_in', lookup_expr='gt',
                                 widget=DateInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {'title': ['icontains'], 'categoryType': ['exact'],}
