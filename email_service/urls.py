from django.urls import path

from . import views

urlpatterns = [
    path("send", views.send.as_view(), name="send"),
]