from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'surname']
    list_display_links = ['id', 'username', 'surname']
    search_fields = ['id']


admin.site.register(Profile, ProfileAdmin)
