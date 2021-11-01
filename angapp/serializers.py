from rest_framework import serializers
from .models import Profile, Projects, Rating

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','user','contact']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        field = '__all__'        