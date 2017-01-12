from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoices.models import Invoice
from invoices.serializers import InvoiceSerializer

@api_view(['GET'])
def invoice_list(request):
    if request.method=='GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)