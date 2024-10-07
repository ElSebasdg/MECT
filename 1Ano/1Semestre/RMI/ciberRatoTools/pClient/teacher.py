from lib2to3.pgen2 import driver
import sys
from croblink import *
from math import *
import xml.etree.ElementTree as ET

CELLROWS=7
CELLCOLS=14

# Constants for the controller
# PID constants

# Hysteresis for bang-bang controller
deltah = 0.05
bangvalue = 0.2

# Memory for error
e_m1 = 0.0
e_m2 = 0.0

# Memory for the control signal
u_m1 = 0.0


class PID:
    def __init__(self, Kp, Ti, Td, max_u):
        self.Kp = 20               # Proportional constant
        self.Ti = 1/h               # Integration time (set to infinity to disable I component)
        self.Td = 1 * h             # Differential time
        self.max_u = 10.0           # Saturation value for the control signal

        self.e_m1 = 0               # Error at measure t-1
        self.e_m2 = 0               # Error at measure t-2
        self.posOverLine = 0        # Process variable at the setpoint
        self.h = 0.050              # Sample time

    def update(self, posOverLine):
        # Calculate the error at the current time step
        error = posOverLine - self.posOverLine

        # Calculate the control signal
        control_signal = (
            self.Kp * posOverLine +
            (self.Kp * self.h / self.Ti) * posOverLine -
            (self.Kp * self.h / self.Ti) * self.e_m1 +
            (self.Kp * self.Td / self.h) * (posOverLine - 2 * self.e_m1 + self.e_m2)
        )

        # Update the error history
        self.e_m2 = self.e_m1
        self.e_m1 = error

        # Limit the control signal to the specified maximum value
        control_signal = max(-self.max_u, min(self.max_u, control_signal))

        # Update the process variable for the next iteration
        self.posOverLine = posOverLine

        return control_signal


class ControllerType:
    NONE = 0
    BANG = 1
    BANG2 = 2
    BANGH = 3
    P = 4
    PID = 5

activeController = ControllerType.P



