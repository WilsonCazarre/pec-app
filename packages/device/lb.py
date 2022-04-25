import soundcard as sc

class LoopBack():

    def __init__(self,default):
        self.speaker = sc.all_microphones(include_loopback = True)[default]

    def input_list():
        out = ""
        i = 0
        
        for device in sc.all_microphones(include_loopback = True):
            out += str(i) + " - "+ str(device) + "\n"  
            i += 1

        return  out 
	
    def set_input(number):
        self.speaker = sc.all_microphones(include_loopback = True)[number]
        
    def listen(self):
    
        with self.speaker.recorder(samplerate=44100) as lb:
            while True:
                rtrn = lb.record(numframes=None)

                if(rtrn.size == 0):
                    continue
                else:
                    return rtrn[0:,0]



