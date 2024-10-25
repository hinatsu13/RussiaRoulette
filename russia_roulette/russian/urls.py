from django.urls import path

from . import views

urlpatterns = [
    path("reward/", views.RewardView.as_view(), name="reward"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("profile/update/", views.Profile.as_view(), name="profile-update"),
]