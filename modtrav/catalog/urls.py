from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^activities/$', views.ActivityListView.as_view(), name='activities'),
    url(r'^activity/(?P<pk>\d+)$', views.ActivityDetailView.as_view(), name='activity-detail'),
    url(r'^activity/create$', views.ActivityCreate.as_view(), name='activity_create'),
    url(r'^activity/(?P<pk>\d+)/update/$', views.ActivityUpdate.as_view(), name='activity_update'),
    url(r'^activity/(?P<pk>\d+)/update/$', views.ActivityDelete.as_view(), name='activity_delete'),
    url(r'^tags/$', views.TagListView.as_view(), name='tags'),
    url(r'^tag/create$', views.TagCreate.as_view(), name='tag_create'),
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^location/create$', views.LocationCreate.as_view(), name='location_create'),
    url(r'^location/(?P<pk>\d+)/delete/$', views.LocationDelete.as_view(), name='location_delete'),

]
