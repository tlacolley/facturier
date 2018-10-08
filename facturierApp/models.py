# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField

# Customer et products

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="full_name", unique=True, always_update=True)


    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone = PhoneNumberField()

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()

# Quotationet bill

class Quotation(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    validated_at = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")



class Bill(models.Model):
    PAYMENT_CHOICES = (
        ('CASH', 'cash'),
        ('CARD', 'card'),
        ('CHECK', 'check'),
        ('PAYPAL', 'paypal'),
        ('BITCOIN', 'bitcoin'),
    )
    customer = models.ForeignKey(Customer, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date de creation")
    validated_at = models.DateTimeField(auto_now=True,
                                verbose_name="Date de validation")
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='CASH')

# Lines de commandes

class LineQuotation(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    quantity = models.IntegerField()
    quotation = models.ForeignKey(Quotation, null=True, blank=True)



class LineBill(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True)
    quantity = models.IntegerField()
    bill = models.ForeignKey(Bill, null=True, blank=True)
