from django.http.response import HttpResponse
from rest_framework import viewsets
from Apiaap.models import student
from Apiaap.serializers import studentSerializer

# Create your views here.
def home(request):
    return HttpResponse("<h2>helllo world</h2>we can go to facebook by the <a>http://127.0.0.1:8000/apistudent/</a>") 
# make five models for put get del post but in python we have to make only one it make automaticallly rest four
class StudentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
