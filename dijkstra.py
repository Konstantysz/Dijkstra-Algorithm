import networkx as nx
import matplotlib.pyplot as plt
import random
from queue import PriorityQueue

def dijkstra_algorithm(graph, source):
    d = {v:float('inf') for v in range(len(graph.nodes()))}
    d[source] = 0

    previous_nodes = {v: -1 for v in range(len(graph.nodes()))}

    queue = PriorityQueue()
    queue.put((0, source))

    visited = []

    while not queue.empty():
        (_, current_node) = queue.get()
        visited.append(current_node)

        for (_, neighbour) in graph.edges(current_node):
            if neighbour not in visited:
                old_dist = d[neighbour]
                new_dist = d[current_node] + graph.edges[neighbour, current_node]['weight']
                if old_dist > new_dist:
                    d[neighbour] = d[current_node] + graph.edges[neighbour, current_node]['weight']
                    previous_nodes[neighbour] = current_node
                    queue.put((new_dist, neighbour))

    return d, previous_nodes

def shortest_path_between_nodes(graph, source, target):
    distances, previous_nodes = dijkstra_algorithm(graph, source)

    shortest_path = []
    path_node = target
    while True:
        shortest_path.append(path_node)
        path_node = previous_nodes[path_node]
        if path_node == source:
            shortest_path.append(path_node)
            break

    shortest_path.reverse()

    return distances[target], shortest_path

def draw_path(graph, path):
    color_map = []
    for node in graph:
        if node in path:
            color_map.append('lightgreen')
        else: 
            color_map.append('lightblue') 
    
    edge_colors = []
    for (u, v) in graph.edges():
        if u in path and v in path:
            graph.edges[u, v]['color'] = 'lightgreen'  
        edge_colors.append(graph.edges[u, v]['color'])   

    labels = nx.get_edge_attributes(graph,'weight')
    pos = nx.spring_layout(G, k=1, seed=7)
    nx.draw_networkx(graph, pos, node_color=color_map,  edge_color=edge_colors)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()

if __name__ == '__main__':
    G = nx.fast_gnp_random_graph(6, 0.6, 1)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(5,15)
        G.edges[u, v]['color'] = 'lightblue'
    
    distance, path = shortest_path_between_nodes(G, 2, 1)
    print("Shortest distance from {} to {} is equal {}".format(2, 1, distance))
    draw_path(G, path)