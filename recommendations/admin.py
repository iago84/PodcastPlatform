from django.contrib import admin

# Register your models here.
from .models import Recommendation
from .models import Algorithm

admin.site.register(Recommendation)
admin.site.register(Algorithm)
