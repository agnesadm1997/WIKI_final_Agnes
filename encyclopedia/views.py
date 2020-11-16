"""
Views.py
Created by Agnes Admiraal
in Visual Studio Code WSL: Ubuntu-20.04

Views file for wiki project.

It contains the functions needed for the encyclopedia templates
that allow users to interact with the wiki website.
- index: shows entries index list
- title: retrieves entry page 
- search: searches for entry page
- newpage: creates a new entry page
- editpage: edits existing entry page
- randompage: retrieves random entry page

Wiki: http://127.0.0.1:8000/
"""

from django.shortcuts import render                                
from django.http import HttpResponseRedirect
from . import util
import random
import markdown2

def index(request):
    """
    Returns a page with list of all names of encyclopedia entries
    """
  
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    """
    Retrieves an encyclopedia entry page by its title. 
    If no such page exists, the function returns an error.
    """
    page = util.get_entry(title)        
    
    if page == None:                
        
        return render(request, "encyclopedia/error.html", {
            "message": "ERROR: page not found"
        }) 

    return render(request, "encyclopedia/title.html", {
        "entry": markdown2.markdown(page),
        "title": title
    })


def search(request): 
    """
    Shows entry pages of which the search command is in the title.
    If the search matches the title completely, it retrieves
    the page immediatly. 
    Shows error in case no match is found.
    """
    entries = util.list_entries()
    seeking = request.GET.get("q").capitalize()

    if seeking in entries:
        
        return render(request, "encyclopedia/title.html", {
            "entry": markdown2.markdown(util.get_entry(seeking)),
            "title": seeking   
        })   

    matches = list()   

    for entry in entries:
        
        if seeking in entry:
           matches.append(entry)
        
    if matches != []:
        
        return render(request, "encyclopedia/search.html", {
            "finds": matches,
            "search": seeking
        })
                                                        
    return render(request, "encyclopedia/error.html", {
            "message": "ERROR: page does not exist"
        })                


def newpage(request): 
    """
    Saves and returns an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it displays an error.
    """
    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        in_use = util.get_entry(title)
            
        if in_use != None:            
            
            return render(request, "encyclopedia/error.html", {
            "message": "ERROR: page already exists"
        }) 

        util.save_entry(title, content)             
                
        return render(request, "encyclopedia/title.html", {
            "entry": markdown2.markdown(util.get_entry(title)),
            "title": title
        })
            
    return render(request,"encyclopedia/newpage.html")


def editpage(request, title):
    """
    Edits and returns an encyclopedia entries' Markdown content. 
    """
    if request.method == "GET":

        return render(request,"encyclopedia/editpage.html", {
            "title": title,
            "content": util.get_entry(title)
        })
                                                                 
    content = request.POST.get("content")  
    util.save_entry(title, content)
    
    return render(request, "encyclopedia/title.html", {
        "entry": markdown2.markdown(util.get_entry(title)),
        "title": title
    })


def randomchoice(request):
    """
    Returns a random entry page.
    """
    randomtitle = random.choice(util.list_entries())
    randompage = util.get_entry(randomtitle)
    return render(request, "encyclopedia/randomchoice.html", {
          "randompage":  markdown2.markdown(randompage)
    })
    

