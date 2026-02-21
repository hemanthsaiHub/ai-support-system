def analyze_sentiment(text: str):
    text = text.lower()
    if any(w in text for w in ["worst", "angry", "refund", "hate"]):
        return "angry"
    if any(w in text for w in ["thanks", "great", "good"]):
        return "happy"
    return "neutral"


def categorize_ticket(text: str):
    text = text.lower()
    if any(w in text for w in ["payment", "refund", "bill"]):
        return "billing"
    if any(w in text for w in ["error", "bug", "login"]):
        return "technical"
    return "general"


def generate_ai_reply(sentiment, category):
    if sentiment == "angry":
        return "We’re sorry for the inconvenience. Our team is working on it."
    if category == "billing":
        return "Our billing team will contact you shortly."
    if category == "technical":
        return "Our technical team is investigating this issue."
    return "Thanks for contacting support."