# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Client, Produit, LigneCmd, Devis, Facture
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ClientListView(ListView):
    model = Client


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