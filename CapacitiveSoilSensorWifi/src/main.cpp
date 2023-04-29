#include <Arduino.h>

// Simple code for Measuring Voltage from
// Capacitive soil moisture sensor
//
int soil_pin = A0; // AOUT pin on sensor
float a = -3.3;  // y-intercept
float b = 1.0;
float soilMoisture, voltageReading = 0;

void setup() {
  Serial.begin(9600); // serial port setup
  analogReference(EXTERNAL); // set the analog reference to 3.3V
}

void loop() {
  voltageReading = analogRead(soil_pin);
  
  soilMoisture = a + b * voltageReading;
  Serial.print("Voltage reading: ");
  Serial.print(voltageReading);
  Serial.print(" V");

  Serial.print("Soil moisture content: ");
  Serial.print(soilMoisture);
  Serial.println(" %");
  delay(5000);
}

