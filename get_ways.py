# getWays(file) returns the list of Way objects from the "*.osm.xml" file
#
# the Way object has 3 variables/properties:
#    id - the integer with the Way's id
#    tags - the dictionary with the Way's tags (key:value)
#    nodes - the list of Node objects
#
# the Node object has 4 variables/properties
#    id - the integer with the Node's id
#    x - the integer with the Node's latitude
#    y - the integer with the Node's longitude
#    coords - the 2-element list with the Node's coords [Latitude, Longitute]


from xml.dom.minidom import parse

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.coords = [x,y]
    def to_str(self):       #for debug
        return "id: "+self.id+", coords: ["+self.coords[0]+", "+self.coords[1] + "]"

class Way:
    def __init__(self, id, nodes, tags):
        self.id = id
        self.nodes = nodes  #list of Nodes
        self.tags = tags    #dictionary with random info about the way
        self.name = tags.get("name", "n/a")
    def getNodes(self):
        return self.nodes
def getWays(file):
    map = parse(file)
    node_list = []              #list of Node objects
    way_list = []               #list of Way objects
    for xml_node in map.getElementsByTagName("node"):
        attributes=(dict(xml_node.attributes.items()))
        id = attributes["id"]
        x = attributes["lat"]
        y = attributes["lon"]
        node_list.append(Node(id,x,y))

    for xml_way in map.getElementsByTagName("way"):
        way_nodes = []          #list of strings (nodes id's) that the way contains
        way_tags = {}           #dictionary of the way's tags

        attributes=(dict(xml_way.attributes.items()))
        way_id = attributes["id"]
        xml_nodes = xml_way.getElementsByTagName("nd")
        for xml_node in xml_nodes:
            for id in xml_node.attributes.items():
                for node in node_list:
                    if node.id==id[1]:
                        way_nodes.append(node)

        xml_tags = xml_way.getElementsByTagName("tag")
        for tag in xml_tags:
            key = tag.attributes.items()[0][1]
            value = tag.attributes.items()[1][1]
            way_tags[key]=value
        way_list.append(Way(way_id,way_nodes,way_tags))
    return way_list
