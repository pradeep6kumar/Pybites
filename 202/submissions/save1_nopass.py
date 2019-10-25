import csv
from pathlib import Path
from urllib.request import urlretrieve
import re
tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, 'r', encoding = "utf-8-sig") as f:
        data = f.read().split('\n')
    
    newitems = []
    for item in data:
        x = item.split(';')
        #print(x[1])
        if x[1] == 'None':
            x[1] = 0
        #print(x)
        newitems.append(x)
        
    dict_ = dict(newitems[1:])
    #print(dict_.items())
    sdict_ = sorted(dict_.items(), key = lambda x: float(x[1]), reverse=True)
    result = sdict_[0:N]
    out = []
    for item in result:
        out.extend(re.findall(r'(?<=Bite )\d+', item[0]))
        
    return out
    
    
if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)