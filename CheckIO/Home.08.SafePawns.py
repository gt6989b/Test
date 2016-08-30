nbrs = {'a':{'b'}, 'b':{'a','c'}, 'c':{'b','d'}, 'd':{'c','e'}, 'e':{'d','f'},
                   'f':{'e','g'}, 'g':{'f','h'}, 'h': {'g'}}

def covers(field):
    col, row = field[0], int(field[1])
    if row == 1:
       return {}

    coverRow = str(row-1)
    return {(nbrCol + coverRow) for nbrCol in nbrs[col]}
       
def safe_pawns(pawns):
    safeCount = 0
    for field in pawns:
        allCovers     = covers(field)
        presentCovers = pawns.intersection(allCovers)
        if presentCovers:
            safeCount += 1
    return safeCount

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
