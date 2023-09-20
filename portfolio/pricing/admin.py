from django.contrib import admin

# Register your models here.

from .models import pricing
from .models import faqs


# Register your models here.
admin.site.register(pricing)
admin.site.register(faqs)



