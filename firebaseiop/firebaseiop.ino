/*
    This sketch establishes a TCP connection to a "quote of the day" service.
    It sends a "hello" message, and then prints received data.
*/
#include <FirebaseESP8266.h>
#include <ESP8266WiFi.h>

#include "DHT.h"
#define DHTPIN 12 

#define DHTTYPE DHT11 

DHT dht(DHTPIN, DHTTYPE);

#ifndef STASSID
#define STASSID "spacex"
#define STAPSK  "azharpasha"
#endif

FirebaseData fbdo;


#define lamp1 5
#define lamp2 4
#define lamp3 0
#define lamp4 2
#define FIREBASE_HOST "https://bbbaa-1503c-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "ptu0YLVr2HOeitbRAaZLkYqvK8PTdabBicnWsMMw"

const char* ssid     = STASSID;
const char* password = STAPSK;

const char* host = "namas.net";
const uint16_t port = 17;

#define PinDigital 4 // mendefinisikan pin yang digunakan adalah pin Digital
int NilaiDigital;

int aa;

void setup() {
  Serial.println(F("DHTxx test!"));

  dht.begin();
  pinMode(lamp1,OUTPUT);
  pinMode(lamp2,OUTPUT);
  pinMode(lamp3,OUTPUT);
  pinMode(lamp4,OUTPUT);
  Serial.begin(115200);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  /* Explicitly set the ESP8266 to be a WiFi-client, otherwise, it by default,
     would try to act as both a client and an access-point and could cause
     network-issues with your other WiFi-devices on your WiFi-network. */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {

  
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

Firebase.setInt(fbdo,"/plant",100);
Firebase.setFloat(fbdo, "/Temperature",t);
Firebase.setFloat(fbdo, "/Humidity",h);


  
  NilaiDigital = digitalRead(PinDigital); // membaca nilai digital

  Serial.print("Nilai Output Digital = ");
  Serial.println(NilaiDigital);
  //Aktif LOW = Jika Ada Asap Maka Nilai nya 0 jika tidak ada Asap maka nilai Nya 1

  //Proses Kirim Data
  Firebase.setInt(fbdo,"/plant",100);
  Firebase.setFloat(fbdo, "/Nilai_Asap", NilaiDigital);

if(Firebase.getString(fbdo,"/Lamp2/L1")){
  Serial.println(fbdo.dataType());
   String val = fbdo.stringData();
  Serial.println(val);
  Serial.println("\n Change the value at firebase");
  delay(100);
  if(val == "true"){
    digitalWrite(lamp1,1);
    }
  else if(val == "false"){
    digitalWrite(lamp1,0);
    
    }

}///aa
if(Firebase.getString(fbdo,"/Lamp2/L2")){
  Serial.println(fbdo.dataType());
   String val = fbdo.stringData();
  Serial.println(val);
  Serial.println("\n Change the value at firebase");
  delay(100);
  if(val == "true"){
    digitalWrite(lamp2,1);
    }
  else if(val == "false"){
    digitalWrite(lamp2,0);
    
    }

}
if(Firebase.getString(fbdo,"/Lamp2/L3")){
  Serial.println(fbdo.dataType());
   String val = fbdo.stringData();
  Serial.println(val);
  Serial.println("\n Change the value at firebase");
  delay(100);
  if(val == "true"){
    digitalWrite(lamp3,1);
    }
  else if(val == "false"){
    digitalWrite(lamp3,0);
    
    }

}
if(Firebase.getString(fbdo,"/Lamp2/L4")){
  Serial.println(fbdo.dataType());
   String val = fbdo.stringData();
  Serial.println(val);
  Serial.println("\n Change the value at firebase");
  delay(100);
  if(val == "true"){
    digitalWrite(lamp4,1);
    }
  else if(val == "false"){
    digitalWrite(lamp4,0);
    
    }

}
  else{
    Serial.println(fbdo.errorReason());
    
    }

 

}
