#define FlamePin A0
#define TempPin A1
#define SmokePin A2

int FlameValue;
int TempValue;
int SmokeValue;
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{ 
  int FlameValue = digitalRead(FlamePin); 
  int TempValue = analogRead(TempPin);
  int SmokeValue = digitalRead(SmokePin);
  float TempCel = ( TempValue/1024.0)*500; 
  Serial.print("TEMP = "); 
  Serial.print(TempCel);
  Serial.print("*C,");
  
  if(FlameValue==HIGH)
  {
    Serial.print("Flame On,");
  }
  else
  {
    Serial.print("No Flame,");
  }
   
  if(SmokeValue==HIGH)
  {
    Serial.print("Smoke detected,");
  }
  else
  {
    Serial.print("No Smoke,");
  }

  Serial.println();
  
  delay(1000);
}
