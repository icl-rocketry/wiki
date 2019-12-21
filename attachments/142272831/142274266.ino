#include <SPI.h>
#include <LoRa.h>

#define ss 5
#define rst 14
#define dio0 2
#define syncWord 0xF4

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

}

void loop() {
  // try to parse packet
  static unsigned int counter = 0;
  
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");

    // read packet
    char pktContents;
    while (LoRa.available()) {
      pktContents=(char)LoRa.read();
    }
    
    // Read package count from content
    char *pointer = &pktContents;
    unsigned int pktCounter=(int)(pointer[12])*10+(int)(pointer[13]);
    
    if (pktCounter > counter+1) {
      Serial.print(pktCounter-counter);
      Serial.println(" packets were lost!");
    }
    counter=pktCounter;
    
    Serial.print(pktContents);
    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}
