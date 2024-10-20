import os

os.chdir("C:/Repository/python_csv")

import requests 

from bs4 import BeautifulSoup

import pandas as pd

html = "https://en.wikipedia.org/wiki/Comma-separated_values"

response = requests.get(html)

soup = BeautifulSoup(response.content, 'html.parser')

response = requests.get(html)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

df = pd.read_html(str(table))[0]

df.to_csv("cars_table_python.csv", index = False)

df_loaded = pd.read_csv('cars_table_python.csv')