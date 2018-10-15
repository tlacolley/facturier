
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic.edit import View
from django.utils.decorators import method_decorator
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill

@method_decorator(csrf_exempt, name='dispatch')
class QuotationFieldEditView(View):
    def post(self, request, pk, update_field, **kwargs):
        quotation = Quotation.objects.get(pk=pk)
        setattr(quotation, update_field, request.POST.get("value") )
        quotation.save()
        return HttpResponse()
