from .models import Activity
from django.contrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']

class ActivityFilter(django_filters.FilterSet):
    class Meta:
        model = Activity
        fields = ['title', 'summary', 'cost', 'duration', 'location', 'tag']
