import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Тут ми додаємо вершини та початкові ребра
ports = ["Шанхай", "Сінгапур", "Ціндао"]
ships = ["VLOC", "Балкер", "Pioneering_Spirit"]
G.add_nodes_from(ports + ships)
initial_edges = [("Шанхай", "VLOC"), ("Сінгапур", "VLOC"), ("Сінгапур", "Балкер"), ("Ціндао", "Балкер"), ("Ціндао", "Pioneering_Spirit")]
G.add_edges_from(initial_edges)

# Додавання додаткових ребер або вершин
additional_edges = [("Шанхай", "Сінгапур"), ("Сінгапур", "Ціндао")]
G.add_edges_from(additional_edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue", font_color="black", font_size=10, edge_color="gray", connectionstyle="arc3,rad=0.1")
plt.title("Мережа морських сполучень")
plt.show()

# Аналіз основних характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print(f"Ступінь вершин: {dict(G.degree())}")