from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Projects, Profile, Rating
from .serializers import ProfileSerializer, ProjectSerializer, RatingSerializer

# Create your views here.

class Project_objects(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class Project_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer 


class Profile_objects(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class Profile_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
