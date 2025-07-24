# motor_control.py
from machine import Pin, PWM

# Setup PWM pins for the ESCs
motor1 = PWM(Pin(10))  # Motor 1
motor2 = PWM(Pin(11))  # Motor 2

motor1.freq(50)  # Set frequency to 50Hz (typical for ESCs)
motor2.freq(50)

# Function to set motor speeds
def set_motor_speeds(speed1, speed2):
    motor1.duty_u16(int(speed1))  # Speed 1 (PWM)
    motor2.duty_u16(int(speed2))  # Speed 2 (PWM)