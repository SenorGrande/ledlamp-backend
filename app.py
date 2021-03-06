import cherrypy

import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 3
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
  pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

@cherrypy.expose
class LedLamp(object):

  @cherrypy.tools.accept(media='text/plain')
  def GET(self):
    return "bruh"

  def POST(self, colour):
    colour_hex = colour.lstrip('#')
    colour_rgb = tuple(int(colour_hex[i:i+2], 16) for i in (0, 2, 4))
    print(colour_hex)
    print(colour_rgb)
    pixels.fill(colour_rgb)
    pixels.show()
    return colour_hex

if __name__ == '__main__':
  #cherrypy.quickstart(HelloWorld())
  conf = {
    '/': {
      'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
      'tools.sessions.on': True,
      'tools.response_headers.on': True,
      'tools.response_headers.headers': [('Content-Type', 'text/plain')],
    }
  }
  cherrypy.quickstart(LedLamp(), '/', conf)

