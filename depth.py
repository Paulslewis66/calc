import networkx as nx

G = nx.Graph()
G.add_edges_from([(0, 7), (0, 5), (0, 3), (7, 2), (7, 4), (0, 5), (5, 1), (0, 3), (3 , 6)])

dfs = list(nx.dfs_tree(G, source=0))
print(dfs)
