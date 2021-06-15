import digitalio
import busio
import board
from PIL import Image
from adafruit_epd.epd import Adafruit_EPD

upbut = digitalio.DigitalInOut(board.D5)
upbut.switch_to_input()
downbut = digitalio.DigitalInOut(board.D6)
downbut.switch_to_input()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None

from adafruit_epd.ssd1680 import Adafruit_SSD1680
display = Adafruit_SSD1680(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)
#Init EPD and Pins

def ClearDis(col):
  #Function to clear display black or white
  display.fill(Adafruit_EPD.BLACK) if col == 'black' else display.fill(Adafruit_EPD.WHITE)


while True:
  if upbut == False:
    image = Image.open("CurDis.png")
    display.image(image)
    display.display()
    print("Image sent.")

  elif downbut == False:
    ClearDis()
    print("Display whitened.")