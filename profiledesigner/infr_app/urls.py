"""
URL configuration for profiledesigner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import index, list_dns, list_kns, list_objects_nominal_parameters, list_pads, list_wells, main_menu, show_prognose

urlpatterns = [
    # path('', index),
    # path('dns', list_dns),
    # path('kns', list_kns),
    # path('pad', list_pads),
    # path('well', list_wells),
    # path('prognose', show_prognose),
    path('main', main_menu),
    path('<str:obj_>/', list_objects_nominal_parameters),
]
