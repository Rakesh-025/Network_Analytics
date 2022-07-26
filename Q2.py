import pandas as pd
import numpy as np
import networkx as nx


df1 = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\facebook.csv")
df2 = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\instagram.csv")
df3 = pd.read_csv(r"C:\Users\kaval\OneDrive\Desktop\360digit\datatypes\linkedin.csv")

df1_mtx = np.matrix(df1)
G = nx.from_numpy_matrix(df1_mtx,create_using=nx.DiGraph()) #convertimg into graph
print(G.edges(data=True))
nx.draw(G)

df2_mtx = np.matrix(df2)
G = nx.from_numpy_matrix(df2_mtx,create_using=nx.DiGraph())
print(G.edges(data=True))
nx.draw(G)

df3_mtx = np.matrix(df3)
G = nx.from_numpy_matrix(df3_mtx,create_using=nx.DiGraph())
print(G.edges(data=True))
nx.draw(G)



