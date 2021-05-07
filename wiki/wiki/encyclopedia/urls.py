from django.urls import path
from . import util
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/TITLE", views.index, name="index"),
    #go to save Create New Page
    path("wiki/save", views.save, name="save"),
    path("wiki/<str:title>", views.get, name="get"),
    path("wiki/<str:title>", views.error, name="name"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/", views.randomPage, name="random")
    
]

