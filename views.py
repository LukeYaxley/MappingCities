from django.shortcuts import render, redirect
import os
import folium
import geopandas as gpd

# Create your views here.
def home(request):
    m = folium.Map(location=[54.38, -2.7], zoom_start=6.99)

    folium.LayerControl().add_to(m)
    m=m._repr_html_()
    context = {'my_map': m}
    return render(request, 'geoApp/home.html', context)
