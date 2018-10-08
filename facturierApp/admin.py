# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Customer, Product, LigneDevis, LigneBill, Devis, Bill



# Customer et products

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug',
                    'email', 'address', 'phone')
    readonly_fields = ('slug',)
    fieldsets = (
        ('General', {
            'fields': (('first_name', 'last_name', 'slug'),
                       ('email', 'address', 'phone')
                       ),
        }),
    )

    search_fields = ('first_name', 'last_name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'stock')
    fieldsets = (
        ('General', {
            'fields': (('name', ),
                       ('price', 'stock')
                       ),
        }),
        ('Content', {
            'fields': (('description',)
                       ),
        }),
    )

    search_fields = ('name', 'price')

# Lignes de commandes

class LigneDevisAdmin(admin.StackedInline):
    model = LigneDevis


class LigneBillAdmin(admin.StackedInline):
    model = LigneBill


# Devis et bill

class DevisAdmin(admin.ModelAdmin):
    inlines = [
        LigneDevisAdmin,
    ]
    list_display = ('customer', 'created_at', 'validated_at')
    fieldsets = (
        ('General', {
            'fields': (('customer',),
                       ('created_at', 'validated_at')
                       ),
        }),
    )

    search_fields = ('customer', 'created_at', 'validated_at')




class BillAdmin(admin.ModelAdmin):
    inlines = [
        LigneBillAdmin,
    ]
    list_display = ('customer', 'created_at', 'validated_at', 'payment')
    fieldsets = (
        ('General', {
            'fields': (('customer',),
                       ('created_at', 'validated_at', 'payment')
                       ),
        }),
    )

    search_fields = ('customer', 'created_at', 'validated_at', 'payment')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Devis, DevisAdmin)
admin.site.register(Bill, BillAdmin)
