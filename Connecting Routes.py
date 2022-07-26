import pandas as pd
import networkx as nx 



G = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\connecting_routes.csv")
# connecting routes=c("flights", " ID", "main Airport”, “main Airport ID", "Destination ","Destination  ID","haults","machinary")
G.columns=["flights","ID","main Airport","main Airport ID","Destination","Destination  ID","haults","machinary","NA"]
G = G.iloc[:500, 1:10]
G.info()

g = nx.Graph()
g = nx.from_pandas_edgelist(G, source = 'main Airport', target = 'Destination')

print(nx.info(g))

 # Degree Centrality
b = nx.degree_centrality(g)  # Degree Centrality
print(b) 

# update the decorator package to 5.0.7 to over come the 'random_state_index is incorrect' error
# pip install decorator==5.0.7

pos = nx.spring_layout(g, k = 0.15)
nx.draw_networkx(g, pos, node_size = 25, node_color = 'blue')

# closeness centrality
closeness = nx.closeness_centrality(g)
print(closeness)

## Betweeness Centrality 
d = nx.betweenness_centrality(g) # Betweeness_Centrality
print(d)

  ## Eigen-Vector Centrality
evg = nx.eigenvector_centrality(g) # Eigen vector centrality
print(evg)

# cluster coefficient
cluster_coeff = nx.clustering(g)
print(cluster_coeff)

# Average clustering
cc = nx.average_clustering(g) 
print(cc)
