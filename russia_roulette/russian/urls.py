from django.urls import path

from . import views

urlpatterns = [
    path("reward/", views.RewardView.as_view(), name="reward"),
]