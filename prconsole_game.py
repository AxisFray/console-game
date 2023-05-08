import random
import msvcrt
import sys
import os
import time


#---------------------USTAWIENIA GRY-----------------

size = 20  # wielkosc planszy
hor = 0  # liczba zdobytych konikow
hnum = 3        #ile konikow
gnum = 2        #ile duchow



#"\U0001F532"  space
#"\U0001F465"  enemy    horse "\U0001F40E"
# emoji ludzik konik drzwi
space = "\U0001F532"
body = "\U0001F3C3"
enemy = "\U0001F465"
horse = "\U0001F40E"
door = "🚪"
ghost = "\U0001F47B"
los1 = random.randint(0, size - 1)

bodyposx = random.randint(0, size - 1)  # ludzik x
bodyposy = random.randint(0, size - 1)  # ludzik y

hx = random.randint(0, size - 1)  # konik x
hy = random.randint(0, size - 1)  # konik y
hx1 = random.randint(0, size - 1)  # konik x1
hy1 = random.randint(0, size - 1)  # konik y2


gx = []         #duch x
gy = []         #duch y
gh = 0          #zdobyte duszki
gh1 = False     #wykorzystanie duszka

dx = random.randint(0, size - 1)  # drzwi x
dy = random.randint(0, size - 1)  # drzwi y
bx = bodyposx           #body x                     
by = bodyposy           #body y
d = False

# plansza gry
Board = []
hxx = [] 
hyy = []


for t in range(0,gnum):
    gx.append(random.randint(0,size-1))
    gy.append(random.randint(0,size-1))

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
    Ghost()


# drzwi wyjscie cel gry
def Exit():
    Board[dx][dy] = door
    
    
def Ghost():
    for p in range(0,gnum):
        if gx[p] == bx & gy[p] == by:
            gx[p] = random.randint(0,size)
            gy[p] = random.randint(0,size)
        if gx[p] == dx & gy[p] == dy:
            gx[p] = random.randint(0,size)
            gy[p] = random.randint(0,size)
        Board[gx[p]][gy[p]] = ghost




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

def GhCheck():
    global gh
    if key == "P":  #prawo
        if Board[bx + 1][by] == ghost:
            gh += 1
    elif key == "H":  #lewo
        if Board[bx - 1][by] == ghost:
            gh +=1
    elif key == "M":  #dol
        if Board[bx][by + 1] == ghost:
            gh +=1
    elif key == "K": #gora
        if Board[bx][by - 1] == ghost:
            gh +=1
    

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
    global bx, by, lpx, lpy, hor, d, key, gh, gh1
    key = msvcrt.getwche()
    
    lpx = bx
    lpy = by
    if key == "H":  # lewo
        if bx - 1 != -1:
            if Board[bx - 1][by] == enemy:
                if gh == 0:
                    Lose()
                else : gh1 = True
            elif Board[bx - 1][by] == horse:
                    hor += 1
            elif Board[bx - 1][by] == door:
               if hor == 1:
                   Win()
               else: d = True
            GhCheck()
            bx -= 1
            LastPos()
            os.system("cls")
            Body()
            ShowBoard()
            if gh1 == True:
                gh -= 1
                gh1 == False
            
    elif key == "P":  # prawo
        if bx + 1 != size:
            if Board[bx + 1][by] == enemy:
                if gh == 0:
                    Lose()
                else: gh1 = True
            elif Board[bx + 1][by] == horse:
                hor += 1
            elif Board[bx + 1][by] == door:
                if hor >= 1:
                    Win()
                else: d = True 
            GhCheck()
            bx += 1
            LastPos()
            os.system("cls")
            Body()
            ShowBoard()
            if gh1 == True:
                gh -= 1
                gh1 == False
    elif key == "M":  # dol
        if by + 1 != size:
            if Board[bx][by + 1] == enemy:
                if gh == 0 :
                    Lose()
                else : gh1  = True
            elif Board[bx][by + 1] == horse:
                hor += 1
            elif Board[bx][by + 1] == door:
                if hor == 1:
                    Win()
                else: d = True
            GhCheck()
            by += 1
            LastPos()
            os.system("cls")
            Body()
            ShowBoard()
            if gh1 == True:
                gh -= 1
                gh1 = False
    elif key == "K":  # gora
        if by - 1 != -1:
            if Board[bx][by - 1] == enemy:
                if gh == 0:
                    Lose()
                else: gh1 = True
            elif Board[bx][by - 1] == horse:
                hor += 1
            elif Board[bx][by - 1] == door:
                if hor == 1:
                    Win()
                else: d = True
            GhCheck()
            by -= 1
            LastPos()
            os.system("cls")
            Body()
            ShowBoard()
            if gh1 == True:
                gh -= 1
                gh1 = False
    else: key = "q"
    
    


#  prawyp  lewo   dolp prawo
# P prawy     H  lewy             K gora       M dol
# sprawdzanie wygranej

def Play():
    os.system("cls")
    b = 0
    GenBoard()
    ShowBoard()
    key = "H"
    while key != "q":
        Keys()
        print(gh)
        b += 1
    sys.exit()


Play()
