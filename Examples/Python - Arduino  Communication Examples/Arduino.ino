// Modifyy this no so that each Arduino can be identified uniquely
#define Arduino_no  1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(5000);
  //print "Hello from Arduino No. 1" on serial output every 5 seconds
  Serial.println("Hello from Arduino No."+ Arduino_no);
}
