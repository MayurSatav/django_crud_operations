from django.shortcuts import render, redirect, HttpResponse
from .models import InvoiceList
import os
from .forms import browse
from .models import handle_uploaded_file 
from invoice2data import extract_data

# Create your views here.

def index(request):
    invoices = InvoiceList.objects.all()
    context = {
        'invoices': invoices,
    }
    return (render(request, 'index.html', context))

def create(request):
    print(request.POST)
    issuer = request.GET['issuer']
    invoice_number = request.GET['invoice_number']
    date = request.GET['date']
    amount = request.GET['amount']
    currency = request.GET['currency']
    other = request.GET['other']
    invoice_details = InvoiceList(issuer=issuer, invoice_number=invoice_number, date=date,amount=amount,currency=currency,other=other)
    invoice_details.save()
    return redirect('/')

file_list = os.listdir("extraction/static/upload")
def add_invoice(request):
    result = None
    form = None
    if request.method == 'POST':  
        form = browse(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['file']) # store file in upload folder
            path = "pdfextractor/static/upload/"+ str(request.FILES['file'])#path of selected file
            result1 = extract_data(path) # extract data from invoice pdf file
            listl=['issuer','invoice_number','date','amount','currency']
            new_in_dict={}
            c={}
            for key in result1:
                if key in listl:
                    new_in_dict[key]=result1[key]
                else:
                    c[key]=result1[key]

            new_in_dict['other']=c
            result = new_in_dict # this is final dictionary
            
    else:
        form = browse()
    context = {"form": form, "result": result}
    return render(request,'add_invoice.html', context)
    #return render(request, 'add_invoice.html')



def delete(request, id):
    invoices = InvoiceList.objects.get(pk=id)
    invoices.delete()
    return redirect('/')

def edit(request, id):
    invoices = InvoiceList.objects.get(pk=id)
    context = {
        'invoices': invoices
    }
    return render(request, 'edit.html', context)


def update(request, id):
    invoices = InvoiceList.objects.get(pk=id)

    invoices.issuer = request.GET['issuer']
    invoices.invoice_number = request.GET['invoice_number']
    invoices.date = request.GET['date']
    invoices.amount = request.GET['amount']
    invoices.currency = request.GET['currency']
    invoices.other = request.GET['other']
    invoices.save()
    return redirect('/')