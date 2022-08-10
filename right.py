import time as ti
import keyboard
from time import time,ctime
import os
import xlwt
import xlrd
from xlutils.copy import copy

os.system('cls')

loct = 'C:\\Users\\Preetish\\Desktop\\New folder (2)\\hcr bot\\data\\1r.xls'

rb = xlrd.open_workbook(loct)
wb = copy(rb)
w_sheet = wb.get_sheet(0)

X = []

while 1:
    if keyboard.is_pressed('q'):
        break

ti.sleep(0.5)
print("Start")

t = time()   
while 1:
    while keyboard.is_pressed('right arrow') ==True:
        a = time()
        c = a-t
        X.append(c)
        while 1:
            if keyboard.is_pressed('right arrow') == False:
                b = time()
                c = b-t
                X.append(c)
                break
            if keyboard.is_pressed('q') == True:
                break        
    if keyboard.is_pressed('q') == True:
        break        


for n in range(len(X)):
    w_sheet.write(n+1,0,X[n])
for n in range(len(X),10000):
    w_sheet.write(n+1,0,'')

print("Finished")

wb.save(loct)