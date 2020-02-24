#!/usr/bin/python -d
# -*- coding: utf-8 -*-

import os
import RPi.GPIO as GPIO
import time

pin = 27
wait_secs = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		GPIO.wait_for_edge(pin, GPIO.FALLING)
		ms = int(round(time.time() * 1000))
		print("Power button pressed. Waiting " + str(wait_secs) + " seconds...")
		while GPIO.input(pin) == GPIO.LOW:
			ms2 = int(round(time.time() * 1000))
			print(str(ms2 - ms))
			if ms2 - ms > 1000 * wait_secs:
				print("Power button held for " + str(wait_secs) + " seconds. Shutting down now!")
				os.system("sudo shutdown now")
			time.sleep(0.1)
except:
	pass
finally:
	GPIO.cleanup()
