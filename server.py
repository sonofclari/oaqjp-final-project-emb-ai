"""
Flask application for emotion detection using IBM Watson NLP.
Provides a web interface to analyze emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze text and return emotion scores with formatted output.
    
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions
    
    Returns:
        str: Formatted string with emotion scores and dominant emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Build formatted string from the actual keys in emotion_detector's response
    emotions_str = (
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}"
    )
    dominant = response['dominant_emotion']

    # Return plain text string (JS puts responseText directly in the DOM)
    return (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
