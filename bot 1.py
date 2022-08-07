import time
import keyboard
from time import time,ctime
import os

def clear():
    os.system('cls')

clear()

X = []
Y = []

n = 0
b = 0

if keyboard.is_pressed('q') == False: 
    t = time()   
    while 1:
        while keyboard.is_pressed('right arrow') ==True:
            a = time()
            c = a-b
            if c<10000:
                Y.append(c)
            print('Y ',Y)
            while 1:
                if keyboard.is_pressed('right arrow') == False:
                    b = time()
                    c = b-a
                    X.append(c)
                    print('X ',X)
                    break

#        while keyboard.is_pressed('right arrow') ==False:
#            a = time()
#            while 1:
#                if keyboard.is_pressed('right arrow') == True:
#                    b = time()
#                    c = b-a
#                    Y.append(c)
#                    print(Y)
#                    break

# editor notes
