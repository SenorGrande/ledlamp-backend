import time
import board
import neopixel

pixel_pin = board.D18

num_pixels = 3

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
  pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pixels.fill((255, 0, 0))
pixels.show()
