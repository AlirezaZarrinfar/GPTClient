from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Chat

class ChatAdminForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'
        widgets = {
            'send': forms.Textarea(attrs={'rows': 3, 'cols': 40}), 
            'response': forms.Textarea(attrs={'rows': 3, 'cols': 40}), 
        }

class ChatInline(admin.TabularInline):
    model = Chat
    extra = 1
    form = ChatAdminForm

class UserAdmin(DefaultUserAdmin):
    inlines = [ChatInline]

admin.site.unregister(User) 
admin.site.register(User, UserAdmin)
