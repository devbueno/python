# main.py
import time
import sensor
import pid_control
import motor_control

motor_control.set_motor_speeds (3300, 3000)

#user_input = input("Pressione uma tecla para iniciar o flight controller")

# Initialize the MPU6050
sensor.init_mpu()
    
# m1 ==> 3850
# m2 ==> 3965
BASEPWM_M1 = 3900
BASEPWM_M2 = 3965
# ? ver qual o pwm minimo necessário no qual o peso do braço do drone começa a ser compensado
MAX_PID_ADJUST = 400 # maximo de ajuste pid permitido

MAX_SPEED_M1 = 4550
MIN_SPEED_M1 = 3650

MAX_SPEED_M2 = 4665
MIN_SPEED_M2 = 3765

# Setpoint for the roll angle (we want to maintain 0° roll)
setpoint = 0

# Initialize PID controller with example constants
pid = pid_control.PID(kp=3.0, ki=0.00, kd=0.0)

while True:
    # Read the roll angle from the MPU6050
    roll = sensor.read_mpu()
    print("roll: ", roll)
    
    
    # Compute the PID output based on the roll angle
    pid_output = pid.compute(setpoint, roll)
    pid_output = max(min(pid_output, MAX_PID_ADJUST), -MAX_PID_ADJUST)
    print("po: ", pid_output)

    
    # Adjust motor speeds based on PID output
    # The PID output will directly influence the motor speed adjustments
    motor_speed1 = BASEPWM_M1 - pid_output  # Centered PWM value around 32768
    motor_speed2 = BASEPWM_M2 + pid_output  # Centered PWM value around 32768
    
    # Set the motor speeds (ensuring they are within the valid PWM range)
    motor_control.set_motor_speeds(min(max(motor_speed1, MIN_SPEED_M1), MAX_SPEED_M1), min(max(motor_speed2, MIN_SPEED_M2), MAX_SPEED_M2))
    
    #time.sleep(0.005)  # Delay to avoid overloading the system
    time.sleep(0.005)
