import pynput.keyboard as kb
import pynput.mouse as ms
from pynput.mouse import Listener
import random
import time

x1 = 0
x2 = 0
y1 = 0
y2 = 0
throwX = 0
throwY = 0

mouse = ms.Controller()
keyboard = kb.Controller()

def on_click(x, y, button, pressed):
    global x1, x2, y1, y2
    print(x, y, button, pressed)
    if str(button) == "Button.left" and pressed == True:
        if x1 == 0 and y1 == 0:
            x1 = x
            y1 = y
            print(str(x1) + " " + str(y1))
        else:
            x2 = x
            y2 = y
            print(str(x2) + " " + str(y2))
            return False
    else:
        if y2 == 0:
            return
        else:
            return False

 
with Listener(on_click=on_click) as listener:
    listener.join()

def mouseClick():
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)

def moveAndClick():
    randomX = random.randint(x1, x2)
    randomY = random.randint(y1, y2)
    mouse.position = (randomX, randomY)
    print('Now we have moved it to {0}'.format(mouse.position))
    mouseClick()
    time.sleep(4)

def dance():
    danceTime = random.randint(10,15)
    keyboard.press('d')
    keyboard.release('d')
    print('dancing for')
    for x in range(danceTime, 0, -1):
        print(x)
        time.sleep(1)

def throwBall():
    keyboard.press('t')
    keyboard.release('t')
    mouse.position = (throwX,ThrowY)
    time.sleep(.5)
    mouseClick()
    time.sleep(.5)

def throw():
    throwTimes = random.randint(3,8)
    for x in range(1, throwTimes, 1):
        print('throwing ' + str(x) + ' of ' + str(throwTimes) + ' times')
        throwBall()

#Start

print('Starting script in ')
for x in range(5,0,-1):
    print(x)
    time.sleep(1)

while 1 < 2:
    moveAndClick()
    dance()
    canThrow = random.randint(1,3)
    if 2 == 1:
        throw()
    else:
        print('no throw')