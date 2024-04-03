from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CourseResource())  # am inregistarat resurele
api.register(CategoryResource())

# dupa inregistrarea resurselor adresele vor fi urmattoarele
# api/v1/course
# api/v1/categories

# for POST, DELETE add header
# KEY: Authorization
# VALUE: ApiKey andrew:keyforuseerandrew1234567890

urlpatterns = [
    path('', include(api.urls), name='index')
]
