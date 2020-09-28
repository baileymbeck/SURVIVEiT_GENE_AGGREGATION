import requests
from bs4 import BeautifulSoup as bs
from csv import writer

r = requests.get('https://expertscape.com/ex/urinary%20bladder%20neoplasms')

soup = bs(r.content, 'html.parser')

# print(soup.prettify())

doctor_column = soup.find('td', attrs={'id': 'expColTD_a'})

print(doctor_column)