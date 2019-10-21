def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    mylist = []
    for items in text:
        if ord(items) > 127:
            mylist.append(items.lower())
    return mylist

