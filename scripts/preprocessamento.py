# preprocessamento.py
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar recursos do NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def limpar_texto(texto):
    """
    Limpa o texto: remove links, caracteres especiais e stopwords.
    :param texto: Texto a ser limpo.
    :return: Texto limpo.
    """
    # Remover links
    texto = re.sub(r"http\S+|www\S+|https\S+", "", texto, flags=re.MULTILINE)
    # Remover menções e hashtags
    texto = re.sub(r"@\w+|#\w+", "", texto)
    # Remover caracteres especiais
    texto = re.sub(r"\W", " ", texto)
    # Remover números
    texto = re.sub(r"\d+", "", texto)
    # Converter para minúsculas
    texto = texto.lower()
    # Remover stopwords
    stop_words = set(stopwords.words("portuguese"))
    palavras = word_tokenize(texto, language='portuguese')  # Especificar o idioma
    texto = " ".join([palavra for palavra in palavras if palavra not in stop_words])
    return texto

def preprocessar_tweets(arquivo_csv):
    """
    Pré-processa os tweets de um arquivo CSV.
    :param arquivo_csv: Caminho do arquivo CSV.
    :return: DataFrame com os tweets pré-processados.
    """
    df = pd.read_csv(arquivo_csv)
    df["Tweet"] = df["Tweet"].apply(limpar_texto)
    return df

# Exemplo de uso
df = preprocessar_tweets("/Users/joaopedrobrandao/Projetos/analise_sentimentos/dados/raw/tweets_brutos.csv")
df.to_csv("dados/processed/tweets_limpos.csv", index=False)
print("Tweets pré-processados e salvos em 'dados/processed/tweets_limpos.csv'.")