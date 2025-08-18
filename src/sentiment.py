from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text, method='textblob'):
    """
    Analyze the sentiment of the given text.

    Parameters:
        text (str): The input text to analyze.
        method (str): The sentiment analysis method to use ('textblob' or 'vader').

    Returns:
        dict: A dictionary containing the sentiment score and label.
    """
    if method == 'textblob':
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            label = 'Positive'
        elif polarity < 0:
            label = 'Negative'
        else:
            label = 'Neutral'
        return {'score': polarity, 'label': label}

    elif method == 'vader':
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']
        if compound > 0.05:
            label = 'Positive'
        elif compound < -0.05:
            label = 'Negative'
        else:
            label = 'Neutral'
        return {'score': compound, 'label': label}

    else:
        raise ValueError("Invalid method. Choose 'textblob' or 'vader'.")

# Example usage
if __name__ == "__main__":
    sample_text = "I love this product! It's amazing."
    result = analyze_sentiment(sample_text, method='textblob')
    print(f"TextBlob Analysis: {result}")

    result = analyze_sentiment(sample_text, method='vader')
    print(f"VADER Analysis: {result}")
