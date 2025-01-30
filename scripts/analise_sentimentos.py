# analise_sentimentos.py
import pandas as pd
from textblob import TextBlob

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto.
    :param texto: Texto a ser analisado.
    :return: Polaridade (-1 a 1).
    """
    if isinstance(texto, str):  # Verifica se é uma string
        analise = TextBlob(texto)
        return analise.sentiment.polarity
    else:
        return 0.0  # Retorna neutro se não for texto


def classificar_sentimento(polaridade):
    """
    Classifica o sentimento com base na polaridade.
    :param polaridade: Valor da polaridade.
    :return: Sentimento ("Positivo", "Neutro" ou "Negativo").
    """
    if polaridade > 0:
        return "Positivo"
    elif polaridade == 0:
        return "Neutro"
    else:
        return "Negativo"

# Carregar tweets pré-processados
df = pd.read_csv("/Users/joaopedrobrandao/Projetos/analise_sentimentos/dados/processed/tweets_limpos.csv")

# Verificar valores ausentes ou não-textuais
print("Valores ausentes na coluna 'Tweet':", df["Tweet"].isnull().sum())

# Remover linhas com valores ausentes (opcional)
df = df.dropna(subset=["Tweet"])

# Converter todos os valores para string (caso haja números ou outros tipos)
df["Tweet"] = df["Tweet"].astype(str)

# Analisar sentimentos
df["Polaridade"] = df["Tweet"].apply(analisar_sentimento)
df["Sentimento"] = df["Polaridade"].apply(classificar_sentimento)

# Salvar resultados
df.to_csv("dados/results/tweets_com_sentimentos.csv", index=False)
print("Análise de sentimentos concluída!")