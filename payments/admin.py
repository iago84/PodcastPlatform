
# Register your models here.
from .models import Payment
from .models import Invoice
from .models import Payout

# admin.py
from django.contrib import admin


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	list_display = ('amount', 'method', 'status', 'date_created', 'model_state')
	search_fields = ('method', 'status')
	list_filter = ('date_created', 'status')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	list_display = ('number', 'total_amount', 'paid', 'date_created', 'model_state')
	search_fields = ('number',)
	list_filter = ('date_created', 'paid')


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
	list_display = ('recipient', 'amount', 'status', 'date_created', 'model_state')
	search_fields = ('recipient', 'status')
	list_filter = ('date_created', 'status')
