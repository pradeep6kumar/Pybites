from collections import namedtuple
import re

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soups = Soup(CONTENT, features='html.parser')
    #print(soups.prettify())

    title = soups.find('div', class_= 'dotd-title')
    ftitle = title.h2.text.strip()

    #description = soups.find_all('li')
    description = soups.find('div', class_ = 'dotd-main-book-summary float-left')
    description = re.sub(r'\t+','', description.text)
    description = re.sub(r'\n+',r'\n', description).split('\n')
    desc = description[3]

    #for item in description:
    #    print(item.text.strip())


    image = soups.find('img', class_= 'bookimage imagecache imagecache-dotd_main_image')
    fimage = image['src']

    link = soups.find('div', class_ = 'dotd-main-book-image float-left')
    flink = link.a['href']

    return  Book(ftitle, desc, fimage, flink)

#print(get_book())