# Análise de Conteúdo Web com Nuvem de Palavras

Este projeto realiza a extração de texto de uma página web, aplica técnicas de processamento de linguagem natural e gera uma **nuvem de palavras** para visualização dos termos mais frequentes. A aplicação foi desenvolvida em Python e utiliza como exemplo a página da Wikipedia sobre **Inteligência Artificial**.

## 📁 Repositório

Repositório oficial: [https://github.com/vitor-souza-ime/rp](https://github.com/vitor-souza-ime/rp)

## 📜 Arquivo principal

- [`main.py`](main.py): Script responsável por realizar todas as etapas — scraping, limpeza e visualização textual.

## 🔧 Funcionalidades

- Extração automatizada de texto de uma URL.
- Pré-processamento do texto (remoção de pontuação, stopwords em português e inglês).
- Geração e exibição de nuvem de palavras com `matplotlib`.

## 🧪 Tecnologias utilizadas

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [nltk](https://www.nltk.org/)
- [wordcloud](https://pypi.org/project/wordcloud/)
- [matplotlib](https://matplotlib.org/)

## ▶️ Como executar

1. Clone este repositório:
   
   git clone https://github.com/vitor-souza-ime/rp
   cd rp

3. Instale as dependências:

   pip install -r requirements.txt

4. Execute o script:

   python main.py

O script por padrão acessa a página:
[https://pt.wikipedia.org/wiki/Intelig%C3%AAncia\_artificial](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial)

## 📊 Exemplo de saída

A saída é uma janela gráfica contendo a **nuvem de palavras** representando os termos mais relevantes da página web analisada.

## 📌 Observações

* O script pode ser facilmente adaptado para outras URLs.
* A biblioteca `nltk` pode pedir para baixar os recursos (`stopwords`) na primeira execução.
* O foco deste projeto é demonstrar o uso de **visualização textual como ferramenta exploratória** para conteúdo web.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

