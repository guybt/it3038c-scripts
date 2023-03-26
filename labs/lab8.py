import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.youtube.com/watch?v=hJ_mOKwAm3M')
soup = BeautifulSoup(data.content, "html.parser")

title = soup.find('title').text.strip()

print('The title of this youtube video is: ' + title)