import pandas as pd
import networkx as nx 

G = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\flight_hault.csv")

G.columns=["ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude","Altitude","Time","DST","Tz database time"]
G = G.iloc[:100, 1:12] # for better visualization i had taken only 100 samples
G.info()
G.isna().sum()
g = nx.Graph()
g = nx.from_pandas_edgelist(G, source = 'IATA_FAA', target = 'ICAO')

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


