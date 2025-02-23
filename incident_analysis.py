# incident_analysis.py

def analyze_transcript(transcript):
    """
    Analyze the radio transcript for indications of traffic slowdowns.
    Returns an incident dict if a significant issue is found.
    """
    transcript_lower = transcript.lower()
    severity = 0
    description = ""
    
    if "accident" in transcript_lower:
        severity = max(severity, 7)
        description = "Accident reported"
    if "congestion" in transcript_lower or "traffic jam" in transcript_lower:
        severity = max(severity, 5)
        description = "Congestion reported"
    if "slow" in transcript_lower:
        severity = max(severity, 4)
        description = "Slow traffic reported"
    if "delay" in transcript_lower:
        severity = max(severity, 3)
        description = "Traffic delay reported"
    
    if severity > 0:
        # Here we simulate a location for the incident; in a real scenario,
        # you might use additional context or geo-tagging.
        incident = {"description": description, "severity": severity, "location": (43.0731, -89.4012)}
        return incident
    else:
        return None