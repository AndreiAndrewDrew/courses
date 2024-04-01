from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course  # din mapa curenta din 'models.py' importam variabila 'Course'
from .models import Category


# Create your views here.
def courses(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})
    # return HttpResponse(courses)
    # return HttpResponse(str(course) + '<br>' for course in courses)
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))


def course_selected(request, course_id):
    # Varianta 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/course_selected.html', {'course': course}) # avem acces la variabila 'course'
    # except Course.DoesNotExist:
    #     raise Http404()

    # Varianta 2
    courses = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/course_selected.html', {'course': courses})


def category(request):
    category = Category.objects.all()
    return render(request, 'shop/category.html', {'category': category})


def category_selected(request, category_id):
    # category = Category.objects.get(pk=category_id)
    courses = Course.objects.filter(category_id=category_id)
    return render(request, 'shop/category_selected.html', {'courses': courses})
