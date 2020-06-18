from django.contrib import admin
from django.urls import path

from .views import HomePageView, ServicesPageView, BookedTableCreateView
from .views import  about_view


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('services/', ServicesPageView.as_view(), name='services'),
  path('booking/',BookedTableCreateView.as_view(), name='booking'),
  path('about/', about_view, name='about'),
]


