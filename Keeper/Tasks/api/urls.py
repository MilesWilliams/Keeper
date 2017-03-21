from django.conf.urls import include, url
from django.contrib import admin

from .views import (
		  TaskCreateView,
		  TaskDeleteView,
		  TaskDetailView,
		  TaskListApiView,
		  TaskUpdateApiView,
		  ImageUploadView,
		  ImageDeleteView,
		  ImageDetailView
	   )

urlpatterns = [
	   url(r'^$', TaskListApiView.as_view(), name='tasks'),
	   url(r'^create$', TaskCreateView.as_view(), name='tasks-create'),
	   url(r'^delete/(?P<pk>\d+)/$', TaskDeleteView.as_view(), name='tasks-delete'),
	   url(r'^(?P<pk>\d+)/$', TaskDetailView.as_view(), name='tasks-detail'),
	   url(r'^update/(?P<pk>\d+)/$', TaskUpdateApiView.as_view(), name='tasks-update'),
	   url(r'^images/upload$', ImageUploadView.as_view(), name='image-upload'),
	   url(r'^images/delete/(?P<pk>\d+)/$', ImageDeleteView.as_view(), name='image-delete'),
	   url(r'^images/(?P<pk>\d+)$', ImageDetailView.as_view(), name='images'),
]