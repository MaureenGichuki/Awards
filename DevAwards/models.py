from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField, ModelForm, widgets
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Project(models.Model):
    """
    Posted projects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to = 'photos/')
    title = models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    url = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    @classmethod
    def get_project_by_user(cls, user):
        project = cls.objects.filter(user=user)
        return project

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_one_project(cls, id):
        project = cls.objects.get(id=id)
        return project

    
    @classmethod
    def search_by_title(self, search_title):
        
        projects = Project.objects.filter(title__icontains=search_title)
        return projects
  

    def __str__(self):
        return self.user.username       


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(blank=True, upload_to = 'profiles/')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile       
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles

class Ratings(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(default=0, validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    userbility = models.IntegerField(default=0,validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    content = models.IntegerField(default=0,validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                     ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rate = models.IntegerField(default=0, validators=[
                                    MaxValueValidator(10),
                                    MinValueValidator(1)
                                  ])
   
    def update(self):
        self.save()

    def save_ratings(self):
        self.save()
        
    def delete_ratings(self):
        self.delete()
        
    @classmethod
    def filter_by_id(cls, id):
        rating = Ratings.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username
