from django.contrib import admin
from .models import Permission, User

# Register your models here.
admin.site.register(Permission)
admin.site.register(User)
