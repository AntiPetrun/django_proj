# # Uncomment to run a scheduled tasks to update classroom availabilities for 90 days period on celery.
# # Comment related code part in models.py starting with.
# # @receiver(post_save, sender=Course)
# # def create_cl_av_for_90_days_period(sender, *args, **kwargs):
#
# from datetime import date, timedelta
#
# from course.models import ClassroomAvailability
# from schedule.models import Classroom
#
#
# def create_cl_av_for_90_days_period(*args, **kwargs):
#     """"Updates classroom availabilities for 90 days period"""
#     # if not Classroom.objects.all():
#     #     pass
#     # else:
#     classrooms = Classroom.objects.all()
#     for classroom in classrooms:
#         cla_av = ClassroomAvailability.objects.filter(classroom=classroom).values('date')
#         last_cl_av_date_dict = cla_av.latest('date', 'start_time')
#         last_cl_av_date = last_cl_av_date_dict.get('date')
#         date_today = date.today()
#         td = timedelta(days=90)
#         date_in_90_days = date_today + td
#         number_of_days = date_in_90_days - last_cl_av_date
#         number_of_days = number_of_days.days
#         date_list = []
#         for day in range(number_of_days):
#             a_date = (last_cl_av_date + timedelta(days=day)).isoformat()
#             date_list.append(a_date)
#         start_time_range = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
#                             "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
#         del date_list[0]
#         for item in date_list:
#             for start_time_option in start_time_range:
#                 # available from 8 AM to 22 PM
#                 ClassroomAvailability.objects.create(
#                     classroom=classroom,
#                     date=item,
#                     start_time=start_time_option,
#                 )
