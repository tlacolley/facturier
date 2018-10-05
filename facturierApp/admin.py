# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Client, Produit, LigneDevis, LigneFacture, Devis, Facture


# Clients et produits

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug',
                    'email', 'address', 'phone')
    fieldsets = (
        ('General', {
            'fields': (('first_name', 'last_name', 'slug'),
                       ('email', 'address', 'phone')
                       ),
        }),
    )

    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    search_fields = ('first_name', 'last_name')


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'price', 'stock')
    fieldsets = (
        ('General', {
            'fields': (('name', 'slug'),
                       ('price', 'stock')
                       ),
        }),
        ('Content', {
            'fields': (('description',)
                       ),
        }),
    )

    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'price')

# Lignes de commandes

class LigneDevisAdmin(admin.StackedInline):
    model = LigneDevis


class LigneFactureAdmin(admin.StackedInline):
    model = LigneFacture


# Devis et facture

class DevisAdmin(admin.ModelAdmin):
    inlines = [
        LigneDevisAdmin,
    ]
    list_display = ('client', 'dateCreation', 'dateValid')
    fieldsets = (
        ('General', {
            'fields': (('client',),
                       ('dateCreation', 'dateValid')
                       ),
        }),
    )

    search_fields = ('client', 'dateCreation', 'dateValid')


class FactureAdmin(admin.ModelAdmin):
    inlines = [
        LigneFactureAdmin,
    ]
    list_display = ('client', 'dateCreation', 'dateValid', 'payment')
    fieldsets = (
        ('General', {
            'fields': (('client',),
                       ('dateCreation', 'dateValid', 'payment')
                       ),
        }),
    )

    search_fields = ('client', 'dateCreation', 'dateValid', 'payment')


admin.site.register(Client, ClientAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Devis, DevisAdmin)
admin.site.register(Facture, FactureAdmin)
