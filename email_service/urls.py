from django.urls import path

from . import views

urlpatterns = [
    path("ping", views.ping.as_view(), name="email/ping"),
    path("send", views.send.as_view(), name="email/send"),
]