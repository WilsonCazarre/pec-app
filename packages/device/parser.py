from lb import LoopBack
from led import LEDs
import function

#light and sound are used in all functions without exption
#because of this fact, I've choosen to make them global variables

#light represents the led strip
#sound represents the computer's speaker

light = LEDs()
sound = LoopBack(0)


#sound setup commands
def sound_input_list():
	print(LoopBack.input_list())

def sound_current_input():
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

#STATIC FUNCTIONS
# if code == "w" -> writes 
# if code == "l" -> loads (when loading R,G,B are arbitrary)
# if code == "s" -> saves
# dafault code 	 -> "w"
def static_send_color(R = 0, G = 0, B = 0, code = "w"):
	light.send(arr = [R,G,B], code = code)

#TIMED FUNCTIONS
def timed_fade(velocity_R, velocity_G, velocity_B):
	function.Fade(light, velocity_R, velocity_G, velocity_B).launch()

def timed_blink():
	pass

#DINAMIC FUNCTIONS 
def dinamic_curvy(curviness_R, curviness_G, curviness_B, dim):
	function.Curvy(light, sound, curviness_R, curviness_G, curviness_B, dim).launch()

def dinamic_interpolate(points, color, curviness, dim):
	function.Interpolate(light,sound,points,color,curviness,dim).launch()


#MAIN LOOP
light_current_COM() # debbug
while True:
	exec(input())
