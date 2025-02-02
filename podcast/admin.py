from django.contrib import admin

# Register your models here.
from .models import Episode
from .models import Category
from .models import Statistic
from .models import Comment
from .models import Download

admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Statistic)
admin.site.register(Comment)
admin.site.register(Download)
