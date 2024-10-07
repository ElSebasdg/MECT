class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)

        # Initialize a buffer to store sensor readings for smoothing
        self.sensor_buffer = [['0', '0', '0', '0', '0', '0', '0'] for _ in range(5)]
        self.buffer_index = 0

    # ... Other methods ...

    def readSensors(self):
        # Read sensor data
        super().readSensors()

        # Update the sensor buffer with the latest reading
        self.sensor_buffer[self.buffer_index] = self.measures.lineSensor

        # Increment the buffer index and wrap around if needed
        self.buffer_index = (self.buffer_index + 1) % 5

        # Calculate the moving average of sensor readings
        smoothed_reading = ['0', '0', '0', '0', '0', '0', '0']
        for i in range(7):
            sum_value = sum(int(self.sensor_buffer[j][i]) for j in range(5))
            smoothed_reading[i] = '1' if sum_value >= 3 else '0'  # Adjust the threshold as needed

        # Update the robot's measures with the smoothed reading
        self.measures.lineSensor = smoothed_reading

    # ... Other methods ...
