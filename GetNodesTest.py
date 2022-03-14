from ImportNodes import get_roads
result = get_roads('test')
for way in result.ways:
    waysoutput.append(Way(way.id, way.nodes, way.tags))
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))