import requests
from bs4 import BeautifulSoup
import string

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('article')

for article in articles:
    article_type = article.find('span', {'data-test': 'article.type'}).text.strip()

    if article_type == 'News':
        title = article.find('a', {'data-track-action': 'view article'}).text.strip()
        article_link = article.find('a', {'data-track-action': 'view article'})['href']

        article_response = requests.get('https://www.nature.com' + article_link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        article_body = article_soup.find('p', {'class': 'article__teaser'}).text.strip()

        # Remove punctuation and replace spaces with underscores
        title = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')

        # Save the article content to a file
        with open(f'{title}.txt', 'w', encoding='utf-8') as file:
            file.write(article_body)
            print(f'Saved {title}.txt')
