# Análise de Sentimentos em Redes Sociais

Este projeto realiza a análise de sentimentos em tweets coletados da API do Twitter (X API). O objetivo é identificar se os tweets têm um sentimento positivo, negativo ou neutro em relação a um tema específico.

---

## 📋 Sobre o Projeto

A análise de sentimentos é uma técnica de processamento de linguagem natural (NLP) que permite entender a opinião das pessoas sobre um assunto. Neste projeto, utilizamos a API do Twitter para coletar tweets, pré-processá-los e aplicar um modelo de análise de sentimentos. Os resultados são visualizados em um dashboard interativo.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (Linguagem de programação)
- **Tweepy** (Coleta de dados da API do Twitter)
- **Pandas** (Manipulação de dados)
- **NLTK** (Pré-processamento de texto)
- **TextBlob** (Análise de sentimentos)
- **Streamlit** (Dashboard interativo)
- **Matplotlib** e **Seaborn** (Visualização de dados)

---

## 📂 Estrutura do Projeto

analise_sentimentos/
│
├── dados/
│ ├── raw/ # Dados brutos (coletados diretamente da API)
│ │ └── tweets_brutos.csv # Tweets coletados
│ ├── processed/ # Dados pré-processados
│ │ └── tweets_limpos.csv # Tweets após limpeza e pré-processamento
│ └── results/ # Resultados finais
│ └── tweets_com_sentimentos.csv # Tweets com análise de sentimentos
│
├── scripts/ # Scripts do projeto
│ ├── twitter_api.py # Configuração da API do Twitter
│ ├── coleta_tweets.py # Script para coletar tweets
│ ├── preprocessamento.py # Script para pré-processar os dados
│ ├── analise_sentimentos.py # Script para análise de sentimentos
│ └── dashboard.py # Script do dashboard interativo
│
├── README.md # Documentação do projeto
└── requirements.txt # Lista de dependências

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

1. **Python 3.8 ou superior** instalado.
2. **Conta de Desenvolvedor do Twitter** com acesso à API.
3. **Chaves de API do Twitter** (API Key, API Secret Key, Access Token, Access Token Secret).

### Passos para Execução

#### 1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise_sentimentos.git
   cd analise_sentimentos
   ```
   #### 2. Instale as dependências:

```bash
pip install -r requirements.txt
```

#### 3. Configure as chaves da API:

Crie um arquivo .env na raiz do projeto e adicione suas chaves:

```
API_KEY=sua_api_key
API_SECRET_KEY=sua_api_secret_key
ACCESS_TOKEN=seu_access_token
ACCESS_TOKEN_SECRET=seu_access_token_secre`
```
#### 4. Execute os scripts na seguinte ordem:

- Coleta de tweets:

```bash
python scripts/coleta_tweets.py
```
- Pré-processamento:

```bash
python scripts/preprocessamento.py
```
- Análise de sentimentos:
```bash
python scripts/analise_sentimentos.py
````

- Dashboard interativo:
```bash
streamlit run scripts/dashboard.py
```
---

## 📊 Resultados
O projeto gera os seguintes resultados:

 #### 1. Tabela de Tweets:

- Uma tabela com os tweets e suas respectivas análises de sentimentos.

#### 2. Distribuição de Sentimentos:

- Um gráfico de barras mostrando a quantidade de tweets positivos, neutros e negativos.

#### 3. Nuvem de Palavras:

- Uma visualização das palavras mais frequentes nos tweets.

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](https://choosealicense.com/licenses/mit/) para mais detalhes.

## ✉️ Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: João Pedro Brandão

Email: [jpedro.brandao@hotmail.com]