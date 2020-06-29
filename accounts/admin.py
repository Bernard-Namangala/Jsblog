from django.contrib import admin
from accounts.models import *
# Register your models here.

admin.site.register(RegularUser)
admin.site.register(OrganizationUser)
