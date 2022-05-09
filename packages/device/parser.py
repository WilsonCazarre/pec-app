

from lb import LoopBack
from led import LEDs
import func

#light and sound are used in all functions without exption
#because of this fact, I've choosen to make them global variables

#light represents the led strip
#sound represents the computer's speaker

light = LEDs()
sound = LoopBack(0)


#sound setup commands
def sound_input_list():
	print(LoopBack.input_list())

def sound_current_speaker():
	print(sound.speaker)

def sound_set_input(number):
	sound.set_input(number)


#light setup commands
def light_input_list():
	print(light.list_ports())

def light_current_COM():
	print(light.port)

def light_set_input(string):
	light.set_com(string)

def light_search_input():
	light.search_com()

#static functions
# if code == "w" -> writes 
# if code == "l" -> loads (when loading R,G,B are arbitrary)
# if code == "s" -> saves
# dafault code 	 -> "w"
def static_send_color(R = 0, G = 0, B = 0, code = "w"):
	light.send(arr = [R,G,B], code = code)

light_current_COM()
while True:
	exec(input())