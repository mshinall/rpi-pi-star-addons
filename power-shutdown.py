#!/usr/bin/python -d
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO

pin = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	GPIO.wait_for_edge(pin, GPIO.FALLING)
	print("External power off. Shutting down now!")
	os.system("sudo shutdown now")
except:
	pass
finally:
	GPIO.cleanup()
