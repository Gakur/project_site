from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('angapp/projects', views.Project_objects.as_view()),
    path('angapp/<int:pk>/', views.Project_details.as_view()),
    path('angapp/profile', views.Profile_objects.as_view),
    path('api/<int:pk>/', views.Profile_details.as_view)
]
urlpatterns = format_suffix_patterns(urlpatterns)