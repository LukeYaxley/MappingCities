import pandas as pd
import geopandas as gpd


def RoadsDataframe(city_name):
    # roads = get_roads(city_name)
    roads = city_name
    Nodes=[]

    for i in roads:
        for j in i.nodes:
            Nodes.append([float(j.lat),float(j.lon),i.name, i.tags])

    RoadsData = pd.DataFrame(Nodes, columns=["latitude","longitude","roadName","tags"])

    # crs = {'init': 'epsg:4326'}
    # polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])
    return RoadsData

# RoadsDataframe("Dereham")
