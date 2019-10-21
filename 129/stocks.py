import requests
#import json
#import urllib.request as urllib2

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

#j = urllib2.urlopen('https://bit.ly/2MzKAQg')


with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

# your turn:
# print(data)
def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""

    cap = str(cap)
    if cap.lower() == 'n/a':
        cap = 0
    else:
        cap = cap.lstrip('$')
        #print(cap)
        if cap.lower().find('b') >= 0:
            cap = float(cap.lower().replace('b',''))*1000
        elif cap.lower().find('m') >= 0:
            cap = float(cap.lower().replace('m', ''))
        cap = float(cap)
    return cap

#print(_cap_str_to_mln_float('$100.45M'))

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    indus_sum = dict()
    #data1 = _cap_str_to_mln_float('cap')
    for items in data:
        if items['industry'] in indus_sum.keys():
            indus_sum[items['industry']] += _cap_str_to_mln_float(items['cap'])
        else:
            indus_sum[items['industry']] = _cap_str_to_mln_float(items['cap'])
    return round(indus_sum[industry],2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    #data2 = _cap_str_to_mln_float('cap')
    symbol_max = dict()
    for items in data:
        if items['symbol'] in symbol_max.keys():
            symbol_max[items['symbol']] = max(symbol_max[items['symbol']],  _cap_str_to_mln_float(items['cap']))
        else:
            symbol_max[items['symbol']] = _cap_str_to_mln_float(items['cap'])

    value = sorted(symbol_max.items(), key = lambda x:x[1], reverse=True)[0][0]
    #sorted(symbol_max.items(), key = lambda x:x[1])
    return value


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    mydict_sector = dict()

    for item in data:
        if item['sector'] not in 'n/a':
            if item['sector'] in mydict_sector.keys():
                mydict_sector[item['sector']] += 1
            else:
                mydict_sector[item['sector']] = 1

    foutput = sorted(mydict_sector.items(), key = lambda x:x[1], reverse=True)
    return (foutput[0][0], foutput[-1][0])
