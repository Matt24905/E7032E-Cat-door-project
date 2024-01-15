// CODE FOR ATTINY85 - Using Aruino UNO as ISP
// Pin named according to ATtiny85 datasheet pinout:

  int P2 = A3; 
  int P3 = A2;

  int P6 = 0;
  int P5 = 1;
  int P7 = 2;

void setup() {
  pinMode(P2, INPUT);       //  ANALOG IN - Photodiode INSIDE
  pinMode(P3, INPUT);       //  ANALOG IN - Photodiode OUTSIDE

  pinMode(P5, OUTPUT);      //  POWER IR circuit
  pinMode(P6, OUTPUT);      //  TO    Raspberry Pi
  pinMode(P7, OUTPUT);      //  START Raspberry Pi
}

void loop() {
  digitalWrite(P5, HIGH);         // Power on IR circuit
  digitalWrite(P6, LOW);          // Off
  digitalWrite(P7, LOW);          // Raspberry off

  delay(1);
  int P2_Value = analogRead(P2);    // Read indoor sensor
  int P3_Value = analogRead(P3);    // Read outdoor sensor

 if (P3_Value < 220 ) {
  digitalWrite(P6, HIGH);         // Tell Raspberry 1 = cat from outdoors
  digitalWrite(P7, HIGH);         // Start Raspberry

  delay(3000);                    // Delay 3000 = 30 seconds  
  digitalWrite(P7, LOW);          // Turn off Raspberry
  digitalWrite(P6, LOW);          // Tell Raspberry 1 = cat from outdoors
 }

else if (P2_Value < 220 ) {
    digitalWrite(P6, LOW);          // Tell Raspberry 0 = cat from indoors
    digitalWrite(P7, HIGH);         // Start Raspberry
    delay(3000);                    // Delay 30 seconds
    digitalWrite(P7, LOW);          // Turn off Raspberry
  }
   else { 
  digitalWrite(P6, LOW);
  digitalWrite(P7, LOW);  
   }

  digitalWrite(P5, LOW);            // Power off IR circuit
delay(9); 
}