from django.http import HttpResponse
import datetime

from django.shortcuts import redirect

import ImportNodes

def home(request):
    html ='<form action="/output/" method="post"> <label for="your_name">Your name: </label> <input id="your_name" type="text" name="your_name" > <input type="submit" value="OK"> </form>'
    return HttpResponse(html)
def output(request):
    now = ImportNodes.get_roads("Norwich")
    listroads = []
    for i in now:
        listroads.append(i.name)
    html = "<html><body> %s.</body></html>" % listroads
    return HttpResponse(html)