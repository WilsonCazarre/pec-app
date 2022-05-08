import lb
import led
import os
import func

def init():
	
	os.system("cls")
	logo()
	print(lb.LoopBack.input_list())
			
	def setup_lb():
		global hw_lb
		
		try:
			numb = int(input("digite o número do dispositivo: "))

		except: #ERR NÃO NUMÉRICO
			print_err("o valor informado não é numérico")
			return False

		if numb < 0:	#ERR NEGATIVO
			print_err("numeros negativos não são permitidos")
			return False
		
		try:	#ERR: IDX OUT OF RNG
			hw_lb = lb.LoopBack(numb)
		except:
			print_err("o dispositivo informado é inválido")
			return False

		return True

	def setup_led():
		global hw_led 

		try:
			hw_led = led.LEDs(input("digite a COM desejada: "))
			return True
		except:
			print_err("COM inválida")
			return False

	if not preset():
		while not setup_lb():
			continue

		while not setup_led():
			continue 

	os.system("echo [42m[30mSucesso![0m")


def quit():
	#salvamento opicional do dispositivo e COM
	os.system("echo [0m")
	raise SystemExit()

def preset():
	#promp para o carregamento do COM e dispositivo
	#returna true em caso de carregamento
	return False 

# -----------------------------------------------

def com():
	try:
		hw_led.set_com(input(">> nome da COM: "))
	except:
		print_err("COM inválida")


def color():
	try:
		hw_led.send(string = input(">> valor da cor: "))
	except:
		print_err("valor R,G,B inválido\n")
		

def load():
	try:
		hw_led.send(arr = [0,0,0], code = "l")
	except:
		print_err("falha na comunicação\n")


def save():
	try:
		hw_led.send(string = input(">> valor da cor: "), code = "s")
	except:
		print_err("valor R,G,B inválido\n")

# -----------------------------------------------

def audio():
	
	print_err(lb.LoopBack.input_list())
		
	try:
		numb = int(input(">> digite o número do dispositivo: "))

	except: #ERR NÃO NUMÉRICO
		print_err("o valor informado não é numérico\n")
		
	if numb < 0:	#ERR NEGATIVO
		print_err("numeros negativos não são permitidos\n")
		return
	
	try:	#ERR: IDX OUT OF RNG
		hw_lb.set_input(numb)
	except:
		print_err("o dispositivo informado é inválido\n")
	
# -----------------------------------------------

def kill():
	func.thread_lock = False
	load()

def curvy():
	f = func.curvy(hw_led, hw_lb)
	f.launch()

def fade():
	f = func.fade(hw_led)
	f.launch()

def interpolate():
	f = func.interpolation(hw_led, hw_lb)
	f.launch()



whitelist = {
			 "color": color,
			 "load" : load,
			 "save" : save,
			 "audio": audio,
			 "com": com,
			 "quit": quit,
			 "exit": quit, 
			 "load": load,
			 "curvy": curvy,
			 "kill": kill,
			 "fade": fade,
			 "interpolate": interpolate
			 }


init()

while True:
	cmd = input(">")

	if cmd in whitelist.keys():
		whitelist[cmd]()
	else:
		print_err("comando inexistente")
