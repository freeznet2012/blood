from donor.models import Donor
from .models import Rrc
import django_filters

class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ['blood', 'district',]


class RrcFilter(django_filters.FilterSet):
    class Meta:
        model = Rrc
        fields = ['district', ]