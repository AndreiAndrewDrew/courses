from django.shortcuts import render
from django.http import HttpResponse
from .models import Course  # din mapa curenta din 'models.py' importam variabila 'Course'


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses':courses})
    # return HttpResponse(courses)
    # return HttpResponse(str(course) + '<br>' for course in courses)
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))
