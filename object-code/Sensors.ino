                                   #include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <ArduinoJson.h>

// Affectation des broches

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10
#define SEALEVELPRESSURE_HPA (1013.25)
#define AN A1 // broche de sortie du module

StaticJsonBuffer<200> jsonBuffer;
Adafruit_BME280 bme; // I2C
int valeur;
int feu;
int echantillons = 10;
unsigned long sum = 0;
unsigned long avg;
JsonObject& root = jsonBuffer.createObject();
void setup(){
  unsigned status;

  Serial.begin(9600); // initialisation de la liaison série
  Serial1.begin(9600); // Envoi des données sur serial1
  status = bme.begin(0x76);  

}

void loop() {
  //printValues();
  sendjson();
  feu = isThereFire(); 
  Serial.println(feu);
  if (feu == 1){
      Serial.println("Fire = Yes");
    }
  else{
      Serial.println("Fire = No");
    }
  delay(3000);
  

}
  



bool isThereFire(){
  int avg;
    for (int i=0; i < 10; i++){
    valeur = analogRead(AN); // conversion AN
    sum = sum + valeur; // somme de 10 échantillons
    avg = sum / echantillons; // calcul de la moyenne de 10 échantillons
    delay(10);
    }
    sum = 0;
    if (avg> 300){return 1;}
    
    else{return 0;}
}

void sendjson(){
    
    root["temperature"] = bme.readTemperature();
    root["pression"] = bme.readPressure() / 100.0F;
    root["altitude"] = bme.readAltitude(SEALEVELPRESSURE_HPA);
    root["humidite"] = bme.readHumidity();
    root["feu"] = feu;
    
    root.printTo(Serial1);

}


void printValues() {
    Serial.print("Temperature = ");
    Serial.print(bme.readTemperature());
    Serial.println(" *C");

    Serial.print("Pressure = ");

    Serial.print(bme.readPressure() / 100.0F);
    Serial.println(" hPa");

    Serial.print("Approx. Altitude = ");
    Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.println(" m");

    Serial.print("Humidity = ");
    Serial.print(bme.readHumidity());
    Serial.println(" %");
    
/*    Serial.print("Fire = ");
    Serial.print(appelle fonction flamme);
    Serial.println("0/1");*/

    Serial.println();
    

}


