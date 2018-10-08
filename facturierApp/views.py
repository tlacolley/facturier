# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import CreateWithInlinesView, InlineFormSet
from datetime import datetime
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill


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


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView,self).get_context_data(**kwargs)
        context["quotations"] = Quotation.objects.all()
        return context



class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class ProductRemoveView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class LineQuotationInline(InlineFormSet):
    model = LineQuotation
    fields = "__all__"
    # can_delete = True

class QuotationCreateView(CreateWithInlinesView):
    model = Quotation
    inlines = [LineQuotationInline,]
    fields = "__all__"
    inlines_names = ['quotations',]

    # inlines = [Customer, Product]


    def get_context_data(self, **kwargs):
        context = super(QuotationCreateView, self).get_context_data(**kwargs)
        context["customer"] = Customer.objects.all()
        context['lineQuotation'] = LineQuotation.objects.all()
        return context

    def get_success_url(self):
        return reverse('index')
