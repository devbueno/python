# pid_control.py
class PID:
    def __init__(self, kp, ki, kd, max_integral=100):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0
        self.max_integral = max_integral

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value

        
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative
