import osmium as osm
import matplotlib.pyplot as plt
import pandas as pd

class NodeHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_nodes = []
    def node(self, n):
        self.osm_nodes.append([n.id, n.location.lon, n.location.lat])


if __name__ == '__main__':
    c = NodeHandler();
    c.apply_file("IVobwodnica.osm")

    data_colnames = ['id',  'lon', 'lat']
    df = pd.DataFrame(c.osm_nodes, columns=data_colnames)
    print(df)
    df.plot(kind='scatter', x='lon', y='lat', color='blue')
    plt.show()