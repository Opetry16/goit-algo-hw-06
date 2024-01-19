import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа
G = nx.Graph()

# Тут ми додаємо вершини та ребра
ports = ["Шанхай", "Сінгапур", "Ціндао"]
ships = ["VLOC", "Балкер", "Pioneering_Spirit"]
G.add_nodes_from(ports + ships)

# Додавання ребер та їх ваг
G.add_weighted_edges_from([("Шанхай", "VLOC", 10), ("Сінгапур", "VLOC", 8),
                            ("Сінгапур", "Балкер", 5), ("Ціндао", "Балкер", 7),
                            ("Ціндао", "Pioneering_Spirit", 12)])

# Визначення позицій для кращої візуалізації
pos = nx.spring_layout(G)

# Візуалізація графа
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=700, node_color="skyblue", font_color="black", font_size=10, edge_color="gray", connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})

plt.title("Мережа морських сполучень з вагами")
plt.show()

def dijkstra(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes()}
    
    # Пріоритетна черга для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Перегляд сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight["weight"]
            
            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Виклик алгоритму Дейкстри для кожної вершини
all_shortest_paths = {}

for source in G.nodes():
    distances, predecessors = dijkstra(G, source)
    all_shortest_paths[source] = {"distances": distances, "predecessors": predecessors}

# Виведення результатів
for source, result in all_shortest_paths.items():
    print(f"\nНайкоротші шляхи з {source}:")
    for target, distance in result["distances"].items():
        path = [target]
        while result["predecessors"][target] is not None:
            target = result["predecessors"][target]
            path.insert(0, target)
        print(f"{path}: {distance}")
