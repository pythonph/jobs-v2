from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'salary_range', 'is_remote')
    search_fields = ('title', 'company_name', 'location')
