from django.db import models

# Create your models here.

class InvoiceList(models.Model):
    issuer = models.CharField(max_length=50)
    invoice_number = models.IntegerField()
    date = models.CharField(max_length=50)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    other = models.CharField(max_length=300)

    def __str__(self):
        return self.issuer

def handle_uploaded_file(f):
    with open('static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)