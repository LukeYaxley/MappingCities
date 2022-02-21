
from django.shortcuts import redirect, render

import ImportNodes

from django.views.generic import TemplateView, ListView



class HomePageView(TemplateView):
    template_name = 'Home.html'


def SearchResultsView(request):
    query = request.GET.get('name')
    Ways = ImportNodes.get_roads(query)
    template_name = 'search_results.html'
    return render(request, template_name, {'Ways': Ways})

