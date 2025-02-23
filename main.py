# main.py
from radio_listener import listen_to_radio
from speech_to_text import transcribe_audio
from incident_analysis import analyze_transcript
from ml_model import load_ml_model
from graph_model import create_graph, update_edge_weights, find_optimal_route
import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Listen to local radio (using a sample audio file)
    audio = listen_to_radio("local_radio.wav")
    
    # Transcribe the audio to text
    transcript = transcribe_audio(audio)
    print("Transcript from radio:", transcript)
    
    # Analyze the transcript for traffic-related incidents
    incident = analyze_transcript(transcript)
    if incident:
        print("Detected incident:", incident)
    else:
        print("No significant incident detected.")
    
    # Load (or train) the ML model to predict penalty adjustments
    ml_model = load_ml_model()
    
    # Create the road network graph
    G = create_graph()
    
    # Update the graph's edge weights based on the detected incident
    G = update_edge_weights(G, incident, ml_model)
    
    # Compute the optimal route from node "A" to node "D"
    optimal_path = find_optimal_route(G, "A", "D")
    print("Optimal path from A to D:", optimal_path)
    
    # Visualize the road network with updated weights
    pos = nx.get_node_attributes(G, 'pos')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Road Network with Updated Weights based on Radio Incident")
    plt.show()

if __name__ == "__main__":
    main()