
from extra_views import CreateWithInlinesView, InlineFormSet
from .models import Customer, Product, LineQuotation, LineBill, Quotation, Bill




class LineQuotationInline(InlineFormSet):
    model = LineQuotation
    fields = "__all__"
    # can_delete = True


class QuotationCreateView(CreateWithInlinesView):
    model = Quotation
    inlines = [LineQuotationInline,]
    fields = "__all__"
    inlines_names = ['quotations',]

    # inlines = [Customer, Product]

    def get_context_data(self, **kwargs):
        context = super(QuotationCreateView, self).get_context_data(**kwargs)
        context["customer"] = Customer.objects.all()
        context['lineQuotation'] = LineQuotation.objects.all()
        return context


    def get_success_url(self):
        return reverse('index')
