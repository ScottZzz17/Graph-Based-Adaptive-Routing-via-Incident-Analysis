# Graph-Based Adaptive Routing & Traffic Incident System

An advanced, end-to-end system designed to integrate live audio transcription, machine learning, and real-time graph optimization to deliver the most efficient travel routes. This project captures local radio updates, transcribes them for incident detection, and dynamically adjusts road network weights to compute optimal routes—all in a fully transparent, modular, and easy-to-understand codebase.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Core Objectives](#core-objectives)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Usage Guidelines](#usage-guidelines)
- [Demonstrative Code](#demonstrative-code)
  - [Audio Capture & Transcription](#audio-capture--transcription)
  - [Incident Analysis & ML Integration](#incident-analysis--ml-integration)
  - [Routing & Visualization](#routing--visualization)
- [Development Roadmap](#development-roadmap)
- [Technical Resources](#technical-resources)
- [Additional Notes](#additional-notes)
- [Contact Information](#contact-information)

---

## Project Overview

This project implements a **dynamic routing system** that leverages local radio broadcasts to detect traffic incidents and adjust travel routes accordingly. The system:

- Captures audio (simulated via a local `.wav` file) and transcribes it to text.
- Analyzes the transcript to detect keywords indicating traffic incidents (e.g., “accident,” “congestion”).
- Uses a machine learning model—with hyperparameter tuning—to map incident severity to a penalty value.
- Updates a road network (modeled as a weighted graph) and calculates the optimal route using Dijkstra’s algorithm.

Every component is fully open-source, with no proprietary or hidden elements.

---

## Core Objectives

- **Audio Capture & Processing:**  
  - Capture local radio broadcasts from an audio file.
  - Transcribe the audio to text using a speech recognition API.

- **Traffic Incident Detection:**  
  - Analyze transcripts to identify key terms that suggest traffic slowdowns or accidents.
  - Assign a severity score based on detected keywords.

- **Machine Learning Integration:**  
  - Employ a Random Forest model with hyperparameter tuning (via GridSearchCV) to predict a penalty value from the severity score.
  - Ensure the ML component is robust yet simple enough for further extension.

- **Dynamic Routing:**  
  - Represent the road network as a weighted graph.
  - Adjust edge weights based on the predicted penalty and compute the optimal route in real time.

---

## Key Features

- **Transparent, Modular Design:**  
  Each component—audio processing, incident detection, ML-based penalty assignment, and routing—is implemented in separate modules for clarity and ease of modification.

- **Adaptive Routing:**  
  The system automatically updates road network weights and recalculates the best route whenever a traffic incident is detected.

- **Advanced Machine Learning:**  
  The integration of hyperparameter tuning ensures that the penalty prediction model is both effective and adaptable to various incident severities.

- **Easy Setup & Use:**  
  With minimal external dependencies and clear module separation, users can quickly set up, run, and experiment with the system.

---

## System Architecture

The project is composed of several interconnected modules:

- **Radio Listener & Speech-to-Text:**  
  Uses the `speech_recognition` library to simulate capturing local radio via a `.wav` file and transcribe the audio using Google's Speech Recognition API.

- **Incident Analysis:**  
  Scans the transcript for traffic-related keywords and creates an incident object that includes a description and a severity score.

- **Machine Learning Module:**  
  A Random Forest regressor (optimized with GridSearchCV) maps the incident severity to a penalty value that is used to adjust the road network.

- **Graph-Based Routing:**  
  Utilizes `networkx` to create a road network graph, update edge weights with the predicted penalty, and compute the optimal route using Dijkstra’s algorithm. Visualization is handled by Matplotlib.

---

## Usage Guidelines

1. **Installation:**  
   Although there is no dedicated `requirements.txt`, you will need to install the following libraries:
   - `speechrecognition`
   - `networkx`
   - `scikit-learn`
   - `matplotlib`
   - `joblib`

   Install them via pip:
   ```bash
   pip install speechrecognition networkx scikit-learn matplotlib joblib
   ```
   
2.	**Audio File Setup:**
  Ensure that an audio file named local_radio.wav is placed in the project directory. This file simulates the local radio broadcast.

3.	**Running the System:**
  Execute the main script:
   ```bash
   python main.py
   ```

4.	**Customization:**
Users are encouraged to modify:
	•	The audio file to test with different radio announcements.
	•	The incident analysis module to add or refine keyword detection.
	•	The ML model parameters and training data for improved penalty prediction.

---

## Demonstrative Code

### Audio Capture & Transcription

This module listens to a local radio audio file and transcribes it into text using a speech recognition API. All implementation details can be found in the `radio_listener.py` and `speech_to_text.py` files.

### Incident Analysis & ML Integration

The system analyzes the transcript for traffic-related keywords, assigns a severity score, and then uses a hyperparameter-tuned Random Forest model to predict a penalty value. The full implementation is provided in the `incident_analysis.py` and `ml_model.py` modules.

### Routing & Visualization

A road network is modeled as a weighted graph, where affected road segments have their weights adjusted based on the predicted penalty. The optimal route is then computed with Dijkstra’s algorithm and visualized using Matplotlib. See the `graph_model.py` and `main.py` files for details.

---

## Development Roadmap

### Current Progress
- **Audio & Transcription:**  
  Reliable transcription from a local `.wav` file.
- **Incident Detection:**  
  Effective detection of key traffic indicators and severity scoring.
- **ML Model:**  
  Successfully integrated Random Forest model with hyperparameter tuning.
- **Routing:**  
  Real-time adjustment of road network weights and optimal route calculation.

### Future Enhancements
- **Live Audio Streaming:**  
  Integrate real-time audio capture using libraries like PyAudio.
- **Enhanced Geospatial Mapping:**  
  Improve incident-to-road mapping by incorporating location data and geocoding.
- **Expanded Network Data:**  
  Use a more detailed, real-world road network for improved routing accuracy.
- **Performance Optimizations:**  
  Explore parallel processing and real-time streaming frameworks for scaling.

---

## Technical Resources

- **Audio Processing:**  
  - SpeechRecognition
- **Machine Learning:**  
  - Scikit-learn  
  - Joblib
- **Graph Modeling & Visualization:**  
  - NetworkX  
  - Matplotlib
- **Python Version:**  
  Python 3.7 or higher is recommended.

---

## Additional Notes

### Challenges Faced & Solutions

- **Speech Recognition Variability:**  
  **Challenge:** Background noise and varying audio quality affected transcription accuracy.  
  **Solution:** Leveraged Google’s robust Speech Recognition API and ensured high-quality audio inputs; further noise reduction techniques can be integrated as needed.

- **Hyperparameter Tuning Complexity:**  
  **Challenge:** A limited dataset made hyperparameter tuning challenging and sometimes led to overfitting.  
  **Solution:** Maintained a small, controlled parameter grid and used cross-validation to ensure reliable model performance. Future work will involve expanding the dataset for more robust tuning.

- **Mapping Incidents to Graph Edges:**  
  **Challenge:** Translating generic traffic alerts into specific road segment adjustments was non-trivial.  
  **Solution:** For demonstration purposes, a fixed edge was chosen for adjustment. In future iterations, integrating geolocation data will allow for precise mapping of incidents to affected road segments.

- **Balancing Simplicity with Functionality:**  
  **Challenge:** Creating a system that is both straightforward to understand and capable of advanced ML integration.  
  **Solution:** The project was modularized into clear components, each with a single responsibility, making it easier to understand, maintain, and extend.

### Open and Transparent Codebase

All code is fully available in this repository. There are no hidden or proprietary components—every detail is shared so that users can learn from, modify, and build upon this project.

---

## Contact Information

For further discussion, collaboration, or a private demonstration of the system’s capabilities, please contact:
- **Email:** szaragoza2@wisc.edu  
- **LinkedIn:** ([https://www.linkedin.com/in/scott-zaragoza-198401329/](https://www.linkedin.com/in/scott-zaragoza-198401329/))
