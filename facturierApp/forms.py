from django import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, View


from extra_views import CreateWithInlinesView, InlineFormSet
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill


class CustomerCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "facturierApp.add_customer"
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


class CustomerUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "facturierApp.change_customer"
    model = Customer
    fields = "__all__"

    def get_success_url(self):
        return reverse('customer_detail', args=[self.object.slug])


class ProductCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "facturierApp.add_product"
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class ProductUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "facturierApp.change_product"
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse('product_detail', args=[self.object.slug])


class LineQuotationInline(InlineFormSet):
    model = LineQuotation
    fields = "__all__"
    # can_delete = True


class QuotationCreateView(PermissionRequiredMixin, CreateWithInlinesView):
    permission_required = "facturierApp.add_quotation"
    model = Quotation
    inlines = [LineQuotationInline,]
    fields = "__all__"

    def get_context_data(self,**kwargs):
        context = super(QuotationCreateView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        return context

    def get_success_url(self):
        return reverse('index')



class LineQuotationForm(forms.ModelForm):
    class Meta:
        model = LineQuotation
        fields = "__all__"



class LineQuotationDelete(forms.ModelForm):
    class Meta:
        model = LineQuotation
        fields = "__all__"
