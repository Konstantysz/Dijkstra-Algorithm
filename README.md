# Dijkstra-Algorithm

This Python script finds and visualizes the shortest path between two nodes in a randomly generated weighted graph using Dijkstra's algorithm.

## Requirements
- `networkx`
- `matplotlib`

You can install them using:
```bash
pip install networkx matplotlib
```
Or create a virtual environment based on a `requirements.txt` file:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## How It Works
1. Generates a random undirected graph with 6 nodes and weighted edges.
2. Finds the shortest path between node 2 and node 1 using Dijkstra's algorithm.
3. Prints the shortest distance and highlights the path on a graph visualization.

## Running the Script
Simply execute the script:
```bash
python dijkstra.py
```

## Output
- The shortest distance from node 2 to node 1.
- A visual representation of the graph with the shortest path highlighted in green.

## Notes
- You can change the source and target nodes by modifying the `shortest_path_between_nodes(G, source, target)` call in the `__main__` block.
