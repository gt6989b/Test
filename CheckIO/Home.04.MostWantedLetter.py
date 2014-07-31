from collections import defaultdict

def checkio(text):

    letterCount = defaultdict(lambda : 0)
    for letter in text.lower():
        if letter.islower():
            letterCount[letter] += 1
    maxCount = 0
    for letter, freq in letterCount.iteritems():
        if freq > maxCount:
           maxCount   = freq
           maxLetters = {letter}
        elif freq == maxCount:
           maxLetters.add(letter)

    return min(maxLetters)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
