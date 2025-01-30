# twitter_api.py
import tweepy

# Insira suas chaves de API do Twitter
API_KEY = "WDqRFvx9cisYrkOy1x8m53j6r"
API_SECRET_KEY = "7Zi3ubEYNsO96Ip4uA7KQ0thrir2talIhnvCwb0YIhI3JoqTrd"
ACCESS_TOKEN = "1559589293093429248-B068mywfh6YcLjtYuAh0mDCrWrNYlk"
ACCESS_TOKEN_SECRET = "etzcCvzeshjfAfjf02N3xlIvCd4jYuWNxskqJkbsnvvNI"

# Autenticação
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAF1pygEAAAAA1c9YOc7ABzSEqvTqi%2Fkno21fefw%3Da31avfYut0vkMAUImJoMSQb4t6ovZ7uzc9WvkbYkqqHCxdlqYD",  # Substitua pelo seu Bearer Token
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def coletar_tweets(query, num_tweets=100):
    """
    Coleta tweets com base em uma query (termo de busca) usando a API v2.
    :param query: Termo de busca (ex: "openai").
    :param num_tweets: Número de tweets a serem coletados.
    :return: Lista de tweets.
    """
    tweets = client.search_recent_tweets(
        query=query,
        max_results=num_tweets,
        tweet_fields=["created_at", "text"]
    )
    return [tweet.text for tweet in tweets.data]