from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["surname", "name", "specialization", 'start_date', "is_active"]
    ordering = ["-is_active", "-id"]
    search_fields = ["surname"]
    list_filter = ["surname", "specialization", "is_active"]
