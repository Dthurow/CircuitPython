# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

RED = 0x100000  # (0x10, 0, 0) also works
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)

colorRotation = [RED, YELLOW, PURPLE, GREEN, AQUA, BLACK ]


#main loop
while True:
	for i in range(30):
		curIndex = i % len(pixels)
		curColor = i % len(colorRotation)
		pixels[curIndex] = colorRotation[curColor]
		time.sleep(.5)
