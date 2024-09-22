from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('CalorieCounter1.urls')),
    path('admin/', admin.site.urls),
]
