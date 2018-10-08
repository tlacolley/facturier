# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill



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

# Lines de commandes

class LineQuotationAdmin(admin.StackedInline):
    model = LineQuotation


class LineBillAdmin(admin.StackedInline):
    model = LineBill


# Quotation et bill

class QuotationAdmin(admin.ModelAdmin):
    inlines = [
        LineQuotationAdmin,
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
        LineBillAdmin,
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
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Bill, BillAdmin)
