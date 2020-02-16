#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(19, GPIO.FALLING)
	print("Low Battery. Shutting down now!")
	os.system("sudo shutdown 5")
except:
	pass
finally:
	GPIO.cleanup()
