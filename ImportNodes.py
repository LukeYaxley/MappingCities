import overpy

api = overpy.Overpass()
def get_roads(city_name):
# function to fetch all ways and nodes
    try:
        result = api.query(f"""
            [timeout:60][out:json];
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
        return result.ways
    except overpy.exception.OverpassTooManyRequests:
        print("City has too many nodes for city to handle")
    finally:
        return None
