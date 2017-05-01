from .models import Request
import django_filters


class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        fields = ['district', 'blood',]