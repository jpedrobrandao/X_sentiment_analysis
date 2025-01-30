# coleta_tweets.py
import pandas as pd
from twitter_api import coletar_tweets

# Coletar tweets
query = "openai"  # Termo de busca
tweets = coletar_tweets(query, num_tweets=100)

# Salvar em um DataFrame
df = pd.DataFrame(tweets, columns=["Tweet"])

# Salvar em um arquivo CSV
df.to_csv("dados/raw/tweets_brutos.csv", index=False)
print("Tweets coletados e salvos em 'dados/raw/tweets_brutos.csv'.")