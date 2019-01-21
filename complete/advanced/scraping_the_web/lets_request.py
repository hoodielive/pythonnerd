import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.example.com')
print(page.content)
