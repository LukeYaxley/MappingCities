from ImportNodes import get_roads
import pandas as pd
import json
import geopandas as gpd
from shapely.geometry import Polygon

def RoadsDataframe(city_name):
    # roads = get_roads(city_name)
    roads = city_name
    Nodes=[]
    lat_list=[]
    lon_list=[]
    lat_list2=[]
    lon_list2=[]
    for i in roads:
        for j in i.nodes:
            Nodes.append([float(j.lon),float(j.lat),i.name, i.tags])
        if (i.tags["highway"]=='primary'):
            lat_list.append(float(j.lat))
            lon_list.append(float(j.lon))
        if (i.tags["highway"]=='secondary'):
            lat_list2.append(float(j.lat))
            lon_list2.append(float(j.lon))

    RoadsData = pd.DataFrame(Nodes, columns=["longitude","latitude","roadName","tags"])
    polygon_geom = zip(lat_list,lon_list)
    polygon_geom2 = zip(lat_list2, lon_list2)

    # crs = {'init': 'epsg:4326'}
    # polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])
    return polygon_geom,polygon_geom2

# RoadsDataframe("Dereham")
