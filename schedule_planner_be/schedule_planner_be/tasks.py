# # Uncomment to run a scheduled tasks to update classroom availabilities for 90 days period on celery.
# # Comment related code part in models.py starting with
# # @receiver(post_save, sender=Course)
# # def create_cl_av_for_90_days_period(sender, *args, **kwargs):
#
# from schedule_planner_be.celery import app
# from schedule_planner_be.service import create_cl_av_for_90_days_period
#
#
# @app.task
# def update_cl_av(*args, **kwargs):
#     create_cl_av_for_90_days_period(*args, **kwargs)
