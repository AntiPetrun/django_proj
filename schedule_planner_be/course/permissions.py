from django.contrib.auth.mixins import AccessMixin
from django.http import Http404


class LessonPermissionsMixin(AccessMixin):
    def has_permissions(self):
        return self.request.user.role == 'Super Admin'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise PermissionError('Super Admin only can post changes to DB.')
        return super().dispatch(request, *args, **kwargs)


class CommentPermissionsMixin1(AccessMixin):
    def has_permissions(self):
        return self.request.user.role == 'Admin'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise PermissionError('Super Admin only can post changes to DB.')
        return super().dispatch(request, *args, **kwargs)
