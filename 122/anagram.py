def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    nword1 = sorted([item.strip().lower() for item in word1 if item.strip() != ''])
    nword2 = sorted([item.strip().lower() for item in word2 if item.strip() != ''])
    if nword1 == nword2:
        return True
    return False


#print(is_anagram('rail safety', 'fairy fun'))

