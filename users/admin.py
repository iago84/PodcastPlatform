from django.contrib import admin

# Register your models here.
from .models import UserProfile
from .models import Role
from .models import Permission
from .models import Message

admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Message)
