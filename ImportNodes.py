import overpy
from get_ways import Way
api = overpy.Overpass()

def get_roads(city_name):
# function to fetch all ways and nodes
        city_name = city_name.split(',')
        if float(city_name[0]) > float(city_name[2]):
                temp = city_name[0]
                city_name[0] = city_name[2]
                city_name[2] = temp
        if float(city_name[1]) < float(city_name[3]):
                temp = city_name[1]
                city_name[1] = city_name[3]
                city_name[1] = temp
        result = api.query(f"""
            [out:json];
        (
        way({city_name[0]},{city_name[1]},{city_name[2]},{city_name[3]})
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
                waysoutput.append(Way(way.id, way.nodes, way.tags))
                print("Name: %s" % way.tags.get("name", "n/a"))
                print("  Highway: %s" % way.tags.get("highway", "n/a"))
                print("  Nodes:")
                for node in way.nodes:
                        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))

        return waysoutput


        return waysoutput

