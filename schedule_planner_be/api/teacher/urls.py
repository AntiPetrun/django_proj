from django.urls import path
from . import views

urlpatterns =[
    path('', views.TeacherListView.as_view()),
    path('<int:pk>/edit', views.TeacherUpdateView.as_view()),
    path('<int:pk>/delete', views.TeacherDeleteView.as_view()),
    path('<int:pk>/', views.TeacherDetailsView.as_view()),
    path('new/', views.TeacherCreateView.as_view()),
]