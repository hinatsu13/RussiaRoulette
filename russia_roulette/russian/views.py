from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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

