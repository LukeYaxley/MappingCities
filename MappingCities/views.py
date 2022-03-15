import overpy
from django.shortcuts import redirect, render
import folium
import geopandas as gpd
import pandas as pd
import overpy
import matplotlib.pyplot as plt


import ImportNodes

from django.views.generic import TemplateView, ListView



class HomePageView(TemplateView):
    template_name = 'Home.html'

def SearchResultsView(request):
    query = request.GET.get('name')
    Error = "No Error Found"
    try:
        Ways = ImportNodes.get_roads(query)
        if len(Ways) == 0:
            template_name = "Error.html"
        else:
            #m = folium.Map(location=[54.38, -2.7], zoom_start=6.99)
            #folium.LayerControl().add_to(m)
            #m = m._repr_html_()
            template_name = 'search_results.html'
    except overpy.exception.OverpassBadRequest:
        Error = "Query did not return any results"
        template_name = "Error.html"
        Ways = None
    except IndexError:
        Error =" Coordinates not entered in correct format"
        template_name = "Error.html"
        Ways = None




    return render(request, template_name, {'Ways': Ways, 'Error':Error})

