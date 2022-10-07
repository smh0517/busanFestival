import django
from django.contrib import admin
from django.urls import path,include
from location import views
from . import views as c_views

urlpatterns = [
    path('index/', c_views.index),
    path('admin/', admin.site.urls),
    path('map/', c_views.map),
    path('map_data/', c_views.map_data),  ##여기에 맵정보 담겨있음
    path('contact/', c_views.contact),
    path('', c_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('party_data/',views.party_data),
    path('location/', include('location.urls')),
]
