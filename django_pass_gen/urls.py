from django.contrib import admin
from django.urls import path

from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('about', views.about),
    path('', views.home),
    path('generate-password', views.password, name='password')
]
