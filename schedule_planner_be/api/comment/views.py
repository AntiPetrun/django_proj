from rest_framework import viewsets, status
from rest_framework.response import Response

from api.comment.serializers import CommentSerializer
from schedule.models import Comment
from api.comment.permissions import CommentPermissionsMixin, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated & CommentPermissionsMixin]
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.save()

