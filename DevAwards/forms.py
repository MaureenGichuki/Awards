from django.forms import ModelForm
from django import forms
from . models import *

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image','url']
        widgets= {
            'url':forms.Textarea()
        }

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['design', 'userbility', 'content']
        
    def save(self, commit=True):
        instance = super().save(commit=False)

        