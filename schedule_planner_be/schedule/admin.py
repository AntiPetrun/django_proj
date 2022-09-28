from django.contrib import admin
from .models import Location, SubwayStation, Classroom, Schedule


admin.site.register(SubwayStation)
admin.site.register(Schedule)
admin.site.register(Location)
# admin.site.register(Availability)
# admin.site.register(AvailabilityOccurrence)
# admin.site.register(ClassroomReservation)
# admin.site.register(TimeSlot)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['id', "classroom", "location", "is_active"]
    ordering = ["-id"]
    search_fields = ["location"]
    list_filter = ["location", "is_active"]


