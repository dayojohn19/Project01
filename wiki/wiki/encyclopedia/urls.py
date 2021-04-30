from django.urls import path
from . import util
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/title", views.index, name="index2"),
    #go to save Create New Page
    path("wiki/save", views.save, name="save"),
    path("wiki/get", views.get, name="get"),
    path("wiki/list", views.list, name="list"),
    path("wiki/get", views.get, name="get"),
    path("wiki/<str:name>", views.error, name="error"),
    
]

