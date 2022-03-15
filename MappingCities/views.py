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
            m = folium.Map(location=[mapWayOrigin.lat,mapWayOrigin.lon], zoom_start=13, min_zoom=12, max_zoom=15)
            
            grid = []
            interval = 0.01 # Equivalent to ~1.1km size
            
            for lat in np.arange(49, 61, interval):
                grid.append([[lat, -11],[lat, 2]])

            for lon in np.arange(-11, 3, interval):
                grid.append([[49, lon],[60, lon]])

            for g in grid:
                folium.PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(m)

            folium.LayerControl().add_to(m)
            m = m._repr_html_()
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

