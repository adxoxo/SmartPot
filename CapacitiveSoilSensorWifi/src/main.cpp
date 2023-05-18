#include <Arduino.h>
#include <WiFiClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

// Simple code for Measuring Voltage from
// Capacitive soil moisture sensor
//
int soil_pin = A0; // AOUT pin on sensor
float air = 640;  // y-intercept
float water = 313;
float soilMoisture, voltageReading = 0;

const char* ssid = "Gemenez_2.4ghz";
const char* password = "LifeIsHere";
const char* serverUrl = "http://192.168.1.67:8000/api/data/soil";

DynamicJsonDocument soiljson(1024);

void setup() {
  Serial.begin(9600); // serial port setup
  analogReference(EXTERNAL); // set the analog reference to 3.3V

  Serial.println();
  Serial.println();
  Serial.print("Connecting to");
  Serial.println(ssid);

  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi Connected");
}

void loop() {
  voltageReading = analogRead(soil_pin);
  
  soilMoisture = map(voltageReading, air, water, 0, 100);
  Serial.print("Voltage reading: ");
  Serial.print(voltageReading);
  Serial.print(" V");

  Serial.print("Soil moisture content: ");
  Serial.print(soilMoisture);
  Serial.println(" %");
  
  soiljson.clear();
  soiljson["voltage"] = voltageReading;
  soiljson["moisture"] = soilMoisture;

  String jsonString;
  serializeJson(soiljson, jsonString);
  Serial.println(jsonString);

  WiFiClient client;
  HTTPClient http;

  http.begin(client, serverUrl);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(jsonString);

  if (httpResponseCode > 0){
    Serial.print("HTTP Response Code: ");
    Serial.print("httpResponseCode");
  } else {
    Serial.print("Error sending data to API: ");
    Serial.println(httpResponseCode);
  }
  http.end();

  delay(5000);
}

