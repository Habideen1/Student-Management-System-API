from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.permissions import AllowAny


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

def homepage(request):
    return HttpResponse("<h1>Welcome to the Student Management System API</h1>")


