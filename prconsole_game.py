import random
import msvcrt
import sys
import os
import time
from colorama import Fore, Back, Style

#---------------------USTAWIENIA GRY-----------------

size = 30  # wielkosc planszy
hnum = 5        #ile konikow
gnum = 5        #ile duchow
space = Fore.WHITE+"\U0001F532"
body = "\U0001F3C3"
enemy = Fore.WHITE+"⬛"
horse = Fore.LIGHTRED_EX+"\U0001F40E"
door = "🚪"
ghost = Fore.BLUE+"\U0001F47B"


#"\U0001F532"  space
#"\U0001F465"  enemy    horse "\U0001F40E"
# emoji ludzik konik drzwi

los1 = random.randint(0, size - 1)

bodyposx = random.randint(0, size - 1)  # ludzik x
bodyposy = random.randint(0, size - 1)  # ludzik y

hor = 0  # liczba zdobytych konikow
hx = random.randint(0, size - 1)  # konik x
hy = random.randint(0, size - 1)  # konik y
hx1 = random.randint(0, size - 1)  # konik x1
hy1 = random.randint(0, size - 1)  # konik y2
hxx = [] 
hyy = []

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
            Board[i].append(random.choice([enemy,space,enemy,space, space, space,space]))
    
    Horse()
    Ghost()
    Exit()
    Body()
    
    


# drzwi wyjscie cel gry
def Exit():
    global dx,dy
    if dx == bx & dy == by:
        dx = random.randint(0,size-1)
        dy = random.randint(0,size-1)
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
    print(Fore.RED + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(Fore.RED +"              PRZEGRAŁEŚ!            ")
    print(Fore.RED +"          SPROBUJ JESZCZE RAZ        ")
    print(Fore.RED +"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(2)
    sys.exit()
    
def Win():
    os.system("cls")
    print(Fore.GREEN +"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(Fore.GREEN +"             WYGRYWASZ!               ")
    print(Fore.GREEN +"             GRATULACJE               ")
    print(Fore.GREEN +"      zebrałeś " , hor , " konikow    ")
    print(Fore.GREEN +"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
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
    
def Info():
    print(Fore.GREEN+"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(Fore.GREEN+"                ZBIERZ KONIKI I WYJDŹ PRZEZ DRZWI           ")
    print(Fore.GREEN+"             DUCHY POMOGĄ CI W PRZEJŚCIU PRZEZ ŚCIANY       ")
    print(Fore.GREEN+"                     PORUSZAJ SIĘ STRZAŁKAMI                ")
    print(Fore.GREEN+"             ←	          ↑       	→	       ↓          ")
    print(Fore.GREEN+"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    time.sleep(4)
    os.system('cls')
    
    


# wyswietlanie planszy
def ShowBoard():
    global body
    Board[bx][by] = body
    for r in range(0, size):
        for t in range(0, size):
            if t == size - 1:
                print(Fore.MAGENTA+Board[r][t])
            else:
                print(Fore.MAGENTA+Board[r][t], end=" ")
    


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
               if hor >= 1:
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
                gh1 = False
            
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
                gh1 = False
    elif key == "M":  # dol
        if by + 1 != size:
            if Board[bx][by + 1] == enemy:
                if gh == 0 :
                    Lose()
                else : gh1  = True
            elif Board[bx][by + 1] == horse:
                hor += 1
            elif Board[bx][by + 1] == door:
                if hor >= 1:
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
                if hor >= 1:
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
    Info()
    GenBoard()
    ShowBoard()
    key = "H"
    while key != "q":
        Keys()
        b += 1
    sys.exit()


Play()
