import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://expertscape.com/ex/urinary%20bladder%20neoplasms')

soup = BeautifulSoup(response.text, 'html.parser')

doctor = soup.find(id='264')

print(doctor)
