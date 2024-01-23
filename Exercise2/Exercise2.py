import networkx as nx 
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Тут ми додаємо вершини та ребра
ports = ["Шанхай", "Сінгапур", "Ціндао"]
ships = ["VLOC", "Балкер", "Pioneering_Spirit"]
G.add_nodes_from(ports + ships)

# Додавання ребер
G.add_edges_from([("Шанхай", "VLOC"), ("Сінгапур", "VLOC"), ("Сінгапур", "Балкер"), ("Ціндао", "Балкер"), ("Ціндао", "Pioneering_Spirit")])

# Визначення позицій для кращої візуалізації
pos = nx.spring_layout(G)

# Візуалізація графа
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue", font_color="black", font_size=10, edge_color="gray")
plt.title("Мережа морських сполучень")
plt.show()


def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    path = []
    while queue:
        current = queue.pop(0)
        path.append(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return path

# Виклик алгоритмів для графа G
dfs_path = dfs(G, "Шанхай")
bfs_path = bfs(G, "Шанхай")

# Порівняння результатів
print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")