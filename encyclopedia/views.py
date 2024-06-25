from django.shortcuts import render
from markdown2 import Markdown

from . import util

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/entry.html", {"entry": "Nothing Found"})
    else:
        return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(util.get_entry(entry)), "title": entry
    })

