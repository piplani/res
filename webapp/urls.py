from django.conf.urls import url
from . import views
import os

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

