# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Client, Produit, LigneCmd, Devis, Facture
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from datetime import datetime

# Create your views here.

class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"


class ClientDetailView(DetailView):
    model = Client


class ClientUpdate(UpdateView):
    model = Client
    fields = "__all__"
    pass