class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)
        self.history = []

    # In this map the center of cell (i,j), (i in 0..6, j in 0..13) is mapped to labMap[i*2][j*2].
    # to know if there is a wall on top of cell(i,j) (i in 0..5), check if the value of labMap[i*2+1][j*2] is space or not
    def setMap(self, labMap):
        self.labMap = labMap

    def printMap(self):
        for l in reversed(self.labMap):
            print(''.join([str(l) for l in l]))
    
    def run(self):
        if self.status != 0:
            print("Connection refused or error")
            quit()

        state = 'stop'
        stopped_state = 'run'

        while True:
            self.readSensors()
            self.deconstruct()
            print(self.full)
            if self.measures.endLed:
                print(self.rob_name + " exiting")
                quit()

            if state == 'stop' and self.measures.start:
                state = stopped_state

            if state != 'stop' and self.measures.stop:
                stopped_state = state
                state = 'stop'

            if state == 'run':
                if self.measures.visitingLed==True:
                    state='wait'
                if self.measures.ground==0:
                    self.setVisitingLed(True);
                self.wander()
            elif state=='wait':
                self.setReturningLed(True)
                if self.measures.visitingLed==True:
                    self.setVisitingLed(False)
                if self.measures.returningLed==True:
                    state='return'
                self.driveMotors(0.0,0.0)
            elif state=='return':
                if self.measures.visitingLed==True:
                    self.setVisitingLed(False)
                if self.measures.returningLed==True:
                    self.setReturningLed(False)
                self.wander()


    # def calculate_new_pose(x, y, theta, inl, inr, sigma, D):
    #     # Apply IIR filter to powers
    #     outl = inl + outl_prev/2 * np.random.normal(1, sigma)
    #     outr = inr + outr_prev/2 * np.random.normal(1, sigma)
    #     # Calculate translation
    #     lin = (outl + outr)/2
    #     xt = x + lin * np.cos(theta)
    #     yt = y + lin * np.sin(theta)
    #     # Calculate rotation
    #     rot = (outr - outl)/D
    #     thetat = theta + rot
    #     # Check for collisions
    #     if collision_occurs(x, y, xt, yt):
    #         thetat = theta
    #     # Update previous powers
    #     outl_prev = outl
    #     outr_prev = outr
    #     # Return new pose
    #     return xt, yt, thetat

    # Define a method for calculating line position from sensor data
    def calculate_line_position(self, line_data):
        posOverLine = 0.0
        nActiveSensors = 0

        for i in range(len(line_data)):
            if line_data[i] == 1:
                posOverLine += i - 3  # Adjust for 0-based index
                nActiveSensors += 1

        if nActiveSensors > 0:
            posOverLine = 0.15 * posOverLine / nActiveSensors

        return posOverLine  

    def deconstruct(self):
        self.full = [int(val) for val in self.measures.lineSensor]

    def wander(self):   

        self.deconstruct()
        global e_m1, e_m2, u_m1

        if len(self.history) < 3 and len(self.history) >= 0:
            self.history.append(self.full)   
        elif len(self.history) == 3:
            self.history = self.history[1:]
            self.history.append(self.full)

        print(self.history)
        # Read sensor data and compute line position
        # small_arr = self.measures.lineSensor[1:6]
        # print("arr: ", small_arr)


        posOverLine = self.calculate_line_position(self.full)
        print("overline: ",posOverLine)



        if self.full == [0,0,0,0,0,0,0]:
            lPow = -0.13
            rPow = -0.13
            self.driveMotors(lPow, rPow)

        # for readings in self.history:
        #     middle_sensor = readings[3]  # Middle sensor
        #     neighboring_sensors = readings[6]  # Neighboring sensors (2nd to 4th elements)

        #     # Check if the middle sensor reads '0' and neighboring sensors read '1'
        #     if middle_sensor == 0 and neighboring_sensors == 1:
        #         print("Curve detected in the following sensor self.history:")
        #         print(readings)

        elif self.history[1:] == [[1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0]] or self.history[1:] == [[1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0]]: 
            print("VIRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            self.driveMotors(0, 0)


        else:
            # Implement control action depending on the type of control
            if activeController == ControllerType.NONE:
                # No feedback action
                # Controller output is the reference input
                control_signal = 0
            elif activeController == ControllerType.BANG:
                # Bang-bang control, unidirectional
                if posOverLine > 0:
                    control_signal = bangvalue
                else:
                    control_signal = 0
            elif activeController == ControllerType.BANG2:
                # Bang-bang control with bipolar output
                if posOverLine > 0:
                    control_signal = bangvalue
                elif posOverLine < 0:
                    control_signal = -bangvalue
                else:
                    control_signal = 0
            elif activeController == ControllerType.BANGH:
                # Bang-bang control with hysteresis
                if posOverLine > 0.5 * deltah:
                    control_signal = bangvalue
                elif posOverLine < -0.5 * deltah:
                    control_signal = -bangvalue
                else:
                    # If the error is within hysteresis limits, keep the previous value
                    control_signal = u_m1
                u_m1 = control_signal

            elif activeController == ControllerType.P:
                # Proportional control
                control_signal = 1.0 * posOverLine

            elif activeController == ControllerType.PID:
                # Compute control signal using PID control principles
                control_signal = pid_controller.update(posOverLine)


                # Store values for the next iterations
                e_m2 = e_m1
                e_m1 = posOverLine
                u_m1 = control_signal

                # Clip the control signal to avoid saturation
                if control_signal > max_u:
                    control_signal = max_u
                if control_signal < -max_u:
                    control_signal = -max_u

            # Apply control signal to adjust robot behavior


            print("sinal controlo: ", control_signal)


            lPow = 0.15 + control_signal
            rPow = 0.15 - control_signal

            self.driveMotors(lPow, rPow)

            print("(", lPow, ",", rPow, ")")

class Map():
    def __init__(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        
        self.labMap = [[' '] * (CELLCOLS*2-1) for i in range(CELLROWS*2-1) ]
        i=1
        for child in root.iter('Row'):
           line=child.attrib['Pattern']
           row =int(child.attrib['Pos'])
           if row % 2 == 0:  # this line defines vertical lines
               for c in range(len(line)):
                   if (c+1) % 3 == 0:
                       if line[c] == '|':
                           self.labMap[row][(c+1)//3*2-1]='|'
                       else:
                           None
           else:  # this line defines horizontal lines
               for c in range(len(line)):
                   if c % 3 == 0:
                       if line[c] == '-':
                           self.labMap[row][c//3*2]='-'
                       else:
                           None
               
           i=i+1


rob_name = "pClient1"
host = "localhost"
pos = 1
mapc = None

for i in range(1, len(sys.argv),2):
    if (sys.argv[i] == "--host" or sys.argv[i] == "-h") and i != len(sys.argv) - 1:
        host = sys.argv[i + 1]
    elif (sys.argv[i] == "--pos" or sys.argv[i] == "-p") and i != len(sys.argv) - 1:
        pos = int(sys.argv[i + 1])
    elif (sys.argv[i] == "--robname" or sys.argv[i] == "-r") and i != len(sys.argv) - 1:
        rob_name = sys.argv[i + 1]
    elif (sys.argv[i] == "--map" or sys.argv[i] == "-m") and i != len(sys.argv) - 1:
        mapc = Map(sys.argv[i + 1])
    else:
        print("Unkown argument", sys.argv[i])
        quit()

if __name__ == '__main__':
    rob=MyRob(rob_name,pos,[0.0,60.0,-60.0,180.0],host)
    if mapc != None:
        rob.setMap(mapc.labMap)
        rob.printMap()
    
    rob.run()