from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import ImageField
from .models import Projects, Profile, Rating


class ProjectsForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Projects
        fields = '__all__'