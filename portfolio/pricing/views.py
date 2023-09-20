from django.shortcuts import render
from .models import pricing
from .models import faqs
# Create your views here.
def pricings(request):
    pricingdata = pricing.objects.all()
    faqsdata = faqs.objects.all()
    context = {
        'price': pricingdata,
        'faqs': faqsdata
    }

    return render(request, 'pricing.html', context)
