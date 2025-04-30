u = "-"
spieler_zeichen = {0: "O", 2: "X"}

feld = [[u for _ in range(7)] for _ in range(6)]

werte = [[0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03],
         [0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04],
         [0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05],
         [0.05, 0.08, 0.11, 0.13, 0.11, 0.08, 0.05],
         [0.04, 0.06, 0.08, 0.10, 0.08, 0.06, 0.04],
         [0.03, 0.04, 0.05, 0.07, 0.05, 0.04, 0.03]]

def ausgabe():
    for zeile in feld:
        for zelle in zeile:
            if zelle == 0 or zelle == 2:
                print(spieler_zeichen[zelle], end=" ")
            else:
                print(u, end=" ")
        print()
    print("0 1 2 3 4 5 6\n")

def bewertung():
    wert = 1
    for x in range(6):
        for y in range(7):
            if feld[x][y] == 0:
                wert -= werte[x][y]
            elif feld[x][y] == 2:
                wert += werte[x][y]
    return wert

def auswertung():
    for s in (0, 2):
        for x in range(3):
            for y in range(7):
                if all(feld[x+i][y] == s for i in range(4)):
                    return s
        for x in range(6):
            for y in range(4):
                if all(feld[x][y+i] == s for i in range(4)):
                    return s
        for x in range(3):
            for y in range(4):
                if all(feld[x+i][y+i] == s for i in range(4)):
                    return s
        for x in range(3, 6):
            for y in range(4):
                if all(feld[x-i][y+i] == s for i in range(4)):
                    return s
    if all(feld[0][y] != u for y in range(7)):
        return 1  # Unentschieden
    return -1

def zug(y, s):
    for x in reversed(range(6)):
        if feld[x][y] == u:
            feld[x][y] = s
            break

def zugRueckgaengig(y):
    for x in range(6):
        if feld[x][y] != u:
            feld[x][y] = u
            break

def maxFunktion(tiefe):
    ergebnis = auswertung()
    if ergebnis != -1:
        return ergebnis
    if tiefe == 0:
        return bewertung()
    maximalwert = -999
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 2)
            wert = minFunktion(tiefe - 1)
            maximalwert = max(maximalwert, wert)
            zugRueckgaengig(y)
    return maximalwert

def minFunktion(tiefe):
    ergebnis = auswertung()
    if ergebnis != -1:
        return ergebnis
    if tiefe == 0:
        return bewertung()
    minimalwert = 999
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 0)
            wert = maxFunktion(tiefe - 1)
            minimalwert = min(minimalwert, wert)
            zugRueckgaengig(y)
    return minimalwert

def besterZug():
    minimalwert = 999
    best_y = 0
    for y in range(7):
        if feld[0][y] == u:
            zug(y, 0)
            wert = maxFunktion(4)
            zugRueckgaengig(y)
            if wert < minimalwert:
                minimalwert = wert
                best_y = y
    return best_y

def spiele():
    global feld
    feld = [[u for _ in range(7)] for _ in range(6)]
    print("Du spielst 'X'. Ich spiele 'O'.")
    ausgabe()
    while auswertung() == -1:
        # Spielereingabe
        while True:
            try:
                y = int(input("Wähle eine Spalte (0-6): "))
                if 0 <= y <= 6 and feld[0][y] == u:
                    break
                else:
                    print("Ungültige Eingabe oder Spalte voll!")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
        zug(y, 2)
        ausgabe()
        if auswertung() != -1:
            break

        # Computerzug
        print("Ich denke nach...")
        computer_zug = besterZug()
        zug(computer_zug, 0)
        print(f"Ich wähle Spalte {computer_zug}")
        ausgabe()

    gewinner = auswertung()
    if gewinner == 2:
        print("Du hast gewonnen! 🎉")
    elif gewinner == 0:
        print("Ich habe gewonnen! 🤖")
    else:
        print("Unentschieden!")

# Spiel starten
if __name__ == "__main__":
    spiele()
