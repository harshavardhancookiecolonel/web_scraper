import requests

from bs4 import BeautifulSoup

def check_articles(url):
    if "articles" not in url:
        return "Invalid page!"

    response = requests.get(url,  headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string
    summary = soup.find('meta', attrs={'name': 'description'})['content']
    return {'title': title, 'description': summary}



url = input()
result = check_articles(url)
print(result)
