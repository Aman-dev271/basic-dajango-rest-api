from django.contrib import admin
from Apiaap.models import student
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class studentAdmin(ModelAdmin):
    list_display = ["s_name"]
    list_filter = ["id"]
    list_per_page  = 2
admin.site.register(student, studentAdmin)

