"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request
import re
# prep

tempfile = os.path.join('/Users/pradeepkumar/temp', 'dirnames')
#urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile, 'r') as f:
        data = f.read().split('\n')

    lyst = []
    for items in data:
        if re.search(r'(?<=/)(.+),True$', items):
            yield re.findall(r'(?<=/)(.+),True$', items)[0]


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    cntr_user = Counter([item for item in list(gen_files()) if item not in IGNORE]).most_common(1)
    cntr_user = Counter([item for item in list(gen_files()) if item not in IGNORE]).most_common(1)
    print(cntr)
    return Stats(user=cntr[0][0], challenge=cntr[0][1])


print(diehard_pybites())
