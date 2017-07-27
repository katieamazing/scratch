import markdown

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Tag(models.Model):
    '''
    Model representing a tag given to an activity:
    (e.g. 'breakfast', 'nerdy', 'good for kids', 'rainy day').
    '''
    tag = models.CharField(max_length=200, help_text='Enter a tag for this activity to help people find it.')

    def __str__(self):
        return self.tag


class Location(models.Model):
    '''
    Model representing a location for an activity.
    '''
    location = models.CharField(max_length=200, help_text='Enter a location for this activity.')

    def __str__(self):
        return self.location


class Activity(models.Model):
    '''
    Model representing an activity.
    '''
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the activity.') #Markdown
    summary_html = models.TextField(max_length=1000, editable=False)
    cost = models.IntegerField(help_text='Enter an approximate median cost for this activity.')
    duration = models.IntegerField(help_text='Enter an approximate number of hours this activity might take.')

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = models.ManyToManyField(Location, help_text='Select a location for this activity.')
    tag = models.ManyToManyField(Tag, help_text='Enter a tag for this activity to help people find it.')

    def save(self, *args, **kwargs):
        self.summary_html = markdown.markdown(self.summary, safe_mode='escape') #TODO implement cleaner/safer HTML
        super(Activity, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular activity instance.
        """
        return reverse('activity-detail', args=[str(self.id)])
