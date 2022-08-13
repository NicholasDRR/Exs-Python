import requests
from bs4 import BeautifulSoup
from rich import print

url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    vote = pergunta.select_one('.s-post-summary--stats-item-number')
    print(f'[red]Data:[/] {data.text} [red]Título:[/] {titulo.text} [red]Votos:[/] {vote.text}', sep='\t')
