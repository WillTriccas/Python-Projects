import requests
from bs4 import BeautifulSoup

r= requests.get("https://www.3tfinance.co.uk/",
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.text
soup = BeautifulSoup(c, "html.parser")

body = soup.find_all("div", {"class": "dmFooterContainer"})


print(body[0])