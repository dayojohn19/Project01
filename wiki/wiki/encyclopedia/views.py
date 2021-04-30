from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms
import markdown

# Create your views here.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def get(request):
    return render(request, "encyclopedia/get.html", {
        "get": util.get_entry(),
    })
 


def list(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html",{'price':200} )

class TitleForm(forms.Form):
    title = forms.CharField(max_length=100, label="New Title")   
 

def create(request):
    if request.method == "POST":
        form = TitleForm(request.POST)
        

    return render(request, "encyclopedia/save.html", {
        "created": ContactForm()
    })    
     
   

def error(request, name):
    return render(request, "encyclopedia/error.html" , {
        "errorname": name.capitalize()
    })



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")



