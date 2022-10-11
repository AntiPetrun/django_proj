from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import ScheduleForm, LocationForm, SubwayStationForm, ClassroomForm
from .models import Location, SubwayStation, Schedule, Classroom
from course.models import Course, Comment
from django.contrib.auth.mixins import LoginRequiredMixin

import csv
from django.http import HttpResponse, HttpResponseRedirect

from .permissions import LocationPermissionsMixin


class ScheduleListView(ListView):
    template_name = 'schedule/schedules.html'
    model = Schedule


class ScheduleUpdateView(UpdateView):
    template_name = 'schedule/edit-schedule.html'
    model = Schedule
    form_class = ScheduleForm

    def get_success_url(self):
        return reverse_lazy('schedule-detail', args=(self.object.id,))


class ScheduleDeleteView(DeleteView):
    template_name = 'schedule/delete-schedule.html'
    model = Schedule
    success_url = reverse_lazy('schedules')


class ScheduleDetailView(DetailView):
    template_name = 'schedule/schedule-detail.html'
    model = Schedule


class ScheduleCreateView(CreateView):
    template_name = 'schedule/add-schedule.html'
    form_class = ScheduleForm

    def get_success_url(self):
        return reverse_lazy('schedule-detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['locations'] = Location.objects.all()
        context['reviews'] = Comment.objects.all()
        return context


class LocationListView(LoginRequiredMixin, ListView):
    template_name = 'schedule/locations.html'
    model = Location


class LocationUpdateView(LoginRequiredMixin, LocationPermissionsMixin, UpdateView):
    template_name = 'schedule/edit-location.html'
    model = Location
    form_class = LocationForm

    def get_success_url(self):
        return reverse_lazy('locations')


class LocationDeleteView(LoginRequiredMixin, LocationPermissionsMixin, DeleteView):
    template_name = 'schedule/delete-location.html'
    model = Location
    fields = ['is_active']
    success_url = reverse_lazy('locations')

    def get_queryset(self):
        locations = Location.objects.filter(is_active=True)
        return locations

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class LocationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'schedule/location-detail.html'
    model = Location


class LocationCreateView(LoginRequiredMixin, LocationPermissionsMixin, CreateView):
    template_name = 'schedule/add-location.html'
    form_class = LocationForm

    def get_success_url(self):
        return reverse_lazy('locations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station'] = SubwayStation.objects.all()
        return context


class SubwayStationListView(LoginRequiredMixin, ListView):
    template_name = 'schedule/subways.html'
    model = SubwayStation


class SubwayStationUpdateView(LoginRequiredMixin, LocationPermissionsMixin, UpdateView):
    template_name = 'schedule/edit-subway.html'
    model = SubwayStation
    form_class = SubwayStationForm

    def get_success_url(self):
        return reverse_lazy('subways')


class SubwayStationDeleteView(LoginRequiredMixin, LocationPermissionsMixin, DeleteView):
    template_name = 'schedule/delete-subway.html'
    model = SubwayStation
    fields = ['is_active']
    success_url = reverse_lazy('subways')

    def get_queryset(self):
        subways = SubwayStation.objects.filter(is_active=True)
        return subways

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SubwayStationDetailView(LoginRequiredMixin, DetailView):
    template_name = 'schedule/subway-detail.html'
    model = SubwayStation


class SubwayStationCreateView(LoginRequiredMixin, LocationPermissionsMixin, CreateView):
    template_name = 'schedule/add-subway.html'
    form_class = SubwayStationForm

    def get_success_url(self):
        return reverse_lazy('subways')


class ClassroomListView(LoginRequiredMixin, ListView):
    template_name = 'schedule/classrooms.html'
    model = Classroom


class ClassroomUpdateView(LoginRequiredMixin, LocationPermissionsMixin, UpdateView):
    template_name = 'schedule/edit-classroom.html'
    model = Classroom
    fields = ['classroom', 'location', 'seats_number', 'pc_number', 'is_active']

    def get_success_url(self):
        return reverse_lazy('classrooms')


class ClassroomDeleteView(LoginRequiredMixin, LocationPermissionsMixin, DeleteView):
    template_name = 'schedule/delete-classroom.html'
    model = Classroom
    fields = ['is_active']
    success_url = reverse_lazy('classrooms')

    def get_queryset(self):
        classrooms = Classroom.objects.filter(is_active=True)
        return classrooms

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ClassroomDetailView(LoginRequiredMixin, DetailView):
    template_name = 'schedule/classroom-detail.html'
    model = Classroom


class ClassroomCreateView(LoginRequiredMixin, LocationPermissionsMixin, CreateView):
    template_name = 'schedule/add-classroom.html'
    form_class = ClassroomForm

    def get_success_url(self):
        return reverse_lazy('classrooms')


