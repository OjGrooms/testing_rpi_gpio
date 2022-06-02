import RPi.GPIO as gpio
from timer import ButtonTimeout
gpio.setmode(gpio.BOARD)

class ButtonTimer(object):
    def __init__(self):
        print('__init__')
        gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        self.rtc = ButtonTimeout(5, self.falling)

    def start(self):
        print('Starting self')
        gpio.add_event_detect(16, gpio.RISING, callback=self.rising, bouncetime=50)

    def falling(self, channel):
        print('button pressed')
        gpio.remove_event_detect(16)
        gpio.add_event_detect(16, gpio.RISING, callback=self.rising, bouncetime=50)
        self.rtc.cancel()

    def rising(self, channel):
        print('button released')
        gpio.remove_event_detect(16)
        gpio.add_event_detect(16, gpio.FALLING, callback=self.falling, bouncetime=50)
        self.rtc.start()

bt = ButtonTimer()
bt.start()

try:
    print('trying input')
    input()

except KeyboardInterrupt:
    pass

gpio.cleanup()
