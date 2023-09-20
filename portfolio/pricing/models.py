from django.db import models

# Create your models here.
class pricing(models.Model):
    
    price = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.price
    
class faqs(models.Model):
    question = models.CharField(max_length=100, blank=False)
    answer = models.TextField(max_length=205, blank=False)
   

    def __str__(self):
        return self.question