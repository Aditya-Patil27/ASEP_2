#ifndef MOTORS_H
#define MOTORS_H

// Motor control functions
void moveCar(String direction, int speed) {
  speed = constrain(speed, 0, 255);  // Ensure speed is within valid range
  
  switch(direction) {
    case "FORWARD":
      analogWrite(MOTOR_LEFT_FWD, speed);
      analogWrite(MOTOR_LEFT_BWD, 0);
      analogWrite(MOTOR_RIGHT_FWD, speed);
      analogWrite(MOTOR_RIGHT_BWD, 0);
      break;
      
    case "BACKWARD":
      analogWrite(MOTOR_LEFT_FWD, 0);
      analogWrite(MOTOR_LEFT_BWD, speed);
      analogWrite(MOTOR_RIGHT_FWD, 0);
      analogWrite(MOTOR_RIGHT_BWD, speed);
      break;
      
    case "LEFT":
      analogWrite(MOTOR_LEFT_FWD, 0);
      analogWrite(MOTOR_LEFT_BWD, speed);
      analogWrite(MOTOR_RIGHT_FWD, speed);
      analogWrite(MOTOR_RIGHT_BWD, 0);
      break;
      
    case "RIGHT":
      analogWrite(MOTOR_LEFT_FWD, speed);
      analogWrite(MOTOR_LEFT_BWD, 0);
      analogWrite(MOTOR_RIGHT_FWD, 0);
      analogWrite(MOTOR_RIGHT_BWD, speed);
      break;
  }
}

void stopCar() {
  analogWrite(MOTOR_LEFT_FWD, 0);
  analogWrite(MOTOR_LEFT_BWD, 0);
  analogWrite(MOTOR_RIGHT_FWD, 0);
  analogWrite(MOTOR_RIGHT_BWD, 0);
}

#endif 