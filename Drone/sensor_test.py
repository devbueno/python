# sensor.py
import machine
import ustruct
from machine import I2C, Pin
import math
from kalman import KalmanFilter
import shut
import time

MPU_ADDR = 0x68

# Set up the I2C bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Kalman filter instance for roll angle
#Tweak Q and R if needed:
#More noise? Increase R.
#Want smoother but slower response? Lower Q.
kalman_roll = KalmanFilter(Q=0.01, R=0.1)


def init_mpu():
    i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')  # Wake the MPU6050

def read_mpu():
    # Read the accelerometer data (X, Y, Z)
    accel_data = i2c.readfrom_mem(MPU_ADDR, 0x3B, 6)  # 6 bytes for accelerometer data
    accel_x, accel_y, accel_z = ustruct.unpack('>hhh', accel_data)

    # Convert to 'g' (gravitational force)
    accel_x /= 16384.0
    accel_y /= 16384.0
    accel_z /= 16384.0
    
    # Calculate roll angle (assuming the drone is mostly flat on the X axis)
    roll_raw = math.atan2(accel_y, accel_z) * (180 / math.pi)  # Roll angle in degrees

    roll_filtered = kalman_roll.update(roll_raw)
    print(roll_filtered)
    return roll_filtered

init_mpu()
while True:
     read_mpu()
     time.sleep(0.1)

