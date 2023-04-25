#include <Arduino.h>
#include <DHT.h> 
#include <WiFiClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

#define DHTPIN D1
#define DHTTYPE DHT11 

const char* ssid = "Gemenez_2.4ghz";
const char* password = "LifeIsHere";
const char* serverUrl = "http:192.168.1.67:8000/api/data/temphumid/";

DHT dht(DHTPIN, DHTTYPE);
DynamicJsonDocument thjson(256);

void setup() {
  Serial.begin(9600);
  dht.begin();

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
  // put your setup code here, to run once:
}

void loop() {
  delay(2000);
  float temps = dht.readTemperature();
  delay(10);
  float hums = dht.readHumidity();
  Serial.print(temps);
  Serial.print(hums);

  thjson.clear();
  thjson["temp"] = temps;
  thjson["humidity"] = hums;
  
  String jsonString;
  serializeJson(thjson, jsonString);
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
  delay(1000);
  // put your main code here, to run repeatedly:
}