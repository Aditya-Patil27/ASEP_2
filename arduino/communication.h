#ifndef COMMUNICATION_H
#define COMMUNICATION_H

void sendSensorData(SensorData data) {
  // Format: SENSORS:leftIR,rightIR,distance
  Serial.print("SENSORS:");
  Serial.print(data.leftIR);
  Serial.print(",");
  Serial.print(data.rightIR);
  Serial.print(",");
  Serial.println(data.distance);
}

#endif 