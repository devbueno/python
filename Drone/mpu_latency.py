import machine
import ustruct
from machine import I2C, Pin
import math
from kalman import KalmanFilter
import time
import shut

MPU_ADDR = 0x68

# Set up the I2C bus
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Kalman filter instance for roll angle
kalman_roll = KalmanFilter(Q=0.01, R=0.1)

# Profiling setup
log = []
_read_count = 0
MAX_READS = 200

def init_mpu():
    i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')  # Wake the MPU6050

def read_mpu():
    global _read_count

    start = time.ticks_us()

    # Read the accelerometer data (X, Y, Z)
    accel_data = i2c.readfrom_mem(MPU_ADDR, 0x3B, 6)
    accel_x, accel_y, accel_z = ustruct.unpack('>hhh', accel_data)

    # Convert to g
    accel_x /= 16384.0
    accel_y /= 16384.0
    accel_z /= 16384.0

    # Calculate raw roll angle
    roll_raw = math.atan2(accel_y, accel_z) * (180 / math.pi)

    # Apply Kalman filter
    roll_filtered = kalman_roll.update(roll_raw)

    # Profiling logic (only for first MAX_READS samples)
    if _read_count < MAX_READS:
        elapsed = time.ticks_diff(time.ticks_us(), start)
        log.append(elapsed)
        _read_count += 1

        if _read_count == MAX_READS:
            avg = sum(log) / len(log)
            print("Sensor profiling complete:")
            print("Average time (us):", avg)
            print("Min:", min(log), "Max:", max(log))

    return roll_filtered
