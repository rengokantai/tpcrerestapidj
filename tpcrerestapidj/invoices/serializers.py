__author__ = 'Hernan Y.Ke'
from rest_framework import serializers
from invoices.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('name','description','total','paid')
