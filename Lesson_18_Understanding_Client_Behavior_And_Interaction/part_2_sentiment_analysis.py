from textblob import TextBlob

class SentimentAnalysis:
    def __init__(self, reviews):
        self.reviews = reviews

    def analyze_sentiment(self):
        analysis_results = []
        
        for review in self.reviews:
            blob = TextBlob(review)
            polarity = blob.sentiment.polarity
            analysis_results.append(polarity)

        return analysis_results

# Assume we have some restaurant reviews
reviews = [
    "The food was amazing and I loved the ambiance!",
    "Long wait times and the staff were rude.",
    "Great service, but the food was just okay."
]

sentiment_analyzer = SentimentAnalysis(reviews)
results = sentiment_analyzer.analyze_sentiment()

for review, score in zip(reviews, results):
    print(f"Review: '{review}' has a sentiment score of: {score}")
