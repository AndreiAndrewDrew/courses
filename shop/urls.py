from django.urls import path
from . import views  # '.' importam tat modulul sub numele 'views'

urlpatterns = [
    path('', views.index, name='index')
]
