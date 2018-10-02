# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Client, Produit, LigneCmd, Devis, Facture
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'slug', 'email', 'address', 'tel')
	fieldsets = (
		('General',{
			'fields':(('firstname', 'lastname', 'slug'),
					('email', 'address', 'tel')
					),
		} ),
			)
	prepopulated_fields = {'slug' : ('firstname', 'lastname')}

	search_fields = ('firstname', 'lastname')


class ProduitAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'price', 'stock')
	fieldsets = (
		('General',{
			'fields':(('name', 'slug'),
					('price', 'stock')
					),
		} ),
		('Content',{
			'fields':(('description',)
					),
		} ),
			)
	prepopulated_fields = {'slug' : ('name',)}

	search_fields = ('name', 'price')


class LigneCmdAdmin(admin.ModelAdmin):
	list_display = ('produit', 'quantity')


class DevisAdmin(admin.ModelAdmin):
	list_display = ('client', 'dateCreation', 'dateValid')
	fieldsets = (
		('General',{
			'fields':(('client',),
					('dateCreation', 'dateValid')
					),
		} ),
			)

	search_fields = ('client', 'dateCreation', 'dateValid')


class FactureAdmin(admin.ModelAdmin):
	list_display = ('client', 'dateCreation', 'dateValid', 'payment')
	fieldsets = (
		('General',{
			'fields':(('client',),
					('dateCreation', 'dateValid', 'payment')
					),
		} ),
			)

	search_fields = ('client', 'dateCreation', 'dateValid', 'payment')



admin.site.register(Client,ClientAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(LigneCmd,LigneCmdAdmin)
admin.site.register(Devis,DevisAdmin)
admin.site.register(Facture,FactureAdmin)
