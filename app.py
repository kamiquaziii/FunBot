import urllib
import requests
import lxml
from bs4 import BeautifulSoup

baseURL = 'http://www.supremenewyork.com/shop/all/'
categories = ["jackets","shirts","tops_sweaters", "sweatshirts", "pants", "shorts", "t-Shirts", "hats", "bags", "accessories", "skate"]

def categorySelect():
    while True:
        try:
            for i, item in enumerate(categories):
                print(str(i+1) + ': ' + item)

            clothing_type = int(input("Enter number of item\n"))

            if clothing_type < 0 or clothing_type > categories.__len__():
                raise Exception('Invalid category')

        except Exception as err:
            print('An exception happened: ' + str(err))

        else:
            return clothing_type

def pieceSearch(category):
    searchURL = baseURL + categories[category - 1]
    print(searchURL)
    site = requests.get(searchURL)
    siteMap = BeautifulSoup(site.content, "lxml")
    articles = siteMap.select('h1 > a')
    colors = siteMap.select('inner-article > a')

    for title in articles:
        print(title)

pieceSearch(categorySelect())
