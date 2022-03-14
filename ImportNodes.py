import overpy
from get_ways import Way
api = overpy.Overpass()

def get_roads(city_name):
# function to fetch all ways and nodes
        result = api.query(f"""
            [out:json];
        area[name ="{city_name}"];
        (
        way(area)
        ['name']
        ['highway']
        ['highway' !~ 'path']
        ['highway' !~ 'steps']
        ['highway' !~ 'motorway']
        ['highway' !~ 'motorway_link']
        ['highway' !~ 'raceway']
        ['highway' !~ 'bridleway']
        ['highway' !~ 'proposed']
        ['highway' !~ 'construction']
        ['highway' !~ 'elevator']
        ['highway' !~ 'bus_guideway']
        ['highway' !~ 'footway']
        ['highway' !~ 'cycleway']
        ['foot' !~ 'no']
        ['access' !~ 'private']
        ['access' !~ 'no'];
        );
        (._;>;);
        out body;
                """)
        waysoutput = []



        return waysoutput

