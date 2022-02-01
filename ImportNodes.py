import overpy

api = overpy.Overpass()
def get_roads(city_name):
# function to fetch all ways and nodes
    result = api.query(f"""
    [out:json];
    area[name = "{city_name}"];
    way(area) ["highway"];
        (._;>;);
        out body;
        
        """)
    return result.ways
