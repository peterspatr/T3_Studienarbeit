def ausgabe():
    for zeile in range(6):
        for spalte in range(7):
            print(str(feld[zeile][spalte]),
                  end=" ")
        print("")
    print("")
    
u = "-"

feld = [[u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u]]
    
werte = [[0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03],
         [0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04],
         [0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05],
         [0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05],
         [0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04],
         [0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03]]

def bewertung():
    wert = 1
    for x in range(6):
        for y in range(7):
            if feld[x][y] == 0:
                wert = wert - werte[x][y]
            if feld[x][y] == 2:
                wert = wert + werte[x][y]
    return wert
    
# Auswertung
# liefert 0, wenn O gewonnen hat
# liefert 2, wenn X gewonnen hat
# liefert 1, wenn es unentschieden ausging
# liefert -1, wenn es noch nicht klar ist.
def auswertung():
    for s in (0, 2):
        for x in (0, 1, 2):
            for y in (0, 1, 2, 3, 4, 5, 6):
                if (feld[x+0][y]==s and feld[x+1][y]==s and
                    feld[x+2][y]==s and feld[x+3][y]==s):
                    return s
        for x in (0, 1, 2, 3, 4, 5):
            for y in (0, 1, 2, 3):
                if (feld[x][y+0]==s and feld[x][y+1]==s and
                    feld[x][y+2]==s and feld[x][y+3]==s):
                    return s
        for x in (0, 1, 2):
            for y in (0, 1, 2, 3):
                if (feld[x+0][y+0]==s and feld[x+1][y+1]==s and
                    feld[x+2][y+2]==s and feld[x+3][y+3]==s):
                    return s
        for x in (3, 4, 5):
            for y in (0, 1, 2, 3):
                if (feld[x-0][y+0]==s and feld[x-1][y+1]==s and
                    feld[x-2][y+2]==s and feld[x-3][y+3]==s):
                    return s
    for y in range(7):
        if feld[0][y]==u:
            return -1
    return 1
    
def zug(y, s):
    for x in (5, 4, 3, 2, 1, 0):
        if feld[x][y] == u:
            feld[x][y] = s
            break

def zugRueckgaengig(y):
    for x in (0, 1, 2, 3, 4, 5):
        if feld[x][y] != u:
            feld[x][y] = u
            break


def max(restTiefe):
    if auswertung() != -1:
        return auswertung()
    if restTiefe == 0:
        return bewertung()
    maximalwert = -999
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 2)
            wert = min(restTiefe - 1)
            if wert > maximalwert:
                maximalwert = wert
            zugRueckgaengig(y)
    return maximalwert

def min(restTiefe):
    if auswertung() != -1:
        return auswertung()
    if restTiefe == 0:
        return bewertung()
    minimalwert = 999
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 0)
            wert = max(restTiefe - 1)
            if wert < minimalwert:
                minimalwert = wert
            zugRueckgaengig(y)
    return minimalwert

minimumY = 0

maximaleTiefe = 5

def minWo():
    global minimumY
    if auswertung() != -1:
        return auswertung()
    minimalwert = 999
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 0)
            wert = max(maximaleTiefe)
            if wert < minimalwert:
                minimalwert = wert
                minimumY = y
            zugRueckgaengig(y)
    return minimalwert
                
def spiele():
    global feld
    global minimumY
    feld = [[u, u, u, u, u, u, u],
            [u, u, u, u, u, u, u],
            [u, u, u, u, u, u, u],
            [u, u, u, u, u, u, u],
            [u, u, u, u, u, u, u],
            [u, u, u, u, u, u, u]]
    while (auswertung() == -1):
        ausgabe()
        y = int(input("Dein y: "))
        if (feld[0][y] != u):
            continue
        zug(y, 2)
        ausgabe()
        if (auswertung() != -1):
            break
        minWo()
        print("Mein y: " + str(minimumY))
        zug(minimumY, 0)
        if auswertung() != -1:
            ausgabe()
            break
