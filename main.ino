int buttonPin = 12;
int ledPin = 13;

void setup() {
	pinMode(ledPin, OUTPUT);
	pinMode(buttonPin, INPUT);
}

void loop() {
	int val = digitalRead(buttonPin);
	digitalWrite(ledPin, val);
}
