from inspect import getsource
import networkx as nx
import matplotlib.pyplot as plt
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from IPython.display import HTML, display,IFrame
from pygments import highlight
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
from operator import attrgetter

#
# prints the source code of a list of functions
# in the jupyter notebook
#

def source(*functions):
    source_code = '\n\n'.join(getsource(fn) for fn in functions)        
    display(HTML(highlight(source_code, PythonLexer(), HtmlFormatter(full=True))))

#
# the following classes are meant for
# drawing graphs and manipulate them on jupyter notebook
#


class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)
    
    def connect(self, A, B, distance = 1):
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)
    
    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)


#
# gets the weight of a certain closed path
# you need to be sure that the nodes are connected
# and there is an edge between each successive node
#

def getWeight(G, path):
    """
    Given a tuple of nodes and the corresponding graph it returns the weight
    of that path assuming it is a closed path
    """
    c = 0
    length = len(path)
    for i in range(length - 1):
        c += G[path[i]][path[i+1]]['weight']
    
    # closing the path
    c += G[path[length - 1]][path[0]]['weight']
    return c

#
# gets the corresponding edges of a graph from a certain path
# once again, you need to be sure that everything is working properly
#

def getEdges(path):
    """
    Given a tuple of nodes from a graph and it returns a list of edges
    """
    length = len(path)
    edges = list()
    for i in range(length-1):
        edges.append((path[i], path[i+1]))
    return edges


#
# you give it colors steps of the animation and the graph 
#

def update_plot(i, data, scat):
    scat.set_array(data[i])
    return scat,

def animate_simple(G, colors):
    numframes = len(colors)
    node_Xs = [float(x) for _, x in G.nodes(data='x')]
    node_Ys = [float(y) for _, y in G.nodes(data='y')]
    fig, ax =  plt.subplots(figsize=(15, 11))
    ax.set_facecolor('w')
    lines = []
    for u, v, data in G.edges(keys=False, data=True):
            if 'geometry' in data:
                xs, ys = data['geometry'].xy
                lines.append(list(zip(xs, ys)))
            else:
                x1 = G.nodes[u]['x']
                y1 = G.nodes[u]['y']
                x2 = G.nodes[v]['x']
                y2 = G.nodes[v]['y']
                line = [(x1, y1), (x2, y2)]
                lines.append(line)

    lc = LineCollection(lines, colors='#999999', linewidths=0.9, alpha=0.3)

    ax.add_collection(lc)
    scat = ax.scatter(node_Xs, node_Ys,c=colors[0], s=30)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ani = animation.FuncAnimation(fig, update_plot, frames=list(range(numframes)),interval=500
                                 ,fargs = (colors, scat))
    return ani