from django.urls import path
from . import views

urlpatterns =[
    path('', views.LessonListView.as_view()),
    path('morning/', views.LessonMorningListView.as_view()),
    path('evening/', views.LessonEveningListView.as_view()),
    path('edit/<int:pk>/', views.LessonUpdateView.as_view()),
    path('delete/<int:pk>/', views.LessonDeleteView.as_view()),
    path('<int:pk>/', views.LessonDetailView.as_view()),
    path('new/', views.LessonCreateView.as_view()),
]