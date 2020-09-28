import requests
from bs4 import BeautifulSoup as bs
from csv import writer

# connection to Expertscape site
r = requests.get('https://expertscape.com/ex/urinary%20bladder%20neoplasms')

# initialize beautiful soup 
soup = bs(r.content, 'html.parser')

# below allows easier readability, saving script here for future pages
# print(soup.prettify())

# this is the column name doctor list
doctor_column = soup.find('td', attrs={'id': 'expColTD_a'})

# ToDo 
# find a way to loop through list
# select function
# name
# ranking
# specialty
# 3 locations
# Nice To Haves
# key word search for gene type

print(doctor_column)