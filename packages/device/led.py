#this is a hardware class, meaning it is used to control physical hardware
#this class talks to the arduino module via COM port

#the messages sent have the format:
#   [0 - 255] , [0 - 255] , [0 - 255] , ['w' , 'l' , 's']
#       R           G           B           code/action 

#code/action cheat sheet:
# w -> dinamicaly writes the RGB value on the strip
# l -> loads the default RGB value from the arduino's EEPROM
# s -> saves a default RGB to the arduino's EEPROM


import serial as se
from serial.tools import list_ports

class LEDs:

    def __init__(self):

        self.device_type = "CH340" 
        self.serial = None 
        self.port = None
        self.is_connected = False 

        self.search_com()

    #sends a message 
    def send(self, arr = None, R = None , G = None , B = None , string = None , code = "w"):
        
        if self.is_connected:
            code = ord(code)
            out = bytearray()

            if arr:
                arr.append(code)
                out = bytearray([x if x < 256 else 255 for x in arr])
                del arr[-1]

            elif R and G and B:
                out = bytearray([R, G, B, code])

            elif string:
                string = string.split(",") 
                for numb in string:
                    out.append(int(numb))
                out.append(code)
                out = bytearray(out)

            self.serial.write(out)
        
    #manualy sets the COM
    def set_com(self,com):
        
        try:
            self.serial = se.Serial(COM,9600,timeout = 1)
        
        except se.SerialException:
            self.serial = None
            self.port = None 
            self.is_connected = False


    #lists the COM ports available 
    def list_ports(self):

        ports = list_ports.comports()
        for port in ports:
            print(port.device)

    #auto conects to the COM
    def search_com(self):
        
        ports = list_ports.comports()
        
        try:

            if not list_ports.comports():
                raise se.SerialException
            
            for port in ports:

                if self.device_type in port.description:
                    self.serial = se.Serial(port.device,9600)
                    self.serial.timeout = 1
                    self.is_connected = True
                    self.port = port.device
                    break

                else:
                    raise se.SerialException
            

        except se.SerialException:
            self.serial = None
            self.port = None 
            self.is_connected = False

                  

