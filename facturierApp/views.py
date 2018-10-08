# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Customer, Product, LigneDevis, LigneBill, Devis, Bill
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


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

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])

class CustomerRemoveView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')
