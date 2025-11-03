import spacy

class NlpTopicExtractor:
    def __init__(self, reviews):
        self.reviews = reviews
        self.nlp = spacy.load("en_core_web_sm")

    def extract_topics(self):
        topics = []
        
        for review in self.reviews:
            doc = self.nlp(review)
            topics.extend([chunk.text for chunk in doc.noun_chunks])

        return topics

# Assume we continue with our previous reviews
nlp_topic_extractor = NlpTopicExtractor(reviews)
topics = nlp_topic_extractor.extract_topics()

print(f"Extracted Topics: {set(topics)}")
