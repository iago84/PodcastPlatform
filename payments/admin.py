from django.contrib import admin

# Register your models here.
from .models import Payment
from .models import Invoice
from .models import Payout

admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Payout)
