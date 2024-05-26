from django.contrib import admin
from .models import hospital,medical,User
admin.site.register(User)
admin.site.register(hospital)
admin.site.register(medical)
# Register your models here.
