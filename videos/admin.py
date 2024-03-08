from django.contrib import admin

from videos.models import Category,Video,Feedback

# Register your models here.
admin.site.register(Video),
admin.site.register(Category),
admin.site.register(Feedback),
