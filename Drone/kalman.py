class KalmanFilter:
    def __init__(self, Q=0.01, R=0.1):
        self.Q = Q  # Process noise covariance
        self.R = R  # Measurement noise covariance
        self.x = 0.0  # Estimated value
        self.P = 1.0  # Estimation error covariance

    def update(self, measurement):
        # Prediction update
        self.P += self.Q

        # Measurement update
        K = self.P / (self.P + self.R)  # Kalman gain
        self.x += K * (measurement - self.x)
        self.P *= (1 - K)

        return self.x