from django.contrib import admin

# Register your models here.
from .models import Tag, Location, Activity

admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Activity)
