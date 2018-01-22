"""
CREAT: 2017/12/23
AUTHOR:　HEHAHUTU
"""
from django.conf.urls import include, url
from rest_framework import routers
from taskApi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tasks', views.TaskList.as_view()),
    url(r'^create_task', views.CreateTask.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
