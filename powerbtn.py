#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

pin=27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(pin, GPIO.FALLING)
	print("Power button pressed. Shutting down now!")
	os.system("sudo shutdown now")
except:
	pass
finally:
	GPIO.cleanup()
