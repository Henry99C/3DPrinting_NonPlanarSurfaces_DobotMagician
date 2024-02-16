#include <PID_v1.h>

double Setpoint;
double Input;
double Output;
double kp = 24.92, ki = 2.45, kd = 67.29;

//Cual es el tiempo de muestreo de marlin, como lo obtengo?
double SampleTime = 1000;

PID myPID(&Input, &Output, &Setpoint, kp, ki, kd, DIRECT);

int EThermistorPin = 0;
float EVo;
float ETc;

const float LUT[][2] = {
  {   23, 300 },
  {   25, 295 },
  {   27, 290 },
  {   28, 285 },
  {   31, 280 },
  {   33, 275 },
  {   35, 270 },
  {   38, 265 },
  {   41, 260 },
  {   44, 255 },
  {   48, 250 },
  {   52, 245 },
  {   56, 240 },
  {   61, 235 },
  {   66, 230 },
  {   71, 225 },
  {   78, 220 },
  {   84, 215 },
  {   92, 210 },
  {  100, 205 },
  {  109, 200 },
  {  120, 195 },
  {  131, 190 },
  {  143, 185 },
  {  156, 180 },
  {  171, 175 },
  {  187, 170 },
  {  205, 165 },
  {  224, 160 },
  {  245, 155 },
  {  268, 150 },
  {  293, 145 },
  {  320, 140 },
  {  348, 135 },
  {  379, 130 },
  {  411, 125 },
  {  445, 120 },
  {  480, 115 },
  {  516, 110 },
  {  553, 105 },
  {  591, 100 },
  {  628,  95 },
  {  665,  90 },
  {  702,  85 },
  {  737,  80 },
  {  770,  75 },
  {  801,  70 },
  {  830,  65 },
  {  857,  60 },
  {  881,  55 },
  {  903,  50 },
  {  922,  45 },
  {  939,  40 },
  {  954,  35 },
  {  966,  30 },
  {  977,  25 },
  {  985,  20 },
  {  993,  15 },
  {  999,  10 },
  { 1004,   5 },
  { 1008,   0 },
  { 1012,  -5 },
  { 1016, -10 },
  { 1020, -15 }
};

void setup() {
  Serial.begin(115200);
  myPID.SetMode(AUTOMATIC);
  myPID.SetTunings(kp, ki, kd);
  myPID.SetSampleTime(SampleTime);
  Setpoint = 0;
}

void loop() {
  //LECTURA DE TEMPERATURA
  EVo = analogRead(EThermistorPin);
  
  for (int i=0; i<64;i++){
     
    if(EVo >= LUT[i][0] && EVo <= LUT[i+1][0]){
          ETc = (((LUT [i+1][1] - LUT [i-1][1])/(LUT [i+1][0] - LUT [i-1][0]))*(EVo-LUT [i+1][0]))+ LUT [i+1][1];
    }
    
  }

  //MODIFICAR SETPOINT
  if(Serial.available()){
    Setpoint = Serial.parseInt();
  }
  
  //CONTROL DE TEMPERATURA
  Input = ETc;
  myPID.Compute();
  analogWrite(3, 255-Output);

  //Serial.println(ETc);
  
  Serial.println(String(ETc,2)+","+String(Setpoint,2));
  delay(250);
}
