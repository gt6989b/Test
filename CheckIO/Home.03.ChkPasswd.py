def checkio(data):

    return len(data) > 9 and \
           any(x.isupper() for x in data) and \
           any(x.islower() for x in data) and \
           any(x.isdigit() for x in data)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
    assert checkio(u'DHJK87DSKJHWW68D') == False, "7th example"