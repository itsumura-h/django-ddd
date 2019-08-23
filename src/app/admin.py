from django.contrib import admin
from .models import SamplePermission, SampleUser

# Register your models here.
admin.site.register(SamplePermission)
admin.site.register(SampleUser)
