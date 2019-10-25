import csv
from pathlib import Path
from urllib.request import urlretrieve
import re

tmp = Path('/tmp')
#tmp = Path('/Users/pradeepkumar/temp/')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, 'r', encoding='utf-8-sig') as f:
        data = f.read().split('\n')

    fdata = []
    for item in data[1:]:
        if ';' in item:
            k, v = item.split(';')
            if v != 'None':
                fdata.append((k, float(v)))
                #print(fdata)

    fitems =  [re.findall(r'(?<=Bite )\d+', items[0])[0] for items in sorted(fdata, key = lambda x: x[1], reverse=True)][0:N]
    return fitems


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)