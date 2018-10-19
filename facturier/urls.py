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
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from facturierApp.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page="/")),
    url(r'^$', IndexView.as_view(), name="index"),


    url(r'^customer/$', CustomerListView.as_view(), name="customer_list"),
    url(r'^customer/create/$', CustomerCreateView.as_view(), name="customer_create"),
    url(r'^customer/(?P<slug>[\w-]+)/$', CustomerDetailView.as_view(), name="customer_detail"),
    url(r'^customer/(?P<slug>[\w-]+)/edit/$', CustomerUpdate.as_view(), name="customer_update"),
    url(r'^customer/(?P<slug>[\w-]+)/remove/$', CustomerRemoveView.as_view(), name="customer_remove"),

    url(r'^product/$', ProductListView.as_view(), name="product_list"),
    url(r'^product/create/$', ProductCreateView.as_view(), name="product_create"),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^product/(?P<slug>[\w-]+)/edit/$', ProductUpdate.as_view(), name="product_update"),
    url(r'^product/(?P<slug>[\w-]+)/remove/$', ProductRemoveView.as_view(), name="product_remove"),

    url(r'^quotation/$', QuotationListView.as_view(), name="quotation_list"),
    url(r'^quotation/(?P<pk>\d+)/$', QuotationDetailView.as_view(), name="quotation_detail"),
    url(r'^quotation/(?P<pk>\d+)/(?P<update_field>[.\w]+)/$', QuotationFieldEditView.as_view(), name="quotation_field_edit"),

    url(r'^quotation/create/$', QuotationCreateView.as_view(), name="quotation_create"),
    url(r'^quotation/line/create/$', QuotationLineCreateView.as_view(), name="quotation_line_create"),
    url(r'^quotation/line/delete/$', QuotationLineDeleteView.as_view(), name="quotation_line_delete"),
    url(r'^quotation/validation/$', QuotationValidationView.as_view(), name="quotation_valid"),
]
