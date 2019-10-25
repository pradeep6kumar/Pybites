from collections import defaultdict
import os
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

# prep data
#holidays_page = os.path.join('D:\\Pbytes', 'us_holidays.php')
#urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, features="html.parser")
    
    newitems = []
    for items in soup.find_all('tr'):
        newitems.append('|'.join(items.get_text().splitlines()).strip())
        #dt = re.findall(r'\d{4}-\d{2}-\d{2}','', items)

    newitems1 = []
    for items in newitems:
        newitems1.append(re.split(r'\|+', items))

    year_event = []

    for items in newitems1[1:]:
        items1 = re.sub(r'(?<=\d{4}-\d{2}-\d{2}).+$','',items[1])
        items2 = re.findall(r'(?<=-)\d+(?=-)', items1)[0]
        year_event.append((items2, items[3]))
    
    dict_ = dict()
    for items in year_event:
        if items[0] in dict_.keys():
            dict_[items[0]] = dict_[items[0]] + [items[1].strip()]
        else:
            dict_[items[0]] = [items[1].strip()]
    return dict_