import django_filters
from django.forms import CheckboxSelectMultiple, DateTimeInput

from core.models.category import Category

from core.models.post import Post


class PostFilter(django_filters.FilterSet):
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), label='Категории', widget=CheckboxSelectMultiple,)
    time_of_creating = django_filters.DateTimeFilter(lookup_expr='gte', widget=DateTimeInput(attrs={'type': 'datetime-local'}), label='От')
    title = django_filters.CharFilter(lookup_expr='icontains', label='Содержит в названии')
    
    class Meta:
        model = Post
        fields = ('title', 'author', 'time_of_creating', 'category', )
    