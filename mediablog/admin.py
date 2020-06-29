from django.contrib import admin
from mediablog.models import *
# Register your models here.

admin.site.register(MediaBlog)
admin.site.register(Comment)
admin.site.register(Reaction)

