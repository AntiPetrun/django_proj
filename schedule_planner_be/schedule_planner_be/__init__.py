# # Uncomment to run a scheduled tasks to update classroom availabilities for 90 days period on celery.
# # Comment related code part in models.py starting with.
# # @receiver(post_save, sender=Course)
# # def create_cl_av_for_90_days_period(sender, *args, **kwargs):
#
# from .celery import app as celery_app
#
# __all__ = ('celery_app',)
#
# # try code below if smth goes wrong :-).
# # from __future__ import absolute_import, unicode_literals
# # from .celery import app as celery_app
# #
# # __all__ = ('celery_app',)
