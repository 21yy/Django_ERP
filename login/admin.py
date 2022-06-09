from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Company)
admin.site.register(models.Position)
