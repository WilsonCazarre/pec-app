import numpy as np
from threading import Thread
from time import sleep
import os

class Function:

	#static variables control thread syncronization among all Function instances
	#there can only be one function running at any given time
	thread_switch = True	#tells the running function to stop execution
	thread_feedback = True	#tells the waiting function if the execution has been stoped

    # abstract method, represents the function main loop
	def calc(self):
	    pass

    # launches the main loop in a separate thread
	def launch(self):
		Function.thread_switch = False
		while not self.thread_feedback:
		    continue

		Function.thread_feedback = False
		Function.thread_switch = True
		Thread(target=self.calc, daemon=True).start()

    # when the object finishes execution, tells the module that a new thread can be launched
	def __del__(self):
	    Function.thread_feedback = True

	@staticmethod
	def adapt(x, lo=0, hi=1, n_lo=0, n_hi=255):
	    tang = ((n_hi - n_lo) / (hi - lo)) if lo != hi else 0
	    disloc = n_lo - tang * lo
	    return tang * x + disloc


class Fade(Function):

    # vR, vG, vB are the velocities witch the individual channels change colors
    # dir represents the direction of groth, if dir == 1 the channel get brighter by V units, if dir == -1 the channel gets dimmer by V units

    # Dom(vN) = [0-255]

    def __init__(self, led, vR, vG, vB, time):

        self.led = led

        self.time = time
        self.current = [0, 0, 0]
        self.speed = [vR, vG, vB]
        self.dir = [1, 1, 1]

    def increment(self, index):
        buff = self.current[index] + self.speed[index] * self.dir[index]

        if 0 <= buff and buff <= 255:
            self.current[index] = buff
        else:
            self.dir[index] *= -1

    def calc(self):
        while Function.thread_switch:

            for i in range(3):
                self.increment(i)

            self.led.send(arr=self.current)
            sleep(self.time)


class Curvy(Function):
    def __init__(self, led, sound, cR, cG, cB, dim):
        self.led = led
        self.sound = sound

        self.curviness = [cR, cG, cB]
        self.normalize = [0, 0, 0]
        self.last = [0, 0, 0]
        self.regen = 0.00000001
        self.dim = dim

    def calc(self):

	    while Function.thread_switch:
	        
	        freqs = np.abs(np.fft.rfft(self.sound.listen()))
	        out = [0, 0, 0]

	        idx = 0
	        quota = (len(freqs) + len(freqs) % 3) // 3

	        for hz in freqs:
	        	color = idx // quota

	        	if hz > out[color]:
	        		out[color] = hz

	        		if hz > self.normalize[color]:
	        			self.normalize[color] = hz

	        	idx += 1

	       	out = [(x + y)/c for x,y,c in zip(out,self.last,self.curviness)]
	        self.last = [x for x in out]
	        out = [int(self.dim * Function.adapt(x, hi= y)) for x, y in zip(out,self.normalize)]
	        self.normalize = [x - self.regen for x in self.normalize]
	        self.led.send(arr=out)


class Interpolate(Function):

	# implementation asumptions:
	#	points is a list of dictionaries: [{"x": n1, "y": n2}, {"x": n3, "y": n4}, ... , {"x": nn, "y": nm}] 
	# 	points is ordered in the x axis
	# 	both x and y coordinates are between [0 - 1]
	#	all of the x axis is represented

	class Curve:

		def __init__(self, points):
			self.points = points
			self.numb = points[0]["y"]
			self.section = 0
			
			self.quota = [0 for x in range(len(points)-1)]
			self.tang = [0 for x in range(len(points)-1)]

		def set_resolution(self,samples):
			self.numb = self.points[0]["y"]
			self.samples = samples
			self.section = 0
			return self.__iter__()

		def __iter__(self):
			self.quota = [int((f["x"] - i["x"]) * self.samples) for f,i in zip(self.points[1:], self.points[0:])]
			for i in range(self.samples - sum(self.quota)):
				self.quota[i % len(self.quota)] += 1
			self.tang = [(f["y"] - i["y"])/q for f,i,q in zip(self.points[1:],self.points[0:],self.quota)]

			return self

		def __next__(self):
			try:
				self.section += 0 if self.quota[self.section] > 0 else 1				
				self.numb += self.tang[self.section]
				self.quota[self.section] -= 1
				return self.numb

			except IndexError:
				raise StopIteration

	def __init__(self, led, sound, points, color, curviness, dim):
	    self.led = led
	    self.sound = sound

	    self.curve = self.Curve(points)
	    self.curviness = curviness
	    self.last = 0
	    self.base = color
	    self.normalize = 0
	    self.regen = 0.0000001
	    self.dim = dim

	def calc(self):

		while Function.thread_switch:
			freqs = np.abs(np.fft.rfft(self.sound.listen()))
			gains = self.curve.set_resolution(len(freqs))
			out = 0
			
			for hz, gain in zip(freqs,gains):
				out += hz * gain
			out = out/len(freqs)
			
			self.normalize = self.normalize if out < self.normalize else out
			out = out / self.normalize
			self.normalize -= self.regen
			out = (out + self.last)/self.curviness
			self.last = out 
			self.led.send([int(c * out * self.dim) for c in self.base])

