"""
CREAT: 2017/12/23
AUTHOR:　HEHAHUTU
"""
from django.conf.urls import include, url
from rest_framework import routers
from taskApi import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]