from django.contrib import admin

from .models import Case, Detainee

admin.site.register(Detainee)
admin.site.register(Case)