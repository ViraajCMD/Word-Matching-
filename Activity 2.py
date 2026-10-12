def match_words(words):

    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:

            ctr += 1
            lst.append(word)

    print(f"List of words with the same first and last characters:\n {lst}")
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])

print(f"The number of words having same first and last characters are :\n{count}")