from django.contrib import admin
from .models import Job, Tag

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'salary_range', 'is_remote')
    list_filter = ('is_remote', 'salary_range')
    search_fields = ('title', 'company_name', 'location')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.site_header = "PythonPH Jobs Board"
