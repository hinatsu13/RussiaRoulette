from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from .models import *

class ProfileForm(ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Users.objects.create(user=user)
            customer_group = Group.objects.get(name='Customer')
            user.groups.add(customer_group)
        return user

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'point_reward',
            'reward'
        ]

class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields = [
            'name',
            'description'
        ]
        