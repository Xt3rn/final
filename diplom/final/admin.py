from django.contrib import admin

from .models import Diplom

@admin.register(Diplom)
class DiplomAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'title', 'supervisor', 'year')
    search_fields = ('student_name', 'title', 'supervisor')
