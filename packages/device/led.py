import serial as se

class LEDs:

    def __init__(self,default):
        self.set_com(default)

    def send(self, arr = False, int_R = False , int_G = False , int_B = False , string = False , code = "w"):
        
        #print(arr, int_R, int_G, int_B, string, code)

        code = ord(code)
        out = bytearray()

        if arr:
            arr.append(code)
            out = bytearray(arr)
            del arr[-1]

        elif int_R and int_G and int_B:
            out = bytearray([int_R, int_G, int_B, code])

        elif string:
            string = string.split(",") 
            for numb in string:
                out.append(int(numb))
            out.append(code)
            out = bytearray(out)

        self.serial.write(out)
        
    def set_com(self,COM):
            self.serial = se.Serial(COM,9600)
            self.serial.timeout = 1
        
