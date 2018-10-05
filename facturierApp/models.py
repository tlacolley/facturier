# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField

# Clients et produits

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from=['first_name', 'last_name'])
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = PhoneNumberField()


class Produit(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()

# Devis et facture

class Devis(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    validated_at = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")


class Facture(models.Model):
    PAYMENT_CHOICES = (
        ('CASH', 'cash'),
        ('CARD', 'card'),
        ('CHECK', 'check'),
        ('PAYPAL', 'paypal'),
        ('BITCOIN', 'bitcoin'),
    )
    client = models.ForeignKey(Client, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    validated_at = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")
    payment = models.CharField(choices=PAYMENT_CHOICES, default='CASH')

# Lignes de commandes

class LigneDevis(models.Model):
    produit = models.ForeignKey(Produit, null=True, blank=True)
    quantity = models.IntegerField()
    devis = models.ForeignKey(Devis, null=True, blank=True)

class LigneFacture(models.Model):
    produit = models.ForeignKey(Produit, null=True, blank=True)
    quantity = models.IntegerField()
    devis = models.ForeignKey(Facture, null=True, blank=True)
