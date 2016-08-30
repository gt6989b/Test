FIRST_TEN = ["zero","one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def wordsUnderTen(number):
    return [FIRST_TEN[number]]

def wordsTenToTwenty(number):
    return [SECOND_TEN[number-10]]

def wordsTwentyToHundred(number):
    ones = number % 10
    tens = number / 10

    words = [OTHER_TENS[tens-2]]
    if ones > 0:
       words += wordsUnderTen(ones)
    return words

def wordsUnderHundred(number):
    if number < 10:
       return wordsUnderTen(number)
    elif number < 20:
       return wordsTenToTwenty(number)
    else:
       return wordsTwentyToHundred(number)

def checkio(number):

    if number < 0 or number > 999:
       words = ['number','outside','range']
    else:
       hundreds = number / 100
       if hundreds:
           words   = wordsUnderTen(hundreds) + ['hundred']
           lowDflt = []
       else:
           words   = []
           lowDflt = [FIRST_TEN[0]]

       tensOnes = number % 100
       words += wordsUnderHundred(tensOnes) if tensOnes else lowDflt

    return ' '.join(words)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(0) == 'zero', "7th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
