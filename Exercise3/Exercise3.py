import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Тут ми додаємо вершини та ребра
ports = ["Шанхай", "Сінгапур", "Ціндао"]
ships = ["VLOC", "Балкер", "Pioneering_Spirit"]
G.add_nodes_from(ports + ships)

# Додавання ребер з вагами
edges_with_weights = [("Шанхай", "VLOC", 5), ("Сінгапур", "VLOC", 3), ("Сінгапур", "Балкер", 2),
                      ("Ціндао", "Балкер", 4), ("Ціндао", "Pioneering_Spirit", 7)]
G.add_weighted_edges_from(edges_with_weights)

# Визначення позицій для кращої візуалізації
pos = nx.spring_layout(G)

# Візуалізація графа з вагами
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue",
        font_color="black", font_size=10, edge_color="gray", width=2, edge_cmap=plt.cm.Blues)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Мережа морських сполучень з вагами")
plt.show()


def dijkstra(graph, start):
    # Ініціалізація відстаней до вершин
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0

    # Ініціалізація списку відвіданих вершин
    visited = set()

    # Головний цикл алгоритму
    while len(visited) < len(graph.nodes()):
        # Вибір вершини з найменшою відстанню
        current_node = min(set(distances.keys()) - visited, key=lambda node: distances[node])

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight['weight'] < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight['weight']

        # Позначення поточної вершини як відвіданої
        visited.add(current_node)

    return distances


# Виклик алгоритму Дейкстри для графа G
dijkstra_distances = dijkstra(G, "Шанхай")

# Виведення результатів
print("Dijkstra Distances:")
for node, distance in dijkstra_distances.items():
    print(f"{node}: {distance}")