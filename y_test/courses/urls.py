from django.urls import path
from .views import *


urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('<int:pk>/', CourseDetailView.as_view()),
]

