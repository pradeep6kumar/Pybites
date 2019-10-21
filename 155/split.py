import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    newitem = []
    for item in re.findall(r'\w+|".+?"', text):
        newitem.append(item.replace('"',''))

    return newitem


#print(split_words_and_quoted_text('Should give "3 elements only"'))