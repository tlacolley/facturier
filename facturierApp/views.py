# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from weasyprint import HTML, CSS
from django_weasyprint import  WeasyTemplateResponseMixin

from django.core.mail import EmailMessage

from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill, STATUS_CHOICES
from .forms import *
from .ajax_views import *


class IndexView(ListView):
    model = Customer

    template_name = 'facturierApp/index.html'

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['all_products'] = Product.objects.all()
        return context

# Customers views

class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        query = self.request.GET.get('q',None)
        print query
        if query != None:
            return Customer.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        else:
            return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView,self).get_context_data(**kwargs)
        context["quotations"] = Quotation.objects.all()
        return context


class CustomerRemoveView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')


# Products views

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        print query
        if query != None:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductRemoveView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


# Quotation viewsdz

class QuotationListView(ListView):
    model = Quotation

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['products'] = Product.objects.all()
        context['line_quotation'] = LineQuotation.objects.all()
        return context


    def get_queryset(self):
        query = self.request.GET.get('q', None)
        # date = self.request.GET.get('datePickerInput',None)
        order = self.request.GET.get('orderByFilter', None)
        status = self.request.GET.get('selectStatus', None)

        if query != None:
            return Quotation.objects.filter(Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query))

        elif order != None:
            if order == 'customer':
                return Quotation.objects.order_by("-"+order)
            else:
                return Quotation.objects.order_by(order)

        elif status != None:
            return Quotation.objects.filter(status=status)

        else:
            return Quotation.objects.all()


class QuotationDetailView(DetailView):
    model = Quotation
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['identity_quot'] = self.kwargs['pk']
        context['status_choices'] = STATUS_CHOICES
        context['payment_choice'] = Bill.PAYMENT_CHOICES
        context['products'] = Product.objects.all()
        context['line_quotation'] = LineQuotation.objects.filter(quotation = self.object)
        context["line_quotation_form"] = LineQuotationForm(initial={"quotation" : self.object})
        context["line_quotation_delete"] = LineQuotationDelete
        return context



class QuotationDetailPDFSend(WeasyTemplateResponseMixin, View):
    model = Quotation

    def get(self, request, pk, **kwargs):

        quotation=  Quotation.objects.get(pk=pk)
        user_infor = quotation.customer
        html = render_to_string('facturierApp/quotation_detail.html',
                        {'quotation': quotation,
                        'pdf' : True
                        })

        pdf = HTML(string=html, base_url='http://127.0.0.1:8000/quotation/'+str(quotation.pk)+'/').write_pdf(
        stylesheets=[CSS(string='body { font-family: serif}')])

        to_emails = [str(user_infor.email),]
        subject = "Quotation " + user_infor.full_name()
        email = EmailMessage(subject, from_email='thomaslacolley@gmail.com', to=to_emails)

        email.attach("certificate_{}".format(user_infor.full_name()) + '.pdf', pdf, "application/pdf")
        email.content_subtype = "pdf"  # Main content is now text/html

        print email
        email.encoding = 'us-ascii'
        email.send()

        return HttpResponseRedirect(reverse('quotation_detail', args=[quotation.pk] ))


class QuotationDetailPDFView(WeasyTemplateResponseMixin, QuotationDetailView):
    # pass

    def get_context_data(self, **kwargs):
        context = QuotationDetailView.get_context_data(self, **kwargs)
        context['pdf'] = True
        return context


class BillListView(ListView):
    model = Bill

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context['products'] = Product.objects.all()
        context['line_bill'] = LineBill.objects.all()
        return context


class BillDetailView(DetailView):
    model = Bill

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['identity_bill'] = self.kwargs['pk']
        context['products'] = Product.objects.all()
        context['line_bill'] = LineBill.objects.filter(bill = self.object)

        return context


class BillDetailPDFView(WeasyTemplateResponseMixin, BillDetailView):
    # pass
    def get_context_data(self, **kwargs):
        context = BillDetailView.get_context_data(self, **kwargs)
        context['pdf'] = True
        return context


class BillDetailPDFSend(WeasyTemplateResponseMixin, View):
    model = Bill

    def get(self, request, pk, **kwargs):
        bill=  Bill.objects.get(pk=pk)
        user_infor = bill.customer
        html = render_to_string('facturierApp/bill_detail.html',
                        {'bill': bill,
                        'pdf' : True
                        })
        pdf = HTML(string=html, base_url='http://127.0.0.1:8000/quotation/'+str(bill.pk)+'/').write_pdf(
        )
        to_emails = [str(user_infor.email)]
        subject = "Bill " + user_infor.full_name()
        email = EmailMessage(subject, from_email='thomaslacolley@gmail.com', to=to_emails)

        email.attach("certificate_{}".format(user_infor.full_name()) + '.pdf', pdf, "application/pdf")
        email.content_subtype = "pdf"  # Main content is now text/html

        print email
        email.encoding = 'us-ascii'
        email.send()

        return HttpResponseRedirect(reverse('bill_detail', args=[bill.pk] ))
