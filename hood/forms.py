from django.db.models import fields
from .models import *
from django.forms import ModelForm
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo','contact','location','neighborhood')

class HoodForm(forms.ModelForm):
    class Meta:
        model=NeighborHood
        fields = ['photo','name','content','location', 'health_cell','police_hotline']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields=['name','photo','email','description','location','neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content','location','neighborhood']