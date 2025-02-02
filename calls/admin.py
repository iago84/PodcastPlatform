from django.contrib import admin

# Register your models here.
from .models import Call
from .models import VideoCall
from .models import CallHistory

admin.site.register(Call)
admin.site.register(VideoCall)
admin.site.register(CallHistory)
