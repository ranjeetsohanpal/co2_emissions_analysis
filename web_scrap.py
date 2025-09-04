import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'https://worldpopulationreview.com/country-rankings/list-of-countries-by-continent'

response = requests.get(url)

html_doc = response.text

soup = BeautifulSoup(html_doc,'html.parser')

table_body = soup.find('tbody')

rows = soup.select("tbody tr")

data = []

for row in rows:
    cols = row.find_all('td')
    if(len(cols)) >=3 :
        country = cols[1].get_text(strip=True)
        continent = cols[2].get_text(strip=True)
        data.append([country,continent])

df = pd.DataFrame(data,columns=["Country", "Continent"])

df.to_csv("countries_by_continent.csv")