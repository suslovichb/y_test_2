from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course
from django_filters.rest_framework import DjangoFilterBackend


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
