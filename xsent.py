import textblob
from ntscraper import Nitter

def analyze_sentiment(query, mode, number):
    nitter = Nitter()

    while True:
        try:
            tweets_data = nitter.get_tweets(query, mode=mode, number=number)
            tweets = tweets_data["tweets"]
            break
        except Exception as e:
            print(f"Fetching error: {e}. Retrying...")

    for tweet in tweets:
        try:
            text = tweet.get('text', '')
            if not text:
                continue

            date = tweet.get("date")
            link = tweet.get("link")
            analysis = textblob.TextBlob(text)
            sentiment = analysis.sentiment.polarity

            print(f"Tweet: {text}")
            print(f"Date: {date}")
            print(f"Link: {link}")
            print(f"Sentiment: {sentiment:.2f}")
            if sentiment >= 0.05:
                print("Positive")
            elif sentiment <= -0.05:
                print("Negative")
            else:
                print("Neutral")
            print("----------------------------------")
        except Exception as e:
            print(f"Error processing tweet: {e}")

if __name__ == '__main__':
    query = "from:elonmusk"
    mode = 'term'
    number = 100
    analyze_sentiment(query, mode, number)
