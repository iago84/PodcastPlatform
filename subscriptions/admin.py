from django.contrib import admin

# Register your models here.
from .models import Plan
from .models import Subscription
from .models import Transaction

admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Transaction)
