#tpcrerestapidj
```
virtualenv env
(linux)source env/bin/activate
```
windows:  
set C:\Python34\ENV\Scripts in PATH, then
```
activate
```

then
```
pip install django djangorestframework
```

```
from invoices.models import Invoice

from invoices.serializers import InvoiceSerializer
invoice = Invoice.objects.get()
invoice.name
serializer = InvoiceSerializer(invoice)
serializer.data
```
