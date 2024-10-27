from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import *
from .forms import *

# Create your views here.
class RewardView(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        return render(request, "reward.html", {'event': event})
    
class ChallengeView(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        return render(request, "challenge.html", {'event': event})
    
class EventListView(View):
    def get(self, request):
        event = Event.objects.all()
        return render(request, 'event-list.html', {'event': event})
    
# Profile let go man (success)
class Profile(LoginRequiredMixin, View):
    login_url = '/russian/login/'
    def get(self, request):
        user = request.user
        history = user.users.event.all()
        return render(request, 'profile.html', {'history': history})
    
class UpdateProfileView(LoginRequiredMixin, View):
    login_url = '/russian/login/'
    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'update-profile.html', {'form': form})
    
    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            users = Users.objects.get(user=request.user)
            users.phone_number = form.cleaned_data["phone_number"]
            form.save()
            users.save()
            return redirect('profile') # Redirect back to profile page
        return render(request, 'update-profile.html')

class Register(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request,user)
            return redirect('event')#อย่าลืมเปลี่ยน

        return render(request,'login.html', {"form":form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')#อย่าลืมเปลี่ยน

class ChangePassword(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in
            return redirect('profile')
        else:
            return render(request, 'change_password.html', {'form': form})

class AddEventView(LoginRequiredMixin, View):
    def get(self, request):
        form = EventForm()
        return render(request, 'formevent.html', {'form': form})
    
    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                point_reward = form.cleaned_data['point_reward'],
                admin = request.user
            )
            for i in form.cleaned_data['reward']:
                print(i.id)
                event.reward.add(i)
            event.save()
            return redirect('event')
        
        return render(request, "formevent.html", {"form": form})
    
class AddRewardView(LoginRequiredMixin, View):
    def get(self, request):
        form = RewardForm()
        return render(request, 'formreward.html', {'form': form})
    
    def post(self, request):
        form = RewardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
        
        return render(request, "formreward.html", {"form": form})
    
class EditEventView(LoginRequiredMixin, View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        form = EventForm(instance=event)
        return render(request, 'formevent.html', {'form': form})
    
    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event')
        
        return render(request, "formevent.html", {"form": form})
    
class DeleteEvent(LoginRequiredMixin, View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return redirect('event')