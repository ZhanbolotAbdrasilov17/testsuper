from django.contrib import admin
from .models import *

admin.site.register(Partner)


admin.site.register(Contact)
admin.site.register(CategoryContact)


@admin.register(Mail1)
class MailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'name', 'date')
    search_fields = ('first_name', 'name', 'phone', 'email', 'date')


@admin.register(Mail2)
class MailAdmin1(admin.ModelAdmin):
    list_display = ('organ', 'position', 'first_name', 'name', 'date')
    search_fields = ('first_name', 'name', 'phone', 'email', 'date', 'organ', 'inn', 'position')

