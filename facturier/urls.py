"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView
from facturierApp.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdate



urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^$',ClientListView.as_view(), name="client_list"),
    url(r'^client/create/$',ClientCreateView.as_view(), name="client_create"),

    url(r'^client/(?P<slug>[\w-]+/$)', ClientDetailView.as_view(), name="client_detail"),
    url(r'^client/(?P<slug>[\w-]+/edit/$)', ClientUpdate.as_view(), name="client_update"),
]
