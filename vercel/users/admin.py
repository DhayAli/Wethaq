from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import RegularUser, Observer, PrisonDirector

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active')
    search_fields = ('fullname', 'mobile')
    ordering = ('-date_joined',)

admin.site.register(RegularUser, UserAdmin)
admin.site.register(Observer, UserAdmin)
admin.site.register(PrisonDirector, UserAdmin)
