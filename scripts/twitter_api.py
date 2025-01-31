# twitter_api.py
import tweepy

# Insira suas chaves de API do Twitter
API_KEY = "API KEY HERE"
API_SECRET_KEY = "API SECRET KEY HERE"
ACCESS_TOKEN = "TOKEN ACESS HERE"
ACCESS_TOKEN_SECRET = "TOKEN SECRET ACESS HERE"

# Autenticação
client = tweepy.Client(
    bearer_token="TOKEN BEARER HERE",  # Substitua pelo seu Bearer Token
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
