#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "async.h"

// constansts
const int PRESSED = 1;
const int RELEASED = 0;
const unsigned long debounceTime = 50;

void blink();
void ledON();
void ledOFF();

Async asyncEngine = Async();

static unsigned long lastOn = millis();

void setup()
{
  Serial.begin(115200);
  pinMode(D4, OUTPUT);

  digitalWrite(D4, HIGH);
  // connectToWifi();
}

void loop()
{
  asyncEngine.run();

  if (Serial.available() > 0)
  {
    // read incoming byte
    int incomingByte = Serial.read();

    // if get 0 then turn off led
    if (incomingByte == RELEASED)
    {
      ledOFF();
    }
    else if (incomingByte == PRESSED)
    {
      // if the key is holding, the light will not be flickering
      // the light will just on
      if ((millis() - lastOn) < debounceTime)
      {
        ledON();
      }
      // if the key is pressed, the light will on
      else
      {
        ledON();
        // blink();
      }

      lastOn = millis();
    }
  }

  if ((millis() - lastOn) > 1000)
  {
    ledOFF();
  }
}

void ledON()
{
  digitalWrite(D4, LOW);
}

void ledOFF()
{
  digitalWrite(D4, HIGH);
}

void blink()
{
  ledON();

  // TO OFF
  asyncEngine.setTimeout(ledOFF, 10);
}