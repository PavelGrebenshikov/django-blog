from django.contrib import admin
from django import forms
from .models import Posts, Category, Comments, Resources
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Posts
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    search_fields = ['id', 'category']

class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'create_date', 'published']
    list_filter = ['id', 'author', 'title', 'create_date', 'published']
    search_fields = ['id', 'author', 'title', 'create_date', 'published']
    form = PostAdminForm

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'create_date']
    list_filter = ['id', 'name', 'create_date']
    search_fields = ['id', 'name', 'create_date']

class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'link']
    list_filter = ['id', 'title', 'link']
    search_fields = ['id']

admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Resources, ResourcesAdmin)