# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 22:03:00 2026

@author: i5
"""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Створюємо граф
G = nx.DiGraph()

# Додаємо ребра з пропускною здатністю
edges = [
    ("Terminal 1", "Warehouse 1", 25),
    ("Terminal 1", "Warehouse 2", 20),
    ("Terminal 1", "Warehouse 3", 15),

    ("Terminal 2", "Warehouse 3", 15),
    ("Terminal 2", "Warehouse 4", 30),
    ("Terminal 2", "Warehouse 2", 10),

    ("Warehouse 1", "Store 1", 15),
    ("Warehouse 1", "Store 2", 10),
    ("Warehouse 1", "Store 3", 20),

    ("Warehouse 2", "Store 4", 15),
    ("Warehouse 2", "Store 5", 10),
    ("Warehouse 2", "Store 6", 25),

    ("Warehouse 3", "Store 7", 20),
    ("Warehouse 3", "Store 8", 15),
    ("Warehouse 3", "Store 9", 10),

    ("Warehouse 4", "Store 10", 20),
    ("Warehouse 4", "Store 11", 10),
    ("Warehouse 4", "Store 12", 15),
    ("Warehouse 4", "Store 13", 5),
    ("Warehouse 4", "Store 14", 10),
    
    ("Source", "Terminal 1", 1000),   # достаточно большое число
    ("Source", "Terminal 2", 1000),
    ("Store 1", "Sink", 1000),
    ("Store 2", "Sink", 1000),
    ("Store 3", "Sink", 1000),
    ("Store 4", "Sink", 1000),
    ("Store 5", "Sink", 1000),
    ("Store 6", "Sink", 1000),
    ("Store 7", "Sink", 1000),
    ("Store 8", "Sink", 1000),
    ("Store 9", "Sink", 1000),
    ("Store 10", "Sink", 1000),
    ("Store 11", "Sink", 1000),
    ("Store 12", "Sink", 1000),
    ("Store 13", "Sink", 1000),
    ("Store 14", "Sink", 1000),
]


# Додаємо всі ребра до графа
G.add_weighted_edges_from(edges)

# Позиції для малювання графа

pos = {
    # ---------- верхний ряд: магазины 1–6 ----------
    "Store 1":  (0, 4),
    "Store 2":  (1, 4),
    "Store 3":  (2, 4),
    "Store 4":  (3, 4),
    "Store 5":  (4, 4),
    "Store 6":  (5, 4),

    # ---------- средний уровень ----------
    # Warehouses
    "Warehouse 1": (2, 3),
    "Warehouse 2": (4, 3),
    # Terminals
    "Terminal 1": (1, 2),
    "Terminal 2": (5, 2),


    "Warehouse 3": (2, 1),
    "Warehouse 4": (4, 1),

    # ---------- нижний ряд: магазины 7–14 ----------
    "Store 7":  (0, 0),
    "Store 8":  (1, 0),
    "Store 9":  (2, 0),
    "Store 10": (3, 0),
    "Store 11": (4, 0),
    "Store 12": (5, 0),
    "Store 13": (6, 0),
    "Store 14": (7, 0),
    
    "Source": (0,3),
    "Sink":(7,2)
}



# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображаємо граф
plt.show()




nodes = [
    "Source","Sink",
    "Store 1", "Store 2", "Store 3",
    "Store 4", "Store 5", "Store 6",
    "Terminal 1", "Terminal 2",
    "Warehouse 1", "Warehouse 2",
    "Warehouse 3", "Warehouse 4",
    "Store 7", "Store 8", "Store 9",
    "Store 10", "Store 11", "Store 12",
    "Store 13", "Store 14",
    
]

node_index = {node: i for i, node in enumerate(nodes)}

n = len(nodes)
capacity_matrix = [[0]*n for _ in range(n)]

for u, v, cap in edges:
    capacity_matrix[node_index[u]][node_index[v]] = cap
    
    
    
from collections import deque

# Функція для пошуку збільшуючого шляху (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()
        
        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if not visited[neighbor] and capacity_matrix[current_node][neighbor] - flow_matrix[current_node][neighbor] > 0:
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    
    return False

# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [[0] * num_nodes for _ in range(num_nodes)]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float('Inf')
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(path_flow, capacity_matrix[previous_node][current_node] - flow_matrix[previous_node][current_node])
            current_node = previous_node
        
        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node
        
        # Збільшуємо максимальний потік
        max_flow += path_flow

    return max_flow , flow_matrix


original_capacity = np.array(capacity_matrix)   # <-- ДО edmonds_karp(...)
max_flow , flow_matrix=edmonds_karp(capacity_matrix,node_index['Source'], node_index['Sink'])
print(f"Максимальний потік: {max_flow}")
    

edges_with_flow = []

for u, v, cap in edges:
    ui, vi = node_index[u], node_index[v]
    actual_flow = flow_matrix[ui][vi]  # фактический поток по ребру

    edges_with_flow.append((u, v, actual_flow))
    
G.add_weighted_edges_from(edges_with_flow)    
# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображаємо граф
plt.show()

# ================================
# Группы узлов (без изменений)
# ================================

stores = [
    "Store 1", "Store 2", "Store 3",
    "Store 4", "Store 5", "Store 6",
    "Store 7", "Store 8", "Store 9",
    "Store 10", "Store 11", "Store 12",
    "Store 13", "Store 14",
]

terminals = ["Terminal 1", "Terminal 2"]

warehouses = [
    "Warehouse 1", "Warehouse 2",
    "Warehouse 3", "Warehouse 4",
]

# ================================
# Вспомогательная функция: фактический поток
# ================================



edges = []

n = len(nodes)

for i in range(n):
    for j in range(n):
        cap = original_capacity[i][j]
        flow = flow_matrix[i][j]

        if cap > 0 or flow > 0:
            edges.append({
                "from": nodes[i],
                "to": nodes[j],
                "original_capacity": cap,
                "actual_flow": flow,
                "utilization_%": (flow / cap * 100) if cap > 0 else 0
            })

df_edges = pd.DataFrame(edges)




df_terminals = (
    df_edges[df_edges["from"].isin(terminals)]
    .groupby("from")
    .agg(
        total_flow=("actual_flow", "sum"),
        total_capacity=("original_capacity", "sum")
    )
    .reset_index()
)

df_terminals["utilization_%"] = (
    df_terminals["total_flow"] / df_terminals["total_capacity"] * 100
).fillna(0)

df_terminals = df_terminals.rename(columns={
    "from": "Термінал",
    "total_flow": "Сумарний потік",
    "total_capacity": "Сумарна пропускна здатність"
})

print("\nПотоки по терміналах:")
print(df_terminals)

df_stores = (
    df_edges[df_edges["to"].isin(stores)]
    .groupby("to")
    .agg(
        total_flow=("actual_flow", "sum"),
        total_capacity=("original_capacity", "sum")
    )
    .reset_index()
)

df_stores["utilization_%"] = (
    df_stores["total_flow"] / df_stores["total_capacity"] * 100
).fillna(0)

df_stores = df_stores.rename(columns={
    "to": "Магазин",
    "total_flow": "Отриманий потік",
    "total_capacity": "Сумарна пропускна здатність"
})

print("\nПотоки по магазинах:")
print(df_stores)



df_edges_filtered = (
    df_edges[
        (~df_edges["from"].isin(["Source", "Sink"])) &
        (~df_edges["to"].isin(["Source", "Sink"]))
    ]
    .sort_values("utilization_%", ascending=False)
    .reset_index(drop=True)
)

print(df_edges_filtered)



    


