#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(pin, GPIO.FALLING)
	print("Low Battery. Shutting down now!")
	os.system("sudo shutdown 5")
except:
	pass
finally:
	GPIO.cleanup()
