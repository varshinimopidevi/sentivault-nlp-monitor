from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the local analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # This runs directly on your laptop, no internet needed!
    scores = analyzer.polarity_scores(text)
    
    # Logic to determine label
    if scores['compound'] >= 0.05:
        label = "POSITIVE"
    elif scores['compound'] <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
        
    # Convert score to a percentage (0-100)
    confidence = round(abs(scores['compound']) * 100, 2)
    if confidence == 0: confidence = 50.0 # Neutral fallback
    
    return label, confidence