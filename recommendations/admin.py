from django.contrib import admin

# Register your models here.
from .models import Recommendation
from .models import Algorithm

from django.contrib import admin
from .models import Recommendation, Algorithm

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_state', 'date_created', 'date_modified', 'user_rating', 'is_active')
    list_filter = ('model_state', 'is_active')
    search_fields = ('name', 'description',)

class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_state', 'date_created', 'date_modified', 'version', 'last_run')
    list_filter = ('model_state', 'version')
    search_fields = ('name', 'description',)

admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Algorithm, AlgorithmAdmin)

