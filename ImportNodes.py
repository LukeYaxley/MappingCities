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
        for way in result.ways:
            waysoutput.append(Way(way.id,way.nodes,way.tags))
            print("Name: %s" % way.tags.get("name", "n/a"))
            print("  Highway: %s" % way.tags.get("highway", "n/a"))
            print("  Nodes:")
            for node in way.nodes:
                print("    Lat: %f, Lon: %f" % (node.lat, node.lon))

        return waysoutput

