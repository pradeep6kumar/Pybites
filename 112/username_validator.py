# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    accumulator = []
    for items in social_platforms.splitlines():
        accumulator.append(items.strip())

    #print('|'.join(accumulator))
    newitems = []
    for items in '|'.join(accumulator).strip().split('||'):
        newitems.append(re.sub(r'\s+|Can contain|Min:|Max:|:',r'',items))

    d = dict()
    for items in newitems:
        smedia, min_r, max_r, regex_r = items.split('|')
        d[smedia] = Validator(range(int(min_r), int(max_r)), re.compile(r'^[{}]{}{},{}{}$'.format(regex_r, "{",int(min_r), int(max_r)-1, "}")))

    return d

    #print(newitems)


#print(parse_social_platforms_string())


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    # ...
    if platform.title() in ['Facebook', 'Twitter', 'Reddit']:
        k = parse_social_platforms_string()
        if re.search(k[platform.title()].regex, username):
            return True
        else:
            return False
    else:
        raise ValueError

print(validate_username('Twitter', 'a'*16))