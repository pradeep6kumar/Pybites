from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    maxs = -100
    for item in scores:
        if user_score >= item:
            maxs = max(item, maxs)
    return HONORS.get(maxs)

print(get_belt(0))