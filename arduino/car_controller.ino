#include "motors.h"
#include "sensors.h"
#include "communication.h"

// Pin Definitions
const int MOTOR_LEFT_FWD = 5;
const int MOTOR_LEFT_BWD = 6;
const int MOTOR_RIGHT_FWD = 9;
const int MOTOR_RIGHT_BWD = 10;
const int MOTOR_ENABLE = 4;

// Serial Communication
const int BAUD_RATE = 9600;

void setup() {
  // Initialize serial communication
  Serial.begin(BAUD_RATE);
  
  // Initialize motor pins
  pinMode(MOTOR_LEFT_FWD, OUTPUT);
  pinMode(MOTOR_LEFT_BWD, OUTPUT);
  pinMode(MOTOR_RIGHT_FWD, OUTPUT);
  pinMode(MOTOR_RIGHT_BWD, OUTPUT);
  pinMode(MOTOR_ENABLE, OUTPUT);
  
  // Enable motors
  digitalWrite(MOTOR_ENABLE, HIGH);
  
  // Initialize sensors
  initializeSensors();
}

void loop() {
  // Check for serial commands
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
  
  // Read sensor data
  SensorData sensorData = readSensors();
  
  // Send sensor data back to main controller
  sendSensorData(sensorData);
  
  // Small delay to prevent overwhelming the serial buffer
  delay(50);
}

void processCommand(String command) {
  // Parse and execute commands from main controller
  if (command.startsWith("MOVE:")) {
    // Format: MOVE:direction:speed
    int colonIndex = command.indexOf(':');
    String direction = command.substring(5, colonIndex);
    int speed = command.substring(colonIndex + 1).toInt();
    
    moveCar(direction, speed);
  }
  else if (command == "STOP") {
    stopCar();
  }
} 