
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import View
from django.template.loader import render_to_string
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill
import json

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
