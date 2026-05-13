#include <ESP32Servo.h>



// SERVO OBJECTS

Servo panServo;
Servo tiltServo;



// PIN DEFINITIONS

#define PAN_PIN        21
#define TILT_PIN       22

#define LIMIT_SWITCH   32
#define RELAY_PIN      25
#define LED_PIN        26



// SERVO STATE VARIABLES

float pan  = 90;
float tilt = 90;
float targetPan  = 90;
float targetTilt = 90;
float smooth = 0.18;



// FIRING STATE

bool firing = false;



// SETUP

void setup()
{
    Serial.begin(115200);

    panServo.attach(PAN_PIN);
    tiltServo.attach(TILT_PIN);

    pinMode(LIMIT_SWITCH, INPUT_PULLUP);
    pinMode(RELAY_PIN, OUTPUT);
    pinMode(LED_PIN, OUTPUT);

    // RELAY OFF (active LOW module)
    digitalWrite(RELAY_PIN, HIGH);
    digitalWrite(LED_PIN, LOW);

    panServo.write(90);
    tiltServo.write(90);

    delay(500);

    // Tilt homing safety
    while (digitalRead(LIMIT_SWITCH) == LOW)
    {
        tilt += 2;
        tiltServo.write(tilt);
        delay(30);
    }

    tilt = 90;
    tiltServo.write(tilt);
}



// MAIN LOOP

void loop()
{
    readSerialCommands();
    updateServoMotion();
    handleLimitProtection();
    updateServos();
    handleRelay();
}



// SERIAL COMMAND PROCESSING

void readSerialCommands()
{
    if (!Serial.available()) return;

    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "FIRE")
    {
        firing = true;
        return;
    }

    if (cmd == "STOP")
    {
        firing = false;
        return;
    }

    int comma = cmd.indexOf(',');

    if (comma > 0)
    {
        targetPan  = cmd.substring(0, comma).toInt();
        targetTilt = cmd.substring(comma + 1).toInt();

        targetPan  = constrain(targetPan,  0, 180);
        targetTilt = constrain(targetTilt, 10, 170);
    }
}



// SERVO SMOOTH MOTION

void updateServoMotion()
{
    pan  += (targetPan  - pan)  * smooth;
    tilt += (targetTilt - tilt) * smooth;
}



// LIMIT SWITCH PROTECTION

void handleLimitProtection()
{
    if (digitalRead(LIMIT_SWITCH) == LOW)
    {
        if (targetTilt < tilt)
        {
            tilt = targetTilt;
        }
    }
}



// WRITE SERVOS

void updateServos()
{
    panServo.write(pan);
    tiltServo.write(tilt);
    delay(12);
}



// RELAY CONTROL

void handleRelay()
{
    if (firing)
    {
        // ACTIVE LOW RELAY → LOW = ON
        digitalWrite(RELAY_PIN, HIGH);
        digitalWrite(LED_PIN, HIGH);
    }
    else
    {
        digitalWrite(RELAY_PIN, LOW);
        digitalWrite(LED_PIN, LOW);
    }
}
