from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('food_search/', views.finder, name='food_search'),
]