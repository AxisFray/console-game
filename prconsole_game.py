import random
import msvcrt
import sys
import os


size = 20  # wielkosc planszy
hor = 0  # liczba zdobytych konikow

# emoji ludzik konik drzwi
space = "\U0001F532"
body = "\U0001F3C3"
enemy = "\U0001F465"
horse = "\U0001F40E"
door = "\U0001F6AA"
los1 = random.randint(0, size - 1)
bodyposx = random.randint(0, size - 1)  # ludzik x
bodyposy = random.randint(0, size - 1)  # ludzik y
hx = random.randint(0, size - 1)  # konik x
hy = random.randint(0, size - 1)  # konik y
dx = random.randint(0, size - 1)  # drzwi x
dy = random.randint(0, size - 1)  # drzwi y
bx = bodyposx
by = bodyposy


# plansza gry
Board = []

# dodawanie wierszy i kolumn
for y in range(0, size):
    Board.append([])


# generowanie planszy
def GenBoard():
    for i in range(0, size):
        for j in range(0, size):
            Board[i].append(random.choice([enemy, space, space, space, space]))
    Exit()
    Horse()
    Body()


# drzwi wyjscie cel gry
def Exit():
    Board[dx][dy] = door


# konik
def Horse():
    Board[hx][hy] = horse


# pozycja ludzika
def Body():
    global body
    Board[bodyposx][bodyposy] = body
    """
#sczytywanie klawiszy 
def on_key_realise(Key):
    global body
    if Key == 102:
        bx += 1
        print('Released Key %s' % Key)
        ShowBoard()
    if Key == 100:
        bx -= 1
        print('Released Key %s' % Key)
        ShowBoard()
    if Key == 98:
        by -= 1
        print('Released Key %s' % Key)
        ShowBoard()
    if Key == 104:
        by += 1
        print('Released Key %s' % Key)
        ShowBoard()

"""


# wyswietlanie planszy
def ShowBoard():
    global body

    for r in range(0, size):
        for t in range(0, size):
            if t == size - 1:
                print(Board[r][t])
            else:
                print(Board[r][t], end=" ")
    Board[bx][by] = body


# sxczywtywanie klawiszy 2 proba
def Keys():
    msvcrt.getwch()
    global bx, by, lpx, lpy
    key = msvcrt.getwche()
    lpx = bx
    lpy = by
    if key == "H":  # lewo
        if bx - 1 < 0:
            pass
        bx -= 1
        Board[lpx][lpy] = space
        os.system("cls")
        ShowBoard()
        os.system("cls")
        ShowBoard()
    if key == "P":  # prawo
        if bx + 1 > size - 1:
            pass
        bx += 1
        Board[lpx][lpy] = space
        os.system("cls")
        ShowBoard()
        os.system("cls")
        ShowBoard()
    if key == "M":  # dol
        if by + 1 > size - 1:
            pass
        by += 1
        Board[lpx][lpy] = space
        os.system("cls")
        ShowBoard()
        os.system("cls")
        ShowBoard()
    if key == "K":  # gora
        if by - 1 < 0:
            pass
        by -= 1
        Board[lpx][lpy] = space
        os.system("cls")
        ShowBoard()
        os.system("cls")
        ShowBoard()
    


#  prawyp  lewo   dolp prawo
# P prawy     H  lewy             K gora       M dol
# sprawdzanie wygranej
def Check():
    if Board[bx][by] == enemy:
        print("Przegrales, sprobuj jeszcze raz")
        sys.exit(0)
    if bx == dx & by == dy:
        print("Wygrales!")
        pass
    if bx == hx & by == hy:
        hor += 1  # licznik zdobytych konikow


os.system("cls")
b = 0
GenBoard()
ShowBoard()
while b <= 99999999999:
    Keys()
    Check()
    b += 1


"""
with Listener(on_realise=on_key_realise) as listener:
    listener.join()
    
"""
