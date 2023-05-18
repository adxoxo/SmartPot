#include <Arduino.h>
#include <BH1750.h>

// put function declarations here:
int myFunction(int, int);
BH1750 lightSensor;

void setup() {
  // put your setup code here, to run once:
  int result = myFunction(2, 3);
  Serial.begin(115200);
  lightSensor.begin();
}

void loop() {
  uint16_t lux = lightSensor.readLightLevel();
  Serial.print("Light Intensity: ");
  Serial.print(lux);
  Serial.println(" lx");
  delay(10000); // Wait for 1 second before the next reading
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}