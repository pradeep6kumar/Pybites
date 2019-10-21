import json

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""
import re
import json


def convert_to_json(members=members):

    accumulator = []
    for items in members.splitlines():
        accumulator.append(items)
    lyst = []
    for enums, items in enumerate(accumulator,0):
        if enums == 1:
            keys = re.split(r',|;|\|', items)
        elif enums > 1:
            lyst.append(dict(zip(keys, re.split(r',|;|\|', items))))
    return json.dumps(lyst)

#print(convert_to_json(members))