import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


filepath = "./map.osm"
G = ox.graph_from_xml(filepath, simplify=False)

source_node = 1785148034
target_node = 1785127170

node_letters = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  
for i, node in enumerate(G.nodes()):
    node_letters[node] = letters[i % len(letters)]
print(node_letters)

shortest_path = nx.astar_path(G, source_node, target_node, weight='length')

fig, ax = ox.plot_graph_route(G, shortest_path, route_color='r', route_linewidth=6, node_size=0, bgcolor='black', show=False, close=False)

for node, letter in node_letters.items():
    node_pos = G.nodes[node]['y'], G.nodes[node]['x']  
    ax.text(node_pos[1], node_pos[0], letter, fontsize=6, ha='center', va='center', color='w')

plt.show()


