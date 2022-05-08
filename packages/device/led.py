import serial as se
from serial.tools import list_ports

class LEDs:

    def __init__(self):

        self.device_type = "CH340" 
        self.serial = None 
        self.port = None
        self.is_connected = False 

        self.search_com()

    def send(self, arr = None, R = None , G = None , B = None , string = None , code = "w"):
        
        if self.is_connected:
            print(self.port)
            code = ord(code)
            out = bytearray()

            if arr:
                arr.append(code)
                out = bytearray(arr)
                del arr[-1]

            elif R and G and B:
                out = bytearray([int_R, G, B, code])

            elif string:
                string = string.split(",") 
                for numb in string:
                    out.append(int(numb))
                out.append(code)
                out = bytearray(out)

            self.serial.write(out)
        
    def set_com(self,com):
            self.serial = se.Serial(COM,9600,timeout = 1)

    def test(self):
        self.serial.write(bytearray([255,0,255,ord("s")]))

    def search_com(self):
        
        ports = list_ports.comports()
        
        try:

            if not list_ports.comports():
                raise se.SerialException
            
            for port in ports:

                if self.device_type in port.description:
                    self.serial = se.Serial(port.device,
                                               9600,
                                               timeout=1)
                    self.is_connected = True
                    self.port = port.device
                    break

                else:
                    raise se.SerialException
            

        except se.SerialException:
            self.serial = None
            self.port = None 
            self.is_connected = False

                  

test = LEDs()
test.test()
