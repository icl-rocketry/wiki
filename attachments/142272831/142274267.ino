/*
Slightly modified version of the arduino-LoRa example code.
Differences include use of a sync word, modified data packet
and setting of a spreading factor.

Written by Daniele Valentino Bella for ICLR
November 2019
*/

#include <SPI.h>
#include <LoRa.h>

#define ss 5
#define rst 14
#define dio0 2
#define syncWord 0xF4
#define spreadingFactor 12

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("LoRa Receiver");

  LoRa.setPins(ss, rst, dio0);
  
  while (!LoRa.begin(866E6)) {
    Serial.println("Starting LoRa failed!");
    delay(1000);
    Serial.println("Trying again...");
  }
  Serial.println("LoRa succesfully initialised!");

  LoRa.setSyncWord(syncWord);
  LoRa.setSpreadingFactor(spreadingFactor);
}

void loop() {
 // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");

    // read packet
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }

    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}
