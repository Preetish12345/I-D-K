import time
import keyboard
from time import time,ctime
import os

def clear():
    os.system('cls')

clear()

X = []
Y = []


if keyboard.is_pressed('q') == False: 
    t = time()   
    while 1:
        while keyboard.is_pressed('left arrow') ==True:
            a = time()
            c = a-t
            Y.append(c)
            print('Y ',Y)
            while 1:
                if keyboard.is_pressed('left arrow') == False:
                    b = time()
                    c = b-t
                    X.append(c)
                    print('X ',X)
                    break
                if keyboard.is_pressed('q') == True:
                    break                     
        if keyboard.is_pressed('q') == True:
            break   

