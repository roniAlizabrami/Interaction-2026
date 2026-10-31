# UFO cow game controller.
# Sends tilt and the buttons over USB serial, about 25 times a second.
# Each line looks like:  x,y,b,a   for example  -240,512,1,0
#   x = tilt left/right, y = tilt forward/back (about -1024 to 1024)
#   b = 1 while button B is held (tractor beam), otherwise 0
#   a = 1 once each time button A is pressed (switches day and night), otherwise 0
from microbit import *

uart.init(baudrate=115200)

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    b = 1 if button_b.is_pressed() else 0
    a = 1 if button_a.was_pressed() else 0
    print("{},{},{},{}".format(x, y, b, a))
    if b:
        display.show(Image.ARROW_S)
    else:
        display.clear()
    sleep(40)
