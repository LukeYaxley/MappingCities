import numpy as np
from django.shortcuts import redirect, render
import folium
import overpy
import PlotWays
import ImportNodes

from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'Home.html'

def SearchResultsView(request):
    query = request.GET.get('name')
    Error = "No Error Found"
    try:
        Ways = ImportNodes.get_roads(query)
        Ways_geo,Ways_geo2 = PlotWays.RoadsDataframe(Ways)

        if len(Ways) == 0:
            template_name = "Error.html"
        else:

            mapWayOrigin = Ways[0].getNodes()[0]
            m = folium.Map(location=[mapWayOrigin.lat,mapWayOrigin.lon], zoom_start=13, min_zoom=12, max_zoom=30)
            grid = []
            interval = 0.01 # Equivalent to ~1.1km size
            for lat in np.arange(49, 61, interval):
                grid.append([[lat, -11],[lat, 2]])

            for lon in np.arange(-11, 3, interval):
                grid.append([[49, lon],[60, lon]])

            for g in grid:
                folium.PolyLine(g, color="black", weight=0.5, opacity=0.5).add_to(m)
            m1 = folium.FeatureGroup("Major Road")
            major = folium.vector_layers.PolyLine(Ways_geo, popup='MajorRoad', tooltip='Major_Road',color='red', weight=3).add_to(m1)
            m1.add_to(m)
            m2 = folium.FeatureGroup("Minor Road")
            minor = folium.vector_layers.PolyLine(Ways_geo2, popup='MinorRoad', tooltip='Minor_Road', color='blue',weight=3).add_to(m2)
            m2.add_to(m)
            # folium.PolyLine (Ways_geo, color='red').add_to(m)
            # folium.PolyLine (Ways_geo2, color='blue').add_to(m)
            folium.LayerControl().add_to(m)
            m = m._repr_html_()

            count = 0
            count2 = 0

            for way in Ways:
                if ((way.tags.get("highway")).strip() == 'primary'):
                    count = count + 1
                elif ((way.tags.get("highway")).strip() == 'secondary'):
                    count2 = count2 + 1
            primary_road = "{:.2f}".format((count/(count+count2))*100)
            secondary_road = "{:.2f}".format((count2/(count+count2))*100)

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

