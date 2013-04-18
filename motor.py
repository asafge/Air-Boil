import RPi.GPIO as GPIO
import time

class Motor(object):

    def __init__(self, idle=0.1, channels=[4, 7 ,17, 18]):
        self.idle_time = idle
        GPIO.setmode(GPIO.BCM)
        self.channels = channels
        for channel in self.channels:
            self._setup_channel(channel)

    def _setup_channel(self, channel):
        GPIO.setup(channel, GPIO.OUT)

    def spin_cw(self, loops=200):
        self.turn_on([])

        for i in xrange(loops):
            print "at loop: %s/%s" % (i, loops)
            self.turn_on([7])
            self.turn_on([7, 18])
            self.turn_on([18])
            self.turn_on([18, 17])
            self.turn_on([17])
            self.turn_on([17, 4])
            self.turn_on([4])
            self.turn_on([4, 7])

        self.turn_on([])

    def spin_ccw(self, loops=200):
        self.turn_on([])

        for i in xrange(loops):
            print "at loop: %s/%s" % (i, loops)
            self.turn_on([4, 7])
            self.turn_on([4])
            self.turn_on([17, 4])
            self.turn_on([17])
            self.turn_on([18, 17])
            self.turn_on([18])
            self.turn_on([7, 18])
            self.turn_on([7])

        self.turn_on([])

    def _idle(self):
        time.sleep(self.idle_time)

    def turn_on(self, on):
        #print "turning on: %s" % on

        for channel in on:
            GPIO.output(channel, GPIO.HIGH)
        
        other_channels = set(self.channels)-set(on)
        for channel in other_channels:
            GPIO.output(channel, GPIO.LOW)

        self._idle()
