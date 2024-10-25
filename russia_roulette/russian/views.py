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

    def get(self, request):
        return render(request, "reward.html")
    
# Profile let go man (in process...)
class Profile(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        history = user.users.event.all()
        return render(request, 'profile.html', {'history': history})
    
class UpdateProfileView(View):
    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'profile_update.html', {'form': form})
    
    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
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
            return redirect('reward')#อย่าลืมเปลี่ยน

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
