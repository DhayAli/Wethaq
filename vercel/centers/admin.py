from django.contrib import admin
from django import forms

from users.models import RegularUser
from .models import Center, CenterUser

class CenterUserInlineForm(forms.ModelForm):
    class Meta:
        model = CenterUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Access the current CenterUser instance if editing an existing one
        if self.instance and self.instance.pk:
            # Exclude all users that are already assigned to the current center
            current_center_users_ids = CenterUser.objects.values_list('user', flat=True)
            current_center_users_ids = list(current_center_users_ids)
            current_user_id = self.instance.user_id
            current_center_users_ids.remove(current_user_id)
            self.fields['user'].queryset = RegularUser.objects.exclude(id__in=current_center_users_ids)



class CenterUserInline(admin.TabularInline):
    model = CenterUser
    extra = 1
    form = CenterUserInlineForm

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    inlines = [CenterUserInline]
    

@admin.register(CenterUser)
class CenterUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'center')