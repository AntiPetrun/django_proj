from django.contrib import admin
from .models import Location, SubwayStation, Classroom, Schedule

admin.site.register(Schedule)
# admin.site.register(Availability)
# admin.site.register(AvailabilityOccurrence)
# admin.site.register(ClassroomReservation)
# admin.site.register(TimeSlot)


@admin.register(SubwayStation)
class SubwayStationAdmin(admin.ModelAdmin):
    list_display = ['station', "is_active"]
    ordering = ["-id"]
    search_fields = ["station"]
    list_filter = ["station", "is_active"]


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['id', "classroom", "location", "is_active"]
    ordering = ["-id"]
    search_fields = ["location"]
    list_filter = ["location", "is_active"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', "city", "street", "building", "is_active"]
    ordering = ["-id"]
    search_fields = ["street", "building"]
    list_filter = ['id', "city", "street", "building", "is_active"]
