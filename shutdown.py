#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(21, GPIO.FALLING)
	print("External power off. Shutting down in 5 minutes...")
	os.system("sudo shutdown 5")
except:
	pass
finally:
	GPIO.cleanup()
