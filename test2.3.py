Brett = [[0,0,0],[0,0,0],[0,0,0]]

zug = 1

faktor = -0.3

def Spielplacebrett(brett, zug):
    print("Du bist am Zug")
    xn = int(input("Spalte angeben(0-2): "))
    yn = int(input("Reihe angeben(0-2): "))
    
    while xn > 2 or yn > 2 or brett[yn][xn] != 0:
        print("Eingabe nicht möglich. Andere Werte wählen!")
        xn = int(input("Spalte angeben (0-2): "))
        yn = int(input("Reihe angeben (0-2): "))

    newbrett = [[0,0,0],[0,0,0],[0,0,0]]
    
    for y in range(3):
        for x in range(3):
            newbrett[y][x] = brett[y][x]
    newbrett[yn][xn] = zug
    return newbrett

def brettdruck(brett):
    print(brett[0])
    print(brett[1])
    print(brett[2])
    print(" ")

def SpielPvE(brett, zug, faktor):
    while count(brett) > 0 and checkwin(brett, zug) == 0:
        if zug == 1:
            brett = Spielplacebrett(brett, 1)
        elif zug == 2:
            print("Computer spielt. Bitte warten")
            brett = brettwahl(brett, 2, faktor)
            
        brettdruck(brett)

        if zug == 1:
            zug = 2
        elif zug == 2:
            zug = 1
        else:
            print("WTF")

    print("Es gewinnt:")
    print(whowin(brett))
    
def SpielEvE(brett, zug, faktor):
    if count(brett) > 0 and checkwin(brett, zug) == 0:
        brett = brettwahl(brett, zug, faktor)
        brettdruck(brett)
    
        if zug == 1:
            newzug = 2
        elif zug == 2:
            newzug = 1
        else:
            print("WTF")
        
        SpielEvE(brett, newzug, faktor)

def SpielEvEa(brett, zug, faktor1, faktor2):
    while count(brett) > 0 and checkwin(brett, zug) == 0:
        if zug == 1:
            print("1 wählt Zug:")
            brett = brettwahl(brett, zug, faktor1)
        if zug == 2:
            print("2 wählt Zug:")
            brett = brettwahl(brett, zug, faktor2)
        brettdruck(brett)

        if zug == 1:
            zug = 2
        elif zug == 2:
            zug = 1
        else:
            print("WTF")
            
    print("Es gewinnt:")
    print(whowin(brett))

def SpielEvEadvancedTest(brett, zug, faktor1, faktor2):
    while count(brett) > 0 and checkwin(brett, zug) == 0:
        if zug == 1:
            brett = brettwahl(brett, zug, faktor1)
        if zug == 2:
            brett = brettwahl(brett, zug, faktor2)

        if zug == 1:
            zug = 2
        elif zug == 2:
            zug = 1
        else:
            print("WTF")
            
    return whowin(brett)

def brettwahl(brett, zug, faktor):
    wertung = -1000000
    wahlbrett = 0

    for m in range(count(brett)):
        b = bewerte(neuesbrett(brett, m, zug), zug, faktor)

        if b > wertung:
            wertung = b
            wahlbrett = m
            
    return neuesbrett(brett, wahlbrett, zug)

def neuesbrett(brett, m, zug):
    newbrett = [[0,0,0],[0,0,0],[0,0,0]]
    for y in range(len(brett)):
        for x in range(len(brett[y])):
            if brett[y][x] == 0:
                m = m - 1
                if m < 0:
                    for yone in range(len(brett)):
                        for xone in range(len(brett[yone])):
                            newbrett[yone][xone] = brett[yone][xone]
                    newbrett[y][x] = zug
                    return newbrett
    
def checkwin(brett, zug):
    for y in range(len(brett)):
        if brett[y][1] == brett[y][0] and brett[y][1] == brett[y][2] and brett[y][1] == zug and brett[y][1] != 0:
            return 1

        if brett[y][1] == brett[y][0] and brett[y][1] == brett[y][2] and brett[y][1] != zug and brett[y][1] != 0:
            return 2

    for x in range(len(brett[0])):
        if brett[1][x] == brett[0][x] and brett[1][x] == brett[2][x] and brett[1][x] == zug and brett[1][x] != 0:
            return 1

        if brett[1][x] == brett[0][x] and brett[1][x] == brett[2][x] and brett[1][x] != zug and brett[1][x] != 0:
            return 2

    if brett[1][1] == brett[0][0] and brett[1][1] == brett[2][2] and brett[1][1] == zug and brett[1][1] != 0:
        return 1

    if brett[1][1] == brett[0][0] and brett[1][1] == brett[2][2] and brett[1][1] != zug and brett[1][1] != 0:
        return 2

    if brett[1][1] == brett[0][2] and brett[1][1] == brett[2][0] and brett[1][1] == zug and brett[1][1] != 0:
        return 1

    if brett[1][1] == brett[0][2] and brett[1][1] == brett[2][0] and brett[1][1] != zug and brett[1][1] != 0:
        return 2

    return 0

def whowin(brett):
    for y in range(len(brett)):
        if brett[y][1] == brett[y][0] and brett[y][1] == brett[y][2] and brett[y][1] != 0:
            return brett[y][1]

    for x in range(len(brett[0])):
        if brett[1][x] == brett[0][x] and brett[1][x] == brett[2][x] and brett[1][x] != 0:
            return brett[1][x]

    if brett[1][1] == brett[0][0] and brett[1][1] == brett[2][2] and brett[1][1] != 0:
        return brett[1][1]

    if brett[1][1] == brett[0][2] and brett[1][1] == brett[2][0] and brett[1][1] != 0:
        return brett[1][1]

    return 0

def wertung(brett, zug):
    if checkwin(brett, zug) == 1:
        return 1
    
    elif checkwin(brett, zug) == 2:
        return -1
    
    else:
        return 0

def count(brett):
    c = 0
    for y in (range(len(brett))):
        for x in range(len(brett[y])):
            if brett[y][x] == 0:
                c = c + 1
    return c

def bewerte(brett, zug, faktor):
    if zug == 1:
        newzug = 2
    elif zug == 2:
        newzug = 1
    else:
        print("WTF")
    
    w = 0
    
    if count(brett) < 1 or checkwin(brett, zug) != 0:
        return wertung(brett, zug)

    else:
        w = wertung(brett, zug)
        for m in range(count(brett)):
            wzwei = bewerte(neuesbrett(brett, m, newzug), newzug, faktor)
            if wzwei is None:
                wzwei = 0
            w = w + (faktor * wzwei)
        return w    
