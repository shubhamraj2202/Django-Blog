from django.conf.urls import url
from . import views
import re

urlpatterns = [url( r'^$', views.index , name='index'),
               url(r'^contact/$', views.contact , name='contact')]