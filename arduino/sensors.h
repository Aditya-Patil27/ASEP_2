#ifndef SENSORS_H
#define SENSORS_H

// Sensor pin definitions
const int IR_SENSOR_LEFT = 2;
const int IR_SENSOR_RIGHT = 3;
const int ULTRASONIC_TRIG = 7;
const int ULTRASONIC_ECHO = 8;

// Sensor data structure
struct SensorData {
  int leftIR;
  int rightIR;
  float distance;
};

void initializeSensors() {
  pinMode(IR_SENSOR_LEFT, INPUT);
  pinMode(IR_SENSOR_RIGHT, INPUT);
  pinMode(ULTRASONIC_TRIG, OUTPUT);
  pinMode(ULTRASONIC_ECHO, INPUT);
}

SensorData readSensors() {
  SensorData data;
  
  // Read IR sensors
  data.leftIR = digitalRead(IR_SENSOR_LEFT);
  data.rightIR = digitalRead(IR_SENSOR_RIGHT);
  
  // Read ultrasonic sensor
  digitalWrite(ULTRASONIC_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(ULTRASONIC_TRIG, LOW);
  
  long duration = pulseIn(ULTRASONIC_ECHO, HIGH);
  data.distance = duration * 0.034 / 2;  // Convert to centimeters
  
  return data;
}

#endif 