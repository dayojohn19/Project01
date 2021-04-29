from django.urls import path

from . import views

urlpatterns = [
    path("wiki/title", views.index, name="index"),
    #go to url page error
    path("wiki/save", views.save, name="save"),
    path("wiki/get", views.get, name="get"),
    path("wiki/list", views.list, name="list"),
]
