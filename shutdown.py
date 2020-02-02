#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonCallback(channel):
	print("button pushed")

try:
	GPIO.wait_for_edge(21, GPIO.FALLING)
	os.system("sudo shutdown -h now")
except:
	pass
finally:
	GPIO.cleanup()
