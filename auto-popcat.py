import pyautogui
import time
from pynput.mouse import Button, Controller

LIMIT = 800
SLEEP = 0.5

print("Starting in 3 seconds")
time.sleep(3)

#run the below two lines and get the coordinates of the postion to click 
init_x, init_y =pyautogui.position() 
print(init_x,init_y)


count=0
while count!=LIMIT: #set value for amount of times to click
    cur_x, cur_y = pyautogui.position()
    pyautogui.click(cur_x, cur_y)
    count+=1
    time.sleep(SLEEP)
    print(count)
    print(cur_x, cur_y)

    if cur_x != init_x or cur_y != init_y:
        print("Mouse moved, stopping")
        break
