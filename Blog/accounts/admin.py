from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'username', 'surname']
    list_display_links = ['id', 'user', 'username', 'surname']
    search_fields = ['id', 'user']


admin.site.register(Profile, ProfileAdmin)
