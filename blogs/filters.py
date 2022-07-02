import django_filters 
from .models import Blog, Tag, CAT_CHOICES
 

# class BlogFilter(django_filters.FilterSet):
#     class Meta:
#         model = Blog
#         fields = ('title', 'text')

class BlogFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=CAT_CHOICES)
    title = django_filters.CharFilter(field_name='title', lookup_expr='incontains', label='по заголовку')
    tags = django_filters.ModelMultipleChoiceFilter(label='тег', filed_name='tag', queryset=Tag.objects.all())
    

    class Meta:
        model = Blog
        fields = []
