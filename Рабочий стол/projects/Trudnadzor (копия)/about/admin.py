from django.contrib import admin
from .models import *


class EduAdmin(admin.TabularInline):
    model = Education


class ExpAdmin(admin.TabularInline):
    model = Exp


class ManagementAdmin(admin.ModelAdmin):
    inlines = [EduAdmin, ExpAdmin]


admin.site.register(Management, ManagementAdmin)
admin.site.register(Structure)
admin.site.register(Category)

