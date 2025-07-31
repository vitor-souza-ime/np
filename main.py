import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import string

# Baixar stopwords do NLTK (se necessário)
nltk.download('stopwords')
from nltk.corpus import stopwords

def extrair_texto_da_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Erro se status != 200
        soup = BeautifulSoup(response.text, 'html.parser')
        textos = soup.stripped_strings
        return ' '.join(textos)
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
        return ""

def limpar_texto(texto):
    texto = texto.lower()  # lowercase
    texto = texto.translate(str.maketrans('', '', string.punctuation))  # remove pontuação
    palavras = texto.split()
    stop_words = set(stopwords.words('portuguese') + stopwords.words('english'))
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words and len(palavra) > 2]
    return ' '.join(palavras_filtradas)

def gerar_nuvem_de_palavras(texto_limpo):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_limpo)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Nuvem de Palavras", fontsize=20)
    plt.show()

# URL a ser analisada
url = "https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial"

# Processo completo
texto_extraido = extrair_texto_da_url(url)
texto_limpo = limpar_texto(texto_extraido)
gerar_nuvem_de_palavras(texto_limpo)
