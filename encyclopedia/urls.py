from django.urls import path

from . import util

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index),
    path("<str:entry>", views.entry, name="entry")
]
