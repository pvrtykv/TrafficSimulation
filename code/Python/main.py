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
    BBox = (df.lon.min(), df.lon.max(), df.lat.min(), df.lat.max())
    map_img = plt.imread('map.png')
    fig, ax = plt.subplots(figsize = (50,30))
    ax.scatter(df.lon, df.lat)
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(map_img, zorder=0, extent=BBox, aspect='equal')
    plt.show()
