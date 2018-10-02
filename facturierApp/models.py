# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.

class Client(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    tel = models.IntegerField()


class Produit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()


class LigneCmd(models.Model):
    produit = models.ForeignKey(Produit, null=True, blank=True)
    quantity = models.IntegerField()


class Devis(models.Model):
    listProduit = models.ForeignKey(LigneCmd, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    dateValid = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")


class Facture(models.Model):
    listProduit = models.ForeignKey(LigneCmd, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    dateCreation = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    dateValid = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")
    payment = models.CharField(max_length=100)
