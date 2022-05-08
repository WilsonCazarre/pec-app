
class Value():


	def __init__(type):
		self.type = type
		self.value = None 

	def cast(value):
		
		if self.type == "int":
			self.value = int(value)
		if self.type == "float":
			self.value = float(value)
		else:
			self.value = value

		return self.value   



class Argument():

	def __init__(self,name,values,func):
		self.name = name
		self.size = size
		self.values = values
		self.function = func 

	def parse(name,string):

		search = string.split(" ")
		search_index = 0


		for word in search:
			if word == self.name:
				argument[search_index : search_index + len(self.values)]
				break
			search_index += 1


class Command():

	def __init__(self,name,arguments):
		self.name = name
		self.options = options

	def run(string):

		string = string.split("")
		pass




