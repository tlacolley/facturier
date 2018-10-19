# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill, STATUS_CHOICES
from .forms import *
from .ajax_views import *


class IndexView(ListView):
    model = Customer

    template_name = 'facturierApp/index.html'

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['all_products'] = Product.objects.all()
        return context

# Customers views

class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        query = self.request.GET.get('q',None)
        print query
        if query != None:
            return Customer.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView,self).get_context_data(**kwargs)
        context["quotations"] = Quotation.objects.all()
        return context


class CustomerRemoveView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')


# Products views

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        print query
        if query != None:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductRemoveView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


# Quotation viewsdz

class QuotationListView(ListView):
    model = Quotation

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['products'] = Product.objects.all()
        context['line_quotation'] = LineQuotation.objects.all()
        return context


    def get_queryset(self):
        query = self.request.GET.get('q', None)
        # date = self.request.GET.get('datePickerInput',None)
        order = self.request.GET.get('orderByFilter', None)
        status = self.request.GET.get('selectStatus', None)

        if query != None:
            return Quotation.objects.filter(Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query))

        elif order != None:
            if order == 'customer':
                return Quotation.objects.order_by("-"+order)
            else:
                return Quotation.objects.order_by(order)

        elif status != None:
            return Quotation.objects.filter(status=status)

        else:
            return Quotation.objects.all()


class QuotationDetailView(DetailView):
    model = Quotation

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['identity_quot'] = self.kwargs['pk']
        context['status_choices'] = STATUS_CHOICES
        context['products'] = Product.objects.all()
        context['line_quotation'] = LineQuotation.objects.filter(quotation = self.object)
        context["line_quotation_form"] = LineQuotationForm(initial={"quotation" : self.object})
        context["line_quotation_delete"] = LineQuotationDelete
        return context
