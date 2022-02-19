import django
from django.http import HttpResponse
import datetime
import django.middleware.csrf as csrf
from django.shortcuts import redirect
import django.template.loader
from django.views.decorators.csrf import csrf_protect

import ImportNodes


from django.views.generic import TemplateView, ListView

from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'