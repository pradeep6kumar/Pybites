from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

def dict2nt(dict_):
    nt = namedtuple('nt', ' '.join(dict_.keys()))
    #tuple(zip(blog.keys(), blog.values()))
    return nt(*dict_.values())


def nt2json(nt):
    return dict(nt._asdict())