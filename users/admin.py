from django.contrib import admin
from .models import UserProfile, Role, Permission, Message

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'model_state', 'date_created', 'date_modified', 'phone_number')
    list_filter = ('model_state',)
    search_fields = ('user__username', 'bio')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_state', 'date_created', 'date_modified')
    list_filter = ('model_state',)
    search_fields = ('name', 'description')

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model_state', 'date_created', 'date_modified')
    list_filter = ('model_state',)
    search_fields = ('name', 'description')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'subject', 'date_created', 'read')
    list_filter = ('read', 'model_state')
    search_fields = ('sender__username', 'receiver__username', 'subject')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Message, MessageAdmin)

