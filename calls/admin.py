# admin.py
from django.contrib import admin

from calls.models import Call, VideoCall, CallHistory


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('caller', 'receiver', 'duration', 'date_created', 'model_state')
    search_fields = ('caller', 'receiver')
    list_filter = ('date_created', 'model_state')

@admin.register(VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    list_display = ('caller', 'receiver', 'duration', 'video_quality', 'date_created', 'model_state')
    search_fields = ('caller', 'receiver')
    list_filter = ('date_created', 'model_state', 'video_quality')

@admin.register(CallHistory)
class CallHistoryAdmin(admin.ModelAdmin):
    list_display = ('call', 'video_call', 'date_created', 'model_state')
    search_fields = ('notes',)
    list_filter = ('date_created', 'model_state')
