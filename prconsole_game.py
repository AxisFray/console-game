import random
import msvcrt
import sys
import os
import time


size = 20  # wielkosc planszy
hor = 0  # liczba zdobytych konikow
hnum = 3
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
d = False

# plansza gry
Board = []
hxx = [] #ilość konikow
hyy = []


for f in range(0,hnum):
    hxx.append(random.randint(0,size-1))
    hyy.append(random.randint(0,size-1))

# dodawanie wierszy i kolumn
for y in range(0, size):
    Board.append([])

def WBut():
    msvcrt.getwch()
    keyy = msvcrt.getwche()
    print(keyy)
# generowanie planszy
def GenBoard():
    for i in range(0, size):
        for j in range(0, size):
            Board[i].append(random.choice([enemy,space,enemy,space, space, space]))
    Exit()
    Horse()
    Body()


# drzwi wyjscie cel gry
def Exit():
    Board[dx][dy] = door
    
    


# konik
def Horse():
    global hxx, hyy, horse,hx1,hy1
    for o in range(0,hnum):
        if hxx[o] == dx & hyy[o] == dy:
            hxx = random.randint(0,size)
            hyy = random.randint(0,size)
        Board[hxx[o]][hyy[o]] = horse
    


# pozycja ludzika
def Body():
    Board[bx][by] = body

def LastPos():
    global d
    if d == True:
        Board[lpx][lpy] = door
    else: Board[lpx][lpy] = space
    d = False

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
    print("zebrałeś " , hor , " konikow")
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
    global bx, by, lpx, lpy, hor, d
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
            if hor >= 1:
                Win()
            else: d = True 
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

