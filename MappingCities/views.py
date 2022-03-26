import numpy as np
from django.shortcuts import redirect, render
import folium
import overpy
import PlotWays
import ImportNodes
from geopy.distance import geodesic

from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'Home.html'

def SearchResultsView(request):
    query = request.GET.get('name')
    Error = "No Error Found"
    m = folium.Map(location=[54.38, -2.7], zoom_start=6.99)
    primary_road = 0.0
    secondary_road = 0.0
    try:
        Ways = ImportNodes.get_roads(query)
        Ways_geo = PlotWays.RoadsDataframe(Ways)

        if len(Ways) == 0:
            template_name = "Error.html"
        else:

            mapWayOrigin = Ways[0].getNodes()[0]
            m = folium.Map(location=[mapWayOrigin.lat,mapWayOrigin.lon], zoom_start=14, min_zoom=9, max_zoom=25)
            grid = []
            interval = 0.01 # Equivalent to ~1.1km size
            for lat in np.arange(49, 61, interval):
                grid.append([[lat, -11],[lat, 2]])

            for lon in np.arange(-11, 3, interval):
                grid.append([[49, lon],[60, lon]])

            for g in grid:
                folium.PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(m)

            m1 = folium.FeatureGroup("Major Road")
            m2 = folium.FeatureGroup("Minor Road")
            temp_lat_list = []
            temp_lon_list = []
            temp_geom_list = []
            major_list = ['motorway_link','trunk_link','motorway','trunk','primary',
                          'secondary','tertiary','primary_link','unclassified']
            minor_list = ['residential','service','footway','cycleway','track','steps','path','unsurfaced','pedestrian','road',
                          'walkway','living_street','bus_guideway','secondary_link','construction','raceway','platform',
                          'residential; ped','minor','byway','tertiary; second','bridleway','pathway','incline']
            major_dist = 0.0
            minor_dist = 0.0

            for way in Ways:
                if ((way.tags.get("highway")).strip() in major_list):
                    for node in way.nodes:
                        temp_lat_list.append(node.lat)
                        temp_lon_list.append(node.lon)
                        temp_geom_list = zip(temp_lat_list, temp_lon_list)
                        major = folium.vector_layers.PolyLine(temp_geom_list, popup='MajorRoad', tooltip=way.name,color='red', weight=5).add_to(m1)

                        coords_1 = [temp_lat_list[0],temp_lon_list[0]]
                        length_m = len(temp_lat_list)
                        coords_2 = [temp_lat_list[length_m-1],temp_lon_list[length_m-1]]

                        major_dist = major_dist + geodesic(coords_1, coords_2).kilometers

                    temp_lat_list = []
                    temp_lon_list = []
                    temp_geom_list = []

                elif ((way.tags.get("highway")).strip() in minor_list):
                    for node in way.nodes:
                        temp_lat_list.append(node.lat)
                        temp_lon_list.append(node.lon)
                        temp_geom_list = zip(temp_lat_list, temp_lon_list)
                        minor = folium.vector_layers.PolyLine(temp_geom_list, popup='MinorRoad', tooltip=way.name,color='Blue', weight=2).add_to(m2)

                        coords_1 = [temp_lat_list[0],temp_lon_list[0]]
                        length_mi = len(temp_lat_list)
                        coords_2 = [temp_lat_list[length_mi-1],temp_lon_list[length_mi-1]]

                        minor_dist = minor_dist + geodesic(coords_1, coords_2).kilometers

                    temp_lat_list = []
                    temp_lon_list = []
                    temp_geom_list = []

            primary_road = "{:.2f}".format((major_dist/(major_dist+minor_dist))*100)
            secondary_road = "{:.2f}".format((minor_dist/(major_dist+minor_dist))*100)

            primary_road = ( "{:.2f}".format((major_dist)) + "km | " + str(primary_road))
            secondary_road = ( "{:.2f}".format((minor_dist)) + "km | " + str(secondary_road))

            m1.add_to(m)
            m2.add_to(m)
            folium.LayerControl().add_to(m)
            m = m._repr_html_()

            template_name = 'search_results.html'
    except overpy.exception.OverpassBadRequest:
        m = False
        Error = "Query did not return any results"
        template_name = "Error.html"
        Ways = None
    except IndexError:
        Error =" Coordinates not entered in correct format"
        template_name = "Error.html"
        Ways = None

    return render(request, template_name, {'Ways': Ways, 'Error':Error, 'my_map': m, 'Primary': primary_road, 'Secondary': secondary_road})
