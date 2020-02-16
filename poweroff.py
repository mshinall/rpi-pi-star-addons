#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(23, GPIO.FALLING)
	print("Power button pressed. Shutting down now!")
	os.system("sudo shutdown now")
except:
	pass
finally:
	GPIO.cleanup()
