const int north = 8;
const int south = 9;
const int east = 11;
const int west = 10;

int state = 1; //For the idle function
char rxChar = 0;

void setup() {
  pinMode(north, OUTPUT);
  pinMode(south, OUTPUT);
  pinMode(east, OUTPUT);
  pinMode(west, OUTPUT);

  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  if(Serial.available() > 0) {
    
    rxChar = Serial.read();
    Serial.flush();
    
    switch (rxChar) {
    
      case 'n':                        
        if (digitalRead(north) == LOW){      
          digitalWrite(north, HIGH);    
        }
        break;
  
      case 's':                        
        if (digitalRead(south) == LOW){     
          digitalWrite(south, HIGH);    
        }
        break;
          
      case 'e':                         
        if (digitalRead(east) == LOW){      
          digitalWrite(east, HIGH);
        }
        break;

      case 'w':                          
        if (digitalRead(west) == LOW){   
          digitalWrite(west, HIGH);
        }
        break;

      case 'a':                          
        if (digitalRead(north) == LOW || digitalRead(east) == LOW){   
          digitalWrite(north, HIGH);
          digitalWrite(east, HIGH);
        }
        break;

      case 'b':                          
        if (digitalRead(south) == LOW || digitalRead(east) == LOW){   
          digitalWrite(south, HIGH);
          digitalWrite(east, HIGH);
        }
        break;

      case 'c':                          
        if (digitalRead(south) == LOW || digitalRead(west) == LOW){   
          digitalWrite(south, HIGH);
          digitalWrite(west, HIGH);
        }
        break;

      case 'd':                          
        if (digitalRead(north) == LOW || digitalRead(west) == LOW){   
          digitalWrite(north, HIGH);
          digitalWrite(west, HIGH);
        }
        break;
        
      case 'p':
        Serial.write("Pong!\n");
        break;
    }
    delay(20);
    
  } else {

    allOff();
    //idle();
    
  }
}

void allOff() {
  digitalWrite(north, LOW);
  digitalWrite(south, LOW);
  digitalWrite(east, LOW);
  digitalWrite(west, LOW);
}

void idle() {
  
  digitalWrite(north, state);
  delay(500);
  digitalWrite(south, state);
  delay(500);
  digitalWrite(east, state);
  delay(500);
  digitalWrite(west, state);
  delay(500);
  
  if (state) {
    state = 0;
  } else {
    state = 1;
  }
  
}
