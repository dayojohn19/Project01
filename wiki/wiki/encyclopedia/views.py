from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms


# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def get(request):
    return render(request, "encyclopedia/error.html")
 


def list(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html")

def error(request, name):
    return render(request, "encyclopedia/error.html")

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")