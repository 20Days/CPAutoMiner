import pynput.keyboard as kb
import pynput.mouse as ms
from pynput.mouse import Listener
import random
import time
from PIL import ImageGrab

xx = True
x1 = 0
x2 = 0
y1 = 0
y2 = 0
throwX = 0
throwY = 0
cA = "(99, 77, 73)"
cB = "(95, 73, 70)"
cC = "(87, 67, 64)"
cD = "(91, 70, 67)"
cE = "(84, 64, 61)"
cF = "(103, 80, 76)"
verbose = False

mouse = ms.Controller()
keyboard = kb.Controller()

v_mode = input('Would you like to run this in verbose mode?(y/N)')

if v_mode == 'y':
    verbose = True
    print('Verbose mode was turned on')
else:
    verbose = False

print('Please select the Top Left most point...')


def on_click(x, y, button, pressed):
    global x1, x2, y1, y2

    if str(button) == "Button.left" and pressed == True:
        if x1 == 0 and y1 == 0:
            x1 = x
            y1 = y
            print('First cords: X: ' + str(x1) + " Y: " + str(y1))
            print('Please now select the Bottom Right most point...')
        else:
            x2 = x
            y2 = y
            print('Second cords: X: ' + str(x2) + " Y: " + str(y2))
            listener.stop()
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
    if y1 < y2:
        randomY = random.randint(y1, y2)
        if verbose:
            print('Y1 is less than Y2')
    else:
        randomY = random.randint(y2, y1)
        if verbose:
            print('Y1 is greater than than Y2')
    image = ImageGrab.grab()
    color = image.getpixel((randomX, randomY))
    if (str(color) == cA) or (str(color) == cB) or (str(color) == cC) or (str(color) == cD) or (str(color) == cE) or (
            str(color) == cF):
        if verbose:
            print("Matches Color!")
        mouse.position = (randomX, randomY)
        print('Moving to {0}'.format(mouse.position))
        mouseClick()
        time.sleep(4)
    else:
        if verbose:
            print("Does not match color.")
        moveAndClick()


def dance():
    danceTime = random.randint(10, 15)
    keyboard.press('d')
    keyboard.release('d')
    print('Dancing for')
    for x in range(danceTime, 0, -1):
        print(x)
        time.sleep(1)


def throwBall():
    keyboard.press('t')
    keyboard.release('t')
    mouse.position = (throwX, throwY)
    time.sleep(.5)
    mouseClick()
    time.sleep(.5)


def throw():
    throwTimes = random.randint(3, 8)
    for x in range(1, throwTimes, 1):
        print('throwing ' + str(x) + ' of ' + str(throwTimes) + ' times')
        throwBall()


# Start

print('Starting script in ')
for x in range(5, 0, -1):
    print(x)
    time.sleep(1)

while 1 < 2:
    moveAndClick()
    dance()
    # canThrow = random.randint(1, 3)
    # if 2 == 1:
    #    throw()
    # else:
    #    print('no throw')
