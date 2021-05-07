from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms
from markdown2 import Markdown
markdowner = Markdown()
import random



# Create your views here.
def index(request):
    entries = util.list_entries()
    searched = []
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            for i in entries:
                if item in entries:
                    page = util.get_entry(item)
                    page_converted = markdowner.convert(page)

                    context = {
                        'page': page_converted,
                        'title': item,
                        'form': Search()
                    }
                    return render(request, "encyclopedia/get.html", context)
                if item.lower() in i.lower():
                    searched.append(i)
                    context = {
                        'searched': searched,
                        'form': Search()
                    }
            return render(request, "encyclopedia/result.html", context)
        else:
            return render(request, "encyclopedia/indext.html",{"form":form})
    else:
        return render(request, "encyclopedia/index.html",{
            "entries": util.list_entries(), "form":Search()
        })

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))

class Post(forms.Form):
    title = forms.CharField(label= "Title")
    textarea = forms.CharField(widget=forms.Textarea(), label='')


class Save(forms.Form):
    title = forms.CharField(label="Title"),
    textarea = forms.CharField(widget=forms.Textarea(), label='')

class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')

def edit(request, title):
    if request.method == 'GET':
        page = util.get_entry(title)
        
        context = {
            'form': Search(),
            'edit': Edit(initial={'textarea': page}),
            'title': title
        }

        return render(request, "encyclopedia/edit.html", context)
    else:
        form = Edit(request.POST) 
        if form.is_valid():
            textarea = form.cleaned_data["textarea"]
            util.save_entry(title,textarea)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)

            context = {

                'form': Search(),
                'page': page_converted,
                'title': title
            }

            return render(request, "encyclopedia/get.html", context)

def get(request, title):
    entries = util.list_entries()
    if title in entries:
        page = util.get_entry(title)
        page_converted = markdowner.convert(page)
        
        context = {
            'page': page_converted,
            'title': title,
            'form': Search()
        }
        return render(request, "encyclopedia/get.html", context)
    else:
        return render(request, "encyclopedia/error.html",{'nameoferror':title.capitalize()})


def save(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            textarea = form.cleaned_data["textarea"]
            entries = util.list_entries()
            if  title in entries:
                return render(request, "encyclopedia/exist.html",{
                    "form":Search(),
                    "message": "Entry Already Exist",
                    "this" : title
                    })
            else:
                util.save_entry(title, textarea)
                page = util.get_entry(title)
                page_converted = markdowner.convert(page)

                context = {
                    'form':Search(),
                    'page':page_converted,
                    'title':title
                }

                return render(request, "encyclopedia/get.html", context)
    else:
        return render(request, "encyclopedia/save.html", {
            "form":Search(), "post": Post()})



 

 


def create(request):
    if request.method == "post":
        form = Search(request.POST)
        title = form(request.title)

    return render(request, "encyclopedia/save.html", {
        'created': util.save_entry(title, content)
    })    
     
   

def error(request, name):
    return render(request, "encyclopedia/error.html" , {
        "errorname": name.capitalize()
    })

def randomPage(request):
    if request.method == 'GET':
        entries = util.list_entries()
        num = random.randint(0, len(entries) - 2  )
        page_random = entries[num]
        page = util.get_entry(page_random)
        page_converted = markdowner.convert(page)

        context = {
            'form': Search(),
            'page': page_converted,
            'title': page_random
        }

        return render(request, "encyclopedia/get.html", context)

