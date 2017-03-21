from django.conf.urls import include, url
from django.contrib import admin

from .views import (ProjectsCreateView)

urlpatterns = [
	   url(r'^$', ProjectsCreateView.as_view(), name='users'),

]
