from django.urls import path
from . import views  # '.' importam tat modulul sub numele 'views'

app_name = 'shop'
urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course_selected/id=<int:course_id>', views.course_selected, name='course_selected'),
    path('category/', views.category, name='category'),
    path('category_selected/id=<int:category_id>', views.category_selected, name='category_selected')

]
