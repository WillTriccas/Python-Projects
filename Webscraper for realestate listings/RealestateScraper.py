import requests
from bs4 import BeautifulSoup

r = requests.get("https://store.nvidia.com/en-gb/geforce/store/gpu/?page=1&limit=9&locale=en-gb&category=GPU&gpu=RTX%203090", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")

body = soup.find_all("div", {"class": "propertyRow"})

#len(body) = 10  as there are 10 results for each page on the website

#print(body[0])

price = body[0].find_all("h4", {"class":"propPrice"})

#Carried the rest of this program on into Jupyter Notebooks


#Below chunk of code was for jupyter notebooks when I couldnt open in
for column_group in item.find_all("div", {"class":"columnGroup"}):
    for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span",{"class":"featureName"})):
        if "LOT SIZE" in feature_group.text.upper():
            print(feature_name.text)
