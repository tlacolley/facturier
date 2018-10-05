# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Client, Produit, LigneCmd, Devis, Facture
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        query = self.request.GET.get('q',None)
        print query
        if query != None:
            return Client.objects.filter(Q(firstname__icontains=query) | Q(lastname__icontains=query))
        else:
            return Client.objects.all()


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = "__all__"

    def get_success_url(self):
        return reverse('client_detail', args=[self.object.slug])

class ClientDetailView(DetailView):
    model = Client

class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = "__all__"

    def get_success_url(self):
        return reverse('client_detail', args=[self.object.slug])

class ClientRemoveView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')