from ImportNodes import get_roads
import pandas as pd
from matplotlib import pyplot as plt

def RoadsDataframe(city_name):
    roads = get_roads(city_name)
    Nodes=[]
    for i in roads:
        for j in i.nodes:
            Nodes.append([float(j.lon),float(j.lat),i.name])


    RoadsData = pd.DataFrame(Nodes, columns=["longitude","latitude","roadName"])
    print(RoadsData)

RoadsDataframe("Dereham")