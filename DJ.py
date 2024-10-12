import networkx as nx

G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edge("A", "B", weight=2)
G.add_edge("A", "D", weight=8)
G.add_edge("B", "D", weight=5)
G.add_edge("B", "E", weight=6)
G.add_edge("D", "E", weight=3)
G.add_edge("D", "F", weight=2)
G.add_edge("E", "F", weight=1)
G.add_edge("E", "C", weight=9)
G.add_edge("F", "C", weight=3)

path = nx.shortest_path(G, "A", "C", weight="weight")
print(path)