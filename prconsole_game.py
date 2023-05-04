import pygame
import random
import msvcrt
from pynput.keyboard import  Listener, Controller
import sys
import os



size = 20  #wielkosc planszy
hor = 0  #liczba zdobytych konikow

#emoji ludzik konik drzwi
space = "\U0001F532"
body = "\U0001F3C3"
enemy = "\U0001F465"
horse = "\U0001F40E"
door = "\U0001F6AA"
los1  = random.randint(0,size-1)
bodyposx = random.randint(0,size-1) #ludzik x
bodyposy = random.randint(0,size-1) #ludzik y
hx = random.randint(0,size-1) #konik x
hy = random.randint(0,size-1)  #konik y
dx = random.randint(0,size-1) #drzwi x
dy = random.randint(0,size-1) #drzwi y

#plansza gry
Board = [
    
    ]

#dodawanie wierszy i kolumn
for y in range(0,size):
        Board.append([])


#generowanie planszy
def GenBoard():
    for i in range(0,size):
        for j in range(0,size):
            Board[i].append(random.choice([enemy,space,space,space,space]))
    Exit()
    Horse()
    Body()
    

#drzwi wyjscie cel gry
def Exit():
    Board[dx][dy] = door

#konik
def Horse():
    Board[hx][hy] = horse


#pozycja ludzika
def Body():
    global body
    Board[bodyposx][bodyposy]  = body
    

#wyswietlanie planszy
def ShowBoard():
    global body
    
    for r in range(0,size):
        for t in range(0,size):
            if t == size-1:
                print(Board[r][t])
            else : print(Board[r][t],end=" ")
    body = Board[bodyposx][bodyposy]
    
    
    
#sczytywanie klawiszy 
def on_key_realise(Key):
    global body
    if Key == 102:
        bodyposx += 1
        print('Released Key %s' % Key)
        
        ShowBoard()
    if Key == 100:
        bodyposx -= 1
        print('Released Key %s' % Key)
        ShowBoard()
    if Key == 98:
        bodyposy -= 1
        print('Released Key %s' % Key)
        ShowBoard()
    if Key == 104:
        bodyposy += 1
        print('Released Key %s' % Key)
        ShowBoard()


#sxczywtywanie klawiszy 2 proba
def Keys():
    msvcrt.getwch()
    key = msvcrt.getwche()
    print(key)
    w = 0
    while w >= 1:
        if key == b'K':
           bodyposx -= 1
           print("sdfwsdf")
        if key == b'M':
            bodyposx +=1
            print("sdfwsdf")
        if key == b'P':
            bodyposy += 1
            print("sdfwsdf")
        if key == b'H':
           bodyposy -= 1
           print("sdfwsdf")
        else : print("inny przycisk")
    

#sprawdzanie wygranej 
def Check():
    if Board[bodyposx][bodyposy] == enemy:
        print("Przegrales, sprobuj jeszcze raz")
        sys.exit(0)
    if Board[bodyposx][bodyposy] == door:
        print("Wygrales!")
        pass
    if Board[bodyposx][bodyposy] == horse:
        hor += 1 #licznik zdobytych konikow


Keys()

with Listener(on_realise=on_key_realise) as listener:
    listener.join()
    




    
   




