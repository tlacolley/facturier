
import json
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import View
from django.template.loader import render_to_string
from django.views.generic import CreateView, DeleteView
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill, STATUS_CHOICES
from .forms import *



@method_decorator(csrf_exempt, name='dispatch')
class QuotationFieldEditView(View):
    def post(self, request, pk, update_field, **kwargs):
        quotation = Quotation.objects.get(id=pk)
        if update_field.startswith("customer."):
            update_field = update_field.replace("customer.", "")
            setattr(quotation.customer, update_field, request.POST.get("value"))
            quotation.customer.save()
        elif update_field.startswith("line."):
            update_field = update_field.replace("line.", "")
            line = quotation.linequotation_set.get(id=request.POST.get("pk"))
            setattr(line, update_field, request.POST.get("value"))
            line.save()
            html = render_to_string("facturierApp/partials/quotation_lines.html", context={"quotation" : quotation })
            return JsonResponse({"updatedLines" : html})
        else:
            setattr(quotation, update_field, request.POST.get("value"))
            quotation.save()

        return HttpResponse('plop')


@method_decorator(csrf_exempt, name="dispatch")
class QuotationLineCreateView(CreateView):
    model = LineQuotation
    form_class = LineQuotationForm

    # def post(self, request, **kwargs):
    #
    #     product_id = request.POST.get("product")
    #     product = Product.objects.get(id=product_id)
    #     quotation_id = request.POST.get("quotation")
    #     quotation = Quotation.objects.get(id=quotation_id)
    #     quantity = request.POST.get("quantity")
    #     creation_line = LineQuotation.objects.create(product=product,quantity=quantity,quotation=quotation)
    #     creation_line.save()
    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string("facturierApp/partials/quotation_lines.html",
        context={"quotation": self.object.quotation })

        return JsonResponse({"updatedLines" : html})




@method_decorator(csrf_exempt, name="dispatch")
class QuotationLineDeleteView(DeleteView):

    def post(self, request, **kwargs):
        line = LineQuotation.objects.get(pk=request.POST.get('pk'))
        line.delete()
        return HttpResponse({'success': True})


@method_decorator(csrf_exempt, name="dispatch")
class QuotationValidationView(View):
    model = Quotation

    def post(self, request, **kwargs):
        quotaion_id = request.POST.get('idQuotation')
        quotation = Quotation.objects.get(pk=quotaion_id)
        quotation_custo = quotation.customer.id
        customer = Customer.objects.get(pk=quotation_custo)
        payment_choice = request.POST.get('selectPayment')
        print payment_choice
        create_bill = Bill.objects.create(customer=customer, payment=payment_choice)
        linesQuotation = quotation.linequotation_set.all()

        for lineQ in linesQuotation:
            creation_line_bill = LineBill.objects.create(product=lineQ.product,quantity=lineQ.quantity,bill=create_bill)



        return HttpResponse({'success': True})


    # def form_valid(self, form):
    #     self.object = form.save()
    #     html = render_to_string("facturierApp/partials/quotation_lines.html",
    #     context={"quotation": self.object.quotation })
    #
    #     return JsonResponse({"updatedLines" : html})
