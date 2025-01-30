# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do dashboard
st.title("Análise de Sentimentos em Tweets")

# Carregar dados
df = pd.read_csv("/Users/joaopedrobrandao/Projetos/analise_sentimentos/dados/results/tweets_com_sentimentos.csv")

# Mostrar tabela com os dados
st.write("### Tabela de Tweets com Sentimentos")
st.write(df)

# Gráfico de distribuição de sentimentos
st.write("### Distribuição de Sentimentos")
contagem_sentimentos = df["Sentimento"].value_counts()
st.bar_chart(contagem_sentimentos)

# Wordcloud (nuvem de palavras)
from wordcloud import WordCloud

st.write("### Nuvem de Palavras")
texto = " ".join(df["Tweet"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)