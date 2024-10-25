from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path('change_pass/', views.ChangePassword.as_view(), name='change_password'),
    path("reward/", views.RewardView.as_view(), name="reward"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("profile/update/", views.Profile.as_view(), name="profile-update"),
]
