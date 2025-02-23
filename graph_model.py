# graph_model.py
import networkx as nx

def create_graph():
    """
    Create a simple road network graph.
    Nodes represent intersections and edges represent road segments with a base travel time.
    """
    G = nx.Graph()
    # Add nodes (with positions for visualization)
    G.add_node("A", pos=(0, 0))
    G.add_node("B", pos=(1, 2))
    G.add_node("C", pos=(3, 1))
    G.add_node("D", pos=(4, 3))
    
    # Add edges with base weights (travel times)
    G.add_edge("A", "B", weight=2)
    G.add_edge("B", "C", weight=2.5)
    G.add_edge("C", "D", weight=1.5)
    G.add_edge("A", "C", weight=3)
    G.add_edge("B", "D", weight=4)
    return G

def update_edge_weights(G, incident, ml_model):
    """
    Update the graph's edge weights based on the detected traffic incident.
    For demonstration, we assume the incident affects edge ('B', 'C').
    The ML model predicts a penalty based on the incident's severity.
    """
    if incident:
        severity = incident["severity"]
        penalty = ml_model.predict([[severity]])[0]
        if G.has_edge("B", "C"):
            G["B"]["C"]["weight"] += penalty
            print(f"Updated edge ('B','C') weight with penalty {penalty:.2f} based on incident: {incident['description']}")
    return G

def find_optimal_route(G, source, target):
    """
    Compute the shortest path from source to target using Dijkstra's algorithm.
    """
    return nx.shortest_path(G, source=source, target=target, weight="weight")