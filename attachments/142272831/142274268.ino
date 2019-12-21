/*
Slightly modified version of the arduino-LoRa example code.
Differences include use of a sync word, modified data packet,
definition of spreading factor and transmit power being set to maximum.

Written by Daniele Valentino Bella for ICLR
November 2019
*/

#include <SPI.h>
#include <LoRa.h>

#define ss 5
#define rst 14
#define dio0 2
#define txPower 20
#define syncWord 0xF4
#define spreadingFactor 12

int counter = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("LoRa Sender");

  LoRa.setPins(ss, rst, dio0);
  
  while (!LoRa.begin(866E6)) {
    Serial.println("Starting LoRa failed!");
    delay(1000);
    Serial.println("Trying again...");
  }
  Serial.println("LoRa succesfully initialised!");

  LoRa.setTxPower(txPower);
  LoRa.setSyncWord(syncWord);
  LoRa.setSpreadingFactor(spreadingFactor);
}

void loop() {
  Serial.print("Sending packet: ");
  Serial.println(counter);

  // send packet
  LoRa.beginPacket();
  LoRa.print("Data Packet ");
  LoRa.print(counter);
  LoRa.endPacket();

  counter++;

  delay(1000);
}
