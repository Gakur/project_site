from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/')
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact =   models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Projects(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='projectpics/')
    description = models.TextField(max_length=600, blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)
    designed_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True) 

    def __str__(self):
        return self.url

    @classmethod
    def print_all(cls):
        project = Projects.objects.all().order_by('-id')
        return project

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    post = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'