import numpy as np
from threading import Thread
from time import sleep
import os


thread_lock = False
thread_died = True 

class f_interface:

	def __init__(self):
		pass

	def calc(self):
		pass

	def map(x, lo, hi, nlo, nhi):
		x = lo if x < lo else x
		x = hi if x > hi else x

		a = (nhi-nlo)/(hi-lo) if hi != lo else 255
		b = nlo - a * lo

		return int(a*x + b)

	def parse(prompt):
		
		def parse_loop():

			param = input(prompt)
			param = param.split(",")


			out = [1,1,1]
			try:
				for i in range(len(out)):
					out[i] = int(param[i])
				return out

			except IndexError:
				f_interface.print_err("faltam índices")
				return False
			except:
				f_interface.print_err("parametro deve ser numérico")
				return False

		done = False
		while not done:
			done = parse_loop()
		return done 

	def isvalid():

		global thread_lock
		global thread_died

		if thread_lock:
			return True
		else:
			thread_died = True
			return False

	def launch(self):
	
			global thread_lock
			global thread_died

			thread_lock = False
			
			while not thread_died:
				continue

			thread_lock = True
			thread_died = False

			test = Thread(target= self.calc,
				   daemon=True).start()
		
	def print_err(info):
		os.system("echo [31m" + "err:" + "[0m" + " " + info)


class curvy(f_interface):

	def __init__(self, led, device):
			self.led = led
			self.device = device

			self.curvyness = f_interface.parse(">> digite o índice de curvatura: ")
			self.normalize = [0,0,0]
			self.last = [0,0,0]
			self.regen = 0.00000001

			
	def calc(self):
		
		while f_interface.isvalid():

			freqs = np.abs(np.fft.rfft(self.device.listen()))
			out = [0,0,0]
			ratio = int(len(freqs)/3)

			for color in range(3):
				for value in freqs[ratio * color : ratio * (color+1) - 1]:
					
					if value > out[color]:
						out[color] = value

						if out[color] > self.normalize[color]:
							self.normalize[color] = out[color]

				out[color] = self.last[color] + (out[color] - self.last[color])/self.curvyness[color]
				self.last[color] = out[color]
				out[color] = f_interface.map(out[color], 0, self.normalize[color], 0, 255)
				self.normalize[color] -= self.regen

			self.led.send(arr = out)
 
class fade(f_interface):

	def __init__(self, led):
		self.dir = [1,1,1]
		self.current = [0,0,0]
		self.led = led
		
		test = 0

		while test != 3:
			test = 0
			self.speed = f_interface.parse(">> digite a velocidade: ")
			
			for numb in self.speed:
				test += 1 if -1< numb and numb < 256 else 0

			if test < 3:
				f_interface.print_err("valores devem ser na faixa de 0-255")

		while True: 
			try:
					self.interval = float(input(">> digíte a frequência de atualização: ")) 
					if self.interval <= 0:
						f_interface.print_err("o valor não pode ser menor ou igual a zero")	
					break
			except:
				f_interface.print_err("o intervalo deve ser um número maior que zero")  

	def calc(self):
		
		while f_interface.isvalid():
			
			for i in range(len(self.current)):

				if self.current[i] + self.speed[i] * self.dir[i] > 255 or self.current[i] + self.speed[i] * self.dir[i] < 0:
					self.dir[i] *= -1
				self.current[i] += self.speed[i] * self.dir[i]  
			
			self.led.send(arr=self.current)
			sleep(self.interval) 	


class interpolation(f_interface):


	class gain_iterator:

		def __init__(self, curve):
			
			self.points = curve
			

		def __iter__(self):
			
			remainder = self.n_points
			self.points["n"] = []
			self.value = self.points["y"][0]
			self.section = 0
			
			# distribuí os pontos de acorodo com a regra de 3

			i = 1
			while i < len(self.points["x"]):

				real = (self.points["x"][i] - self.points["x"][i-1])/100 * self.n_points
				floor = int(real)
				remainder -= floor
				self.points["n"].append(floor)
				i += 1

			# distribuí o resto caso exista

			i = 0
			while remainder != 0:

				self.points["n"][i % len(self.points["n"])] += 1
				remainder -= 1
				i+= 1

			# calcula o inclinação de cada reta
			
			self.points["i"] = []
			i = 1
			while i < len(self.points["y"]):
				self.points["i"].append((self.points["y"][i] - self.points["y"][i-1])/self.points["n"][i-1]) 
				i += 1

			return self

		def refresh(self,n_points):
			self.n_points = n_points
			return self.__iter__()

		def __next__(self):

			#caso não hajam mais pontos na seção atual
			try:
				if self.points["n"][self.section] == 0:
					self.section += 1 							#incrementa a seção
				
			
				#caso hajam pontos na seção atual

				self.points["n"][self.section] -= 1 			#decrementa o número de pontos da seção
				self.value += self.points["i"][self.section]	#soma o ganho da seção ao valor atual
				return self.value 								#retorna o valor atual

			#caso a seção exeda os limites da curva
			except IndexError:
				raise StopIteration							#fim da execução 
			

	def __init__(self, led, device):
		self.led = led 
		self.device = device
		
		self.gains = self.gain_iterator({"x":[0,	30, 	100],
										 "y":[1,	0.1,	0  ]})
		self.curvyness = int(input(">>curvyness: "))	#place holder
		self.normalize_hi = 0
		
		self.cut_factor = float(input(">>fator de corte: "))			#place holder	
		self.cut_val = 0
		
		self.last = 0


	def calc(self):

		while f_interface.isvalid():

			freqs = np.abs(np.fft.rfft(self.device.listen()))
			gains = self.gains.refresh(len(freqs) - 1)
			freqs = iter(freqs)
			
			out = 0
			current = 0

			for gain, sample in zip(gains, freqs):
				current =  gain * sample if gain * sample > current else current 

			
			if self.normalize_hi < current:
				self.normalize_hi = current
				self.cut = current * self.cut_factor
			else:
				current = current if current > self.cut_val else 0
			
			out = current + abs(current - self.last)/self.curvyness
			self.last = out

			out = f_interface.map(out, 0, self.normalize_hi, 0, 255)	
			out =  out if out > 100 else int(0) 								# fator de corte, implementação ignora o fator de curvatora, isso deve ser corrigido!
			self.led.send(arr = [out,0,0])										# o fator de corte e uttil, mas clama pela regeneração da normalização


