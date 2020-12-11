from django.contrib import admin

# Register your models here.
from .models import PersonInfo,Question

admin.site.register(PersonInfo)
admin.site.register(Question)