"""
CREAT: 2017/12/23
AUTHOR:　HEHAHUTU
"""
from django.conf.urls import include, url
from rest_framework import routers
from taskApi import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]