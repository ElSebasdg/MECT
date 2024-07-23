from lib2to3.pgen2 import driver
import sys
from croblink import *
from math import *
import xml.etree.ElementTree as ET

MAX_MOTOR = 0.10

CELLROWS=7
CELLCOLS=14


class PID():
    def __init__(self, kp, ki, kd):
        # PID tunning parameters
        self.kp = kp
        self.ki = ki
        self.kd = kd
        # PID measurements
        self.error = 0
        self.last_error = 0
        self.integral = 0
        self.derivative = 0
        self.output = 0
        # max motor power

    # return the current computed motor power
    def current_speed(self):
        return self.output

    # get motor power based on PID controller logic
    #                                measurement    setpoint    
    def pid_output(self, current_value, target_value):
        self.error = target_value - current_value

        proportionalTerm = self.kp * self.error

        self.integral += self.error
        self.derivative = self.error - self.last_error
        self.last_error = self.error

        self.output = proportionalTerm + self.ki * self.integral + self.kd * self.derivative
        # clip control to avoid saturation
        if self.output > MAX_MOTOR:
            self.output = MAX_MOTOR
        if self.output < -MAX_MOTOR:
            self.output = -MAX_MOTOR

        return self.output




class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)
        self.controller = PID(0.0025, 0.0001, 0.00001)
        self.ln_left = None
        self.ln_center = None

        self.ln_right = None
        self.full = None
        self.small_arr = None
        self.pow = 0

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
            print(self.small_arr)
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

    def deconstruct(self):
        self.ln_left = [int(val) for val in self.measures.lineSensor[0:2]]
        self.ln_center = [int(val) for val in self.measures.lineSensor[2:5]]
        self.ln_right = [int(val) for val in self.measures.lineSensor[5:7]]
        self.full = [int(val) for val in self.measures.lineSensor]
        self.small_arr = [int(val) for val in self.measures.lineSensor[1:6]]


    def compute_rotation_speed(self):
        # Define weights for each sensor. The weights increase as the sensor gets further from the center.
        weights = [-0.80, -0.40, 0.60, 0.40, 0.80]

        # Calculate the weighted sum of the sensor readings.
        weighted_sum = sum(sensor * weight for sensor, weight in zip(self.small_arr, weights))

        # Calculate the sum of the weights for the sensors that are detecting the line.
        active_weights = sum(weight for sensor, weight in zip(self.small_arr, weights) if sensor == 1)
        
        # Calculate the average weighted sensor reading.
        if active_weights != 0:
            rotation_speed = 0.08 * weighted_sum / active_weights
        else:
            rotation_speed = 0

        return rotation_speed


        
        # if small_arr ==  ['0','1','1','1','0']:   # Correct to LEFT
        #     #self.driveMotors(0.15,0.15)
        #     print("RETO")

        # #                        l    r
        # elif small_arr == ['0','0','0','0','0']: # Correct course BACK
        #     self.driveMotors(-0.7,-0.7)
        #     print("PA TRAS")


        # elif small_arr == ['1','1','1','0','0']:  # Correct course RIGTH
        #     self.driveMotors(0.10,0.8)  
        # elif small_arr == ['0','0','1','1','1']: # Correct course LEFT
        #     self.driveMotors(0.08,0.10)
        # elif small_arr == ['0','1','0','0','0']:  # Correct course RIGTH
        #     self.driveMotors(0.08,0.10) 


        # elif small_arr == ['0','0','1','1','0']: # Rotate all left
        #     self.driveMotors(0,0.13)

        # elif small_arr == ['0','1','1','0','0']: # Rotate all Rigth
        #     self.driveMotors(0.13,0)

        # #                       ['0','1','0','0','0','0','0']
        # elif small_arr[0] == '1' and small_arr[4] == '0': # Rotate softly left
        #     self.driveMotors(0.08,0.10)
        # #                       ['0','0','0','0','0','0','1']
        # elif small_arr[0] == '0' and small_arr[4] == '1': # Rotate softly right
        #     self.driveMotors(0.10,0.08)
        # else:
        #     self.driveMotors(0.15,0.15)

    def wander(self):
        self.deconstruct()
        if self.small_arr == [0,0,0,0,0]:
            print("pa tras")
            left_power = -MAX_MOTOR
            right_power = -MAX_MOTOR
        else:
            target_value = 1.40  # desired line position
            current_value = self.compute_rotation_speed()
            print("Current Value:", current_value)

            controller_power = self.controller.pid_output(current_value, target_value)
            print("Controller Power:", controller_power)

            # Ensure that the motor power doesn't exceed the limit
            left_power = MAX_MOTOR + controller_power
            right_power = MAX_MOTOR - controller_power
            print("(", left_power, ",", right_power, ")")

        self.driveMotors(left_power, right_power)


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