# CircuitPlaygroundExpress_CapTouch

import time

import board
import touchio
import neopixel

#global stuff
RED = 0x100000  
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)


class touchSensor:
    isOn = False
    color = (255,0,0)
    pixelIndex = 0


    def __init__(self, color, pixelIndex, touchsens):
        self.color = color
        self.pixelIndex = pixelIndex
        self.touch = touchsens

    def checkTouch(self):
        if self.touch.value and self.isOn:
            pixels[self.pixelIndex] = (0,0,0)
            self.isOn = False
        elif self.touch.value and not self.isOn:
            pixels[self.pixelIndex] = self.color
            self.isOn = True

#set up
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)


touchPads = {"touch1" : touchSensor(RED, 6, touch1),
"touch2" : touchSensor(AQUA, 8, touch2),
"touch3" : touchSensor(PURPLE, 9, touch3),
"touch4" : touchSensor(BLUE, 1, touch4),
"touch5" : touchSensor(YELLOW, 2, touch5),
"touch6" : touchSensor(BLUE, 3, touch6),
"touch7" : touchSensor(GREEN, 4, touch7),

  }

#main loop
while True:
    for t in touchPads.keys():
        touchPads[t].checkTouch()
    time.sleep(0.2)



