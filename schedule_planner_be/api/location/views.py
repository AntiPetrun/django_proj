from rest_framework import viewsets, status
from rest_framework.response import Response

from api.location.serializers import LocationSerializer
from schedule.models import Location
from api.location.permissions import LocationPermissionsMixin
from rest_framework.permissions import IsAuthenticated


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated & LocationPermissionsMixin]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.save()
