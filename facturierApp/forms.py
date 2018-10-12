from django import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, View


from extra_views import CreateWithInlinesView, InlineFormSet
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class LineQuotationInline(InlineFormSet):
    model = LineQuotation
    fields = "__all__"
    # can_delete = True


class QuotationCreateView(CreateWithInlinesView):
    model = Quotation
    inlines = [LineQuotationInline,]
    fields = "__all__"

    def get_context_data(self,**kwargs):
        context = super(QuotationCreateView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return context

    def get_success_url(self):
        return reverse('index')
