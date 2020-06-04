import osmium as osm
import matplotlib.pyplot as plt
import pandas as pd
"""
class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type,
                                   elem.id,
                                   tag.k,
                                   tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")
"""
class NodeHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_nodes = []
    def node(self, n):
        self.osm_nodes.append([n.id, n.location.lat, n.location.lon])


if __name__ == '__main__':
    c = NodeHandler();
    c.apply_file("IVobwodnica.osm")
  #  print(sorted(c.osm_data))
# h = CounterHandler()

    #h.apply_file("IVobwodnica.osm")

    #print("Number of nodes: %d" % h.num_nodes)

    data_colnames = ['id',  'lat', 'lon']
    df_osm = pd.DataFrame(c.osm_nodes, columns=data_colnames)
    print(df_osm)