def sort_words(s):
    #1st approach
    list_words = s.split(" ")
    list_words.sort(key=str.lower)
    #2d approach
    #list_words = sorted(s.split(), key=str.casefold)
    return " ".join(list_words)

print(sort_words("banana apple ORANGE cherry"))  # apple banana cherry ORANGE
print(sort_words("string of words"))  # of string words