import random
import msvcrt
import sys
import os
import time


size = 20  # wielkosc planszy
hor = 0  # liczba zdobytych konikow
#"\U0001F532"  space
#"\U0001F465"  enemy    horse "\U0001F40E"
# emoji ludzik konik drzwi
space = "\U0001F532"
body = "\U0001F3C3"
enemy = "\U0001F465"
horse = "\U0001F40E"
door = "🚪"
los1 = random.randint(0, size - 1)

bodyposx = random.randint(0, size - 1)  # ludzik x
bodyposy = random.randint(0, size - 1)  # ludzik y

hx = random.randint(0, size - 1)  # konik x
hy = random.randint(0, size - 1)  # konik y
hx1 = random.randint(0, size - 1)  # konik x1
hy1 = random.randint(0, size - 1)  # konik y2

dx = random.randint(0, size - 1)  # drzwi x
dy = random.randint(0, size - 1)  # drzwi y
bx = bodyposx
by = bodyposy
d = 0

# plansza gry
Board = []

def WBut():
    msvcrt.getwch()
    keyy = msvcrt.getwche()
    print(keyy)

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
    global hx, hy, horse,hx1,hy1
    if hx == dx & hy == dy:
        hx = random.randint(0,size)
        hy = random.randint(0,size)
    Board[hx][hy] = horse
    if hx1 == dx & hy1 == dy:
        hx1 = random.randint(0,size)
        hy1 = random.randint(0,size)
    Board[hx1][hy1] = horse


# pozycja ludzika
def Body():
    Board[bx][by] = body

def LastPos():
    if d == 1:
        Board[lpx][lpy] = door
    else: Board[lpx][lpy] = space

    

def Lose():
    os.system("cls")
    print("PRZEGRAŁEŚ!")
    print("SPROBUJ JESZCZE RAZ")
    time.sleep(2)
    sys.exit()
    
def Win():
    os.system("cls")
    print("WYGRYWASZ!")
    print("GRATULACJE")
    time.sleep(2)
    sys.exit()


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
#       if bx - 1 <= 0:
#            pass
        if Board[bx - 1][by] == enemy:
            Lose()
        elif Board[bx - 1][by] == horse:
            hor += 1
        elif Board[bx - 1][by] == door:
            if hor == 1:
                Win()
            else: d += 1
        bx -= 1
        LastPos()
        os.system("cls")
        Body()
        ShowBoard()
    elif key == "P":  # prawo
#        if bx + 1 >= size:
#            pass
        if Board[bx + 1][by] == enemy:
            Lose()
        elif Board[bx + 1][by] == horse:
            hor += 1
        elif Board[bx + 1][by] == door:
            if hor == 1:
                Win()
            else: d += 1
        bx += 1
        LastPos()
        os.system("cls")
        Body()
        ShowBoard()
    elif key == "M":  # dol
#       if by + 1 >= size:
#          pass
        if Board[bx][by + 1] == enemy:
            Lose()
        elif Board[bx][by + 1] == horse:
            hor += 1
        elif Board[bx][by + 1] == door:
            if hor == 1:
                Win()
            else: d += 1
        by += 1
        LastPos()
        os.system("cls")
        Body()
        ShowBoard()
    elif key == "K":  # gora
#        if by - 1 <= 0:
#            pass
        if Board[bx][by - 1] == enemy:
            Lose()
        elif Board[bx][by - 1] == horse:
            hor += 1
        elif Board[bx][by - 1] == door:
            if hor == 1:
                Win()
            else: d += 1
        by -= 1
        LastPos()
        os.system("cls")
        Body()
        ShowBoard()
    
    


#  prawyp  lewo   dolp prawo
# P prawy     H  lewy             K gora       M dol
# sprawdzanie wygranej

def Play():
    os.system("cls")
    b = 0
    GenBoard()
    ShowBoard()
    while b <= 99999999999:
        Keys()
        b += 1

Play()

