import numpy as np
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
            mapWayOrigin = Ways[0].getNodes()[0]
            m = folium.Map(location=[mapWayOrigin.lat,mapWayOrigin.lon], zoom_start=13)

            folium.LayerControl().add_to(m)
            m = m._repr_html_()
            template_name = 'search_results.html'
    except overpy.exception.OverpassBadRequest:
        Error = "Query did not return any results"
        template_name = "Error.html"
        Ways = None


    return render(request, template_name, {'Ways': Ways, 'Error':Error, 'my_map': m})

