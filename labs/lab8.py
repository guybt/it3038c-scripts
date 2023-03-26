import requests
from bs4 import BeautifulSoup

data = requests.get('https://winning-homebrew.com/make-hooch-at-home.html')
soup = BeautifulSoup(data.content, "html.parser")

title = soup.find('title').text.strip()

print('The title of this article is: ' + title)