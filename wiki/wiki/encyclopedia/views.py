from django.shortcuts import render
from django.http import HttpResponse
from . import util

# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html", {
        "save": util.save_entry()
    })

def get(request):
    return render(request, "encyclopedia/index.html", {
        "get": util.get_entry()
    })
 

def list(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html")

