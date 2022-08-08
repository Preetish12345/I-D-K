import time
import keyboard
from time import time,ctime
import os
import xlwt
import xlrd
from xlutils.copy import copy

os.system('cls')

X = []

while 1:
    if keyboard.is_pressed('q'):
        break

t = time()   
while 1:
    while keyboard.is_pressed('left arrow') ==True:
        a = time()
        c = a-t
        X.append(c)
        while 1:
            if keyboard.is_pressed('left arrow') == False:
                b = time()
                c = b-t
                X.append(c)
                break
            if keyboard.is_pressed('q') == True:
                break                     
    if keyboard.is_pressed('q') == True:
        break   

print(X)

rb = xlrd.open_workbook('data21.xls')
wb = copy(rb)
w_sheet = wb.get_sheet(0)

for n in range(len(X)):
    w_sheet.write(n+1,0,X[n])
for n in range(len(X),10000):
    w_sheet.write(n+1,0,'')

wb.save('data21.xls')  