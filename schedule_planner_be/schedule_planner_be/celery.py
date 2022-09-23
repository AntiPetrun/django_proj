# # Uncomment to run a scheduled tasks to update classroom availabilities for 90 days period on celery.
# # Comment related code part in models.py starting with.
# # @receiver(post_save, sender=Course)
# # def create_cl_av_for_90_days_period(sender, *args, **kwargs):
# import os
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule_planner_be.settings')
#
# app = Celery('schedule_planner_be')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#
# app.conf.beat_schedule = {
#     'update_cl_av_daily': {'task': 'schedule_planner_be.tasks.update_cl_av',
#                            'schedule': crontab(minute='*/1440')}
# }
