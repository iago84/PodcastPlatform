from django.contrib import admin

# Register your models here.
from .models import Plan
from .models import Subscription
from .models import Transaction

from django.contrib import admin
from .models import Plan, Subscription, Transaction

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_state', 'date_created', 'date_modified', 'price', 'duration_months')
    list_filter = ('model_state',)
    search_fields = ('name', 'description')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'start_date', 'end_date', 'status', 'model_state', 'date_created', 'date_modified')
    list_filter = ('status', 'model_state')
    search_fields = ('user__username', 'plan__name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription', 'amount', 'payment_method', 'transaction_date', 'transaction_status', 'model_state', 'date_created', 'date_modified')
    list_filter = ('transaction_status', 'payment_method', 'model_state')
    search_fields = ('subscription__user__username',)

admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Transaction, TransactionAdmin)

