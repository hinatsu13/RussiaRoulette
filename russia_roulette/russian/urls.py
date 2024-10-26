from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("change_pass/", views.ChangePassword.as_view(), name="change_password"),
    path("reward/", views.RewardView.as_view(), name="reward"),
    path("events/", views.EventListView.as_view(), name="event"),
    path("Challenge/", views.ChallengeView.as_view(), name="challenge"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("profile/update/", views.UpdateProfileView.as_view(), name="profile-update"),
    path("events/add/", views.AddEventView.as_view(), name="add-event"),
    path("events/reward/", views.AddRewardView.as_view(), name="add-reward"),
]
