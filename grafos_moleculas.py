import networkx as nx
import matplotlib.pyplot as plt

# Grafo para a molécula de água (H₂O)
# Átomos: Oxigênio (O), Hidrogênio 1 (H1), Hidrogênio 2 (H2)
G_h2o = nx.Graph()
G_h2o.add_nodes_from(['O', 'H1', 'H2'])
G_h2o.add_edges_from([('O', 'H1'), ('O', 'H2')])
# Cada átomo é um vértice. O oxigênio está conectado a dois hidrogênios formando duas ligações covalentes.

# Visualizar o grafo da água
plt.figure(figsize=(4,4))
pos_h2o = nx.spring_layout(G_h2o)
nx.draw(G_h2o, pos_h2o, with_labels=True, node_color=['red', 'lightblue', 'lightblue'], node_size=1200, font_size=14)
plt.title('Estrutura molecular - Água (H₂O)')
plt.show()

# Grafo para a molécula de dióxido de carbono (CO₂)
# Átomos: Carbono (C), Oxigênio 1 (O1), Oxigênio 2 (O2)
G_co2 = nx.Graph()
G_co2.add_nodes_from(['C', 'O1', 'O2'])
G_co2.add_edges_from([('C','O1'),('C','O2')])
# O carbono está no centro, conectado aos dois oxigênios por ligações covalentes.

# Visualizar o grafo do CO₂
plt.figure(figsize=(4,4))
pos_co2 = nx.spring_layout(G_co2)
nx.draw(G_co2, pos_co2, with_labels=True, node_color=['black', 'red', 'red'], node_size=1200, font_size=14)
plt.title('Estrutura molecular - Dióxido de Carbono (CO₂)')
plt.show()
