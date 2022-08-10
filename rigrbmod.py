import xlrd
from time import time
import time as ti
import keyboard
import pyautogui
import os
import ctypes

loct = ('C:\\Users\\Preetish\\Desktop\\New folder (2)\\hcr bot\\data\\1r.xls')

wb = xlrd.open_workbook(loct)     
sheet = wb.sheet_by_index(0) 

os.system('cls')

t = time()


def cell(x):
    if x == 0:
        return 0
    else:
        return sheet.cell_value(x,0)

for i in range(1,1000):
    try:
        c = cell(i)
    except IndexError:
        z = i
        break

print(z)

n = 1
print("Press q to start")

while 1:
    if keyboard.is_pressed('q') == True:
        break

ti.sleep(1)
print("Started")

while n<z:
    ctypes.windll.user32.mouse_event(0x0010)
    ti.sleep(cell(n)-cell(n-1))
    ctypes.windll.user32.mouse_event(0x0008)
    ti.sleep(cell(n+1)-cell(n))
    n = n+2

ctypes.windll.user32.mouse_event(0x0010)

print("Finished")
