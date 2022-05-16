import numpy as np
from threading import Thread
from time import sleep
import os


thread_swtich = True 
thread_feedback = True 

class Adapter:

	def __init__(self, lo = 0, hi = 1, n_lo = 0, n_hi = 255):

		self.lo = lo
		self.hi = hi
		self.n_lo = n_lo
		self.n_hi = n_hi

		self.tang = (n_hi - n_lo)/(hi - lo) if hi != lo else 0
		self.disloc = n_lo - a * lo

	def format(x):
		return int(a*x + b)

	def update_coefs(self, hi):

		self.tang = (n_hi - n_lo)/(hi - lo) if hi != lo else 0
		self.disloc = n_lo - a * lo

class Function:

	# abstract method, represents the function main loop
	def calc(self):
		pass

	# launches the main loop in a separate thread
	def launch(self):
		thread_swtich = False
		while not thread_feedback:
			continue

		thread_feedback = False
		thread_swtich = True
		Thread(target=self.calc,daemon=True).start()

	#when the object ginishes executions, tells the module that a new thread can be launched
	def __del__(self):
		thread_feedback = True

class Fade(Function):

	#vR, vG, vB are the velocities witch the individual channels change colors
	#dir represents the direction of groth, if dir == 1 the channel get brighter by V units, if dir == -1 the channel gets dimmer by V units

	#Dom(vN) = [0-255]
	
	def __init__(self,led, vR, vG, vB, time):

		self.led = led
		
		self.time = time
		self.current = [0,0,0]
		self.speed = [vR,vG,vB]
		self.dir = [1,1,1]
	
	def increment(self,index):
		buff = self.current[index] + self.speed[index] * self.dir[index]  

		if 0 <= buff and buff <= 255:
			self.current[index] = buff
		else:
			self.dir[index] *= -1 

	def calc(self):
		# while thread_swtich:

		for i in range(3):
			self.increment(i)

			#time delay here

test = Fade(1,1,10,100,10,20,30)

for i in range(5):
	for num in test.current:
		print(num)
	print(" ")	

	test.calc()


