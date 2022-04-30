#include <EEPROM.h>


#define R 0 
#define G 1
#define B 2
#define RGB 3

const int OUT_PINS[RGB] = {9,10,11};

void save_preset(byte color_r, byte color_g, byte color_b){
  EEPROM.write(R,color_r);
  EEPROM.write(G,color_g);
  EEPROM.write(B,color_b);
}

void load_preset(){
    for(int i = 0; i < RGB; i++)
      analogWrite(OUT_PINS[i],EEPROM.read(i));
}


void setup() {
  for(int i = 0; i < RGB; i++)
    pinMode(OUT_PINS[i],OUTPUT);

  load_preset();
  Serial.begin(9600);
}

//  "0 0 0 c " -> R-G-B-code
//   0 1 2 3  
//  code: 
//    s = save as default
//    l = load default
//    w = write on strip

void loop() {
  if(Serial.available()){
    
      byte PWM[4]; 
      Serial.readBytes(PWM,4);
      //for(int i = 0; i < 4; i++)
      //  Serial.print(char(PWM[i]));
      //Serial.println();
      
      switch((char)PWM[3]){
        
        case 's':
          save_preset(PWM[R],PWM[G],PWM[B]);
        break; 
        
        case 'l':
          load_preset();
        break;
        
        case 'w':
          for(int i = 0; i < RGB; i++)
            analogWrite(OUT_PINS[i],PWM[i]);
        break;
      }
  }
}
