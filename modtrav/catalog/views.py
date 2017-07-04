from django.shortcuts import render

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tag, Location, Activity

# Create your views here.
def index(request):
    '''
    View function for the homepage of the site.
    '''
    # Generate counts of the main objects
    num_activities = Activity.objects.all().count()
    num_locations = Location.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_activities':num_activities,
            'num_locations':num_locations,
        },
    )

class ActivityListView(generic.ListView):
    model = Activity

class ActivityDetailView(generic.DetailView):
    model = Activity

#TODO make all create/delete/update things permissions required
class ActivityCreate(CreateView):
    model = Activity
    fields = '__all__'

class ActivityUpdate(UpdateView):
    model = Activity
    fields = '__all__'

class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('activities')

class TagListView(generic.ListView):
    model = Tag

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('tags')

class LocationListView(generic.ListView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'
    success_url = reverse_lazy('locations')

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')
