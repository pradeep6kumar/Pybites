import os
import urllib.request
from pathlib import Path
import re

#LOG = os.path.join('/tmp', 'safari.logs')
#PY_BOOK, OTHER_BOOK = '🐍', '.'
#urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


LOG = os.path.join('/Users/pradeepkumar/temp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
#urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)

if not Path(LOG).exists():
    urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():

    with open(LOG, 'r') as f:
        data = f.read().split('\n')

    save_enums = []
    for enums, item in enumerate(data,0):
        if re.search('sending to slack', item):
            save_enums.append(enums - 1)

    fitem = []
    for enums, iters in enumerate(data):
        if enums in save_enums:
            if re.search('python', iters, re.IGNORECASE):
                fitem.append((re.findall(r'^\d+-\d+', iters)[0] , PY_BOOK))
            else:
                fitem.append((re.findall(r'^\d+-\d+', iters)[0] , OTHER_BOOK))

    dict_ = dict()
    #print(fitem)
    for k, v in fitem:
        #print(k, v)
        #print(len([k, v]))
        if k not in dict_.keys():
            dict_[k] = [v]
        else:
            dict_[k] = dict_[k] + [v]

    for k, v in dict_.items():
        print(k, ''.join(v), end ='\n')

