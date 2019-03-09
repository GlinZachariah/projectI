from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('simple', views.simple_upload, name='simple_upload'),
path('working', views.make_result, name='make_result'),
path('dir_view', views.dir_view, name='dir_view'),
]
