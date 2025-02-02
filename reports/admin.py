from django.contrib import admin
from .models import Report, FlaggedContent

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model_state', 'date_created', 'date_modified', 'status')
    list_filter = ('status', 'model_state')
    search_fields = ('title', 'content')

class FlaggedContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'model_state', 'date_created', 'date_modified', 'flagged_by')
    list_filter = ('content_type', 'model_state')
    search_fields = ('content_type', 'content_description', 'flagged_by')

admin.site.register(Report, ReportAdmin)
admin.site.register(FlaggedContent, FlaggedContentAdmin)
