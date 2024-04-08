from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

year_1 = doc.find