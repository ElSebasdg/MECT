
from pickle import FALSE
from random import random, choice
import sys
from textwrap import wrap
from this import d
from croblink import *
from math import *
import xml.etree.ElementTree as ET
import time

CELLROWS=7
CELLCOLS=14

MAX_MOTOR = 0.13

MAP = [ [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)

        self.controller = PID(0.0015, 0.00000001, 0.000001)
        self.readSensors()

        self.initial_pos = [self.measures.x, self.measures.y]

        self.pos = ((self.measures.x - self.initial_pos[0]) / 2, (self.measures.y - self.initial_pos[1]) / 2)
        
        self.map = [[0 for col in range(CELLCOLS*2-1)] for row in range(CELLROWS*2-1)]

        self.ln_left = None
        self.ln_center = None
        self.ln_right = None
        self.ln_right45 = None
        self.ln_right135 = None
        self.ln_left45 = None
        self.ln_left135 = None

        self.turn = ""


        self.rotate_state = False
        self.arrived_target_angle = True
        self.arrived_next_cell = False

        self.current_angle = self.measures.compass
        self.target_angle = self.measures.compass
        self.initial_angle = 0

        self.visitedCells = []
        self.allVisitedCells = []
        self.visitedCells.append((0,0))

        self.history = []

        self.corners = {}

        self.lPow = 0
        self.rPow = 0


        self.sensors = []

        self.res = 0

        self.find_turn()


        print("Compass = ", self.measures.compass)
        print("Initial_pos ", self.pos)



    # In this map the center of cell (i,j), (i in 0..6, j in 0..13) is mapped to labMap[i*2][j*2].
    # to know if there is a wall on top of cell(i,j) (i in 0..5), check if the value of labMap[i*2+1][j*2] is space or not
    def setMap(self, labMap):
        self.labMap = labMap

    def printMap(self):
        for l in reversed(self.labMap):
            print(' '.join([str(l) for l in l]))

    def run(self):
        if self.status != 0:
            print("Connection refused or error")
            quit()

        state = 'stop'
        stopped_state = 'run'

        while True:
            self.readSensors()

            if self.measures.endLed:
                print("exiting")
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
                    self.setVisitingLed(True)
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

    # def printMap(self):
    #     print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in self.map]))
    


    def print_sensor(self):
        print(f"Center = {self.ln_center}\t Left = {self.ln_left}\t Right = {self.ln_right}")
        print(f"Current_cell = {self.pos}   Target_cell = {self.target_cell}")
        print(f"Arrived Target Cell = {self.arrived_target_cell()}")
        print(f"Rotate State = {self.rotate_state}   Arrived Target Angle = {self.arrived_target_angle}")
        print(f"Sensors = {self.sensors}")
        print(f"Visited Cells = {self.visitedCells}")
        print(self.measures.compass)

    def get_relative_pos(self):
        self.initial_pos = ((self.measures.x - self.initial_pos[0]) / 2, (self.measures.y - self.initial_pos[1]) / 2)

    def deconstruct(self):
        self.ln_left = [int(val) for val in self.measures.lineSensor[0:2]]
        self.ln_center = [int(val) for val in self.measures.lineSensor[2:5]]
        self.ln_right = [int(val) for val in self.measures.lineSensor[5:7]]
        self.ln_left45 = [int(val) for val in self.measures.lineSensor[0:2]]
        self.ln_left135 = [int(val) for val in self.measures.lineSensor[0:2]]
        self.ln_right45 = [int(val) for val in self.measures.lineSensor[5:7]]
        self.ln_right135 = [int(val) for val in self.measures.lineSensor[5:7]]
        self.full = [int(val) for val in self.measures.lineSensor]
        self.small_arr = [int(val) for val in self.measures.lineSensor[1:6]]
        self.current_angle = self.measures.compass

    def find_turn(self):
        
        lst_targetcells = []
        target = []

        
        print("target cells: ", lst_targetcells)
        #Reached a dead end
        #Rotate 180 degress
        if "TURN_AROUND" in self.sensors:
            print("TURN_AROUND STATE")

            # 0
            if self.current_angle < 5 and self.current_angle > -5:
                print("zero")
                target = [(round(self.pos[0]-1), round(self.pos[1])), 180,"TURN_AROUND" ,True]      

            # 90
            elif self.current_angle > 85 and self.current_angle < 95:
                print("noventa")
                target = [(round(self.pos[0]), round(self.pos[1]) - 1),-90,"TURN_AROUND", True]        
            
            # -90
            elif self.current_angle < -85 and self.current_angle > -95:
                print("-noventa")
                target = [(round(self.pos[0]), round(self.pos[1]) + 1),90,"TURN_AROUND", True]       

                
            # 180 / -180
            elif abs(self.current_angle) > 175:
                print("O OUTRO")
                target = [(round(self.pos[0] + 1), round(self.pos[1])), 0,"TURN_AROUND",True] 

            #return "TURN_AROUND", True   
            print(target)
            lst_targetcells.append(target)
            self.allVisitedCells.append(target)  
                
                
        if self.sensors == [] or "CENTER" in self.sensors:
            # Just to calculate target  cell
            if self.current_angle > -3 and self.current_angle < 3:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])), 0,"CENTER", True]   
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target = [(round(self.pos[0]) + 1, round(self.pos[1] + 1)), 45, "CENTER",True]     
            
            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0]), round(self.pos[1] + 1)), 90, "CENTER",True]  

            elif self.current_angle > 132 and self.current_angle < 138:
                target = [(round(self.pos[0]) - 1, round(self.pos[1] + 1)), 135, "CENTER",True] 

            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target = [(round(self.pos[0]) - 1, round(self.pos[1])), 180, "CENTER",True]     
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0]) - 1, round(self.pos[1] - 1)), -135, "CENTER",True]         
            
            elif self.current_angle < -87 and self.current_angle > -93:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1), -90, "CENTER",True]      
            
            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0]) + 1, round(self.pos[1] - 1)), -45, "CENTER",True]     

            #return "FORWARD", False
            lst_targetcells.append(target)   
            self.allVisitedCells.append(target)  

        if "LEFT" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target= [(round(self.pos[0]), round(self.pos[1]) + 1), 90,"LEFT", True]           
                print ("-------------------LEFT TURN-----------------") 

            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0] - 1), round(self.pos[1]) - 1), 135,"LEFT", True] 
                print ("-------------------LEFT TURN-----------------")        
            
            elif self.current_angle > 85 and self.current_angle < 95:
                target = [(round(self.pos[0] - 1), round(self.pos[1])), 180, "LEFT", True]         

            elif self.current_angle > 132 and self.current_angle < 138:
                target= [(round(self.pos[0]) - 1, round(self.pos[1]) + 1), -135,"LEFT", True]           
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0]), round(self.pos[1]) - 1), -90,"LEFT", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0] + 1), round(self.pos[1]) + 1), -45, "LEFT", True]    

            elif self.current_angle < -87 and self.current_angle > -93:
                target= [(round(self.pos[0] + 1), round(self.pos[1])), 0,"LEFT", True]         
            
            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0] + 1), round(self.pos[1]) - 1), 45, "LEFT", True]

            #return "LEFT", True
        
            lst_targetcells.append(target)   
            self.allVisitedCells.append(target)  
        
        if "RIGHT" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target= [(round(self.pos[0]), round(self.pos[1]) - 1), -90,"RIGHT", True]           
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0] + 1), round(self.pos[1]) + 1), -45,"RIGHT", True]         

            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0] + 1), round(self.pos[1])), 0, "RIGHT", True]    

            elif self.current_angle > 132 and self.current_angle < 138:
                target= [(round(self.pos[0]) + 1, round(self.pos[1]) - 1), 45,"RIGHT", True]           
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0]), round(self.pos[1]) + 1), 90,"RIGHT", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0] - 1), round(self.pos[1]) - 1), 135, "RIGHT", True]    

            elif self.current_angle < -87 and self.current_angle > -93:
                target= [(round(self.pos[0] - 1), round(self.pos[1])), -180,"RIGHT", True]         
            
            elif self.current_angle == -45:
                target = [(round(self.pos[0] - 1), round(self.pos[1]) + 1), 45, "RIGHT", True]

            #return "RIGHT", True
                
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)  

        if "LEFT45" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target = [(round(self.pos[0]) + 1, round(self.pos[1]) + 1), 45,"LEFT45", True]           
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0]), round(self.pos[1]) - 1), 90,"LEFT45", True]         
            
            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0] - 1), round(self.pos[1]) - 1), 135,"LEFT45", True]
            
            elif self.current_angle > 132 and self.current_angle < 138:
                target = [(round(self.pos[0]) - 1, round(self.pos[1])), 180,"LEFT45", True]         
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0] - 1), round(self.pos[1]) + 1), -135,"LEFT45", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0]), round(self.pos[1]) + 1), -90,"LEFT45", True]
            
            elif self.current_angle < -87 and self.current_angle > -93:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])) + 1, -45,"LEFT45", True] 

            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])), 0,"LEFT45", True]

            #return "LEFT45", True
                
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)     
        
        if "LEFT135" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target = [(round(self.pos[0]) - 1, round(self.pos[1]) - 1), 135,"LEFT135", True]           
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0]) - 1, round(self.pos[1])), 180,"LEFT135", True]         
            
            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0] - 1), round(self.pos[1]) + 1), -135,"LEFT135", True]
            
            elif self.current_angle > 132 and self.current_angle < 138:
                target = [(round(self.pos[0]), round(self.pos[1]) + 1), -90,"LEFT135", True]         
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0] + 1), round(self.pos[1]) + 1), -45,"LEFT135", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])), 0,"LEFT135", True]
            
            elif self.current_angle < -87 and self.current_angle > -93:
                target = [(round(self.pos[0]) + 1, round(self.pos[1]) - 1), 45,"LEFT135", True] 

            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1), 90,"LEFT135", True]

            #return "LEFT135", True
                
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)  

        if "RIGHT45" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target = [(round(self.pos[0]) + 1, round(self.pos[1]) + 1), -45,"RIGHT45", True]           
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0]) + 1, round(self.pos[1])), 0,"RIGHT45", True]         
            
            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0] + 1), round(self.pos[1]) - 1), 45,"RIGHT45", True]
            
            elif self.current_angle > 132 and self.current_angle < 138:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1), 90,"RIGHT45", True]         
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0] - 1), round(self.pos[1]) - 1), 135,"RIGHT45", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0]) - 1, round(self.pos[1])),-180,"RIGHT45", True]
            
            elif self.current_angle < -87 and self.current_angle > -93:
                target = [(round(self.pos[0]) - 1, round(self.pos[1]) + 1), -135,"RIGHT45", True] 

            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0]), round(self.pos[1]) + 1), -90,"RIGHT45", True]

            #return "RIGHT45", True
                
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)  

        if "RIGHT135" in self.sensors:
            if self.current_angle > -3 and self.current_angle < 3:
                target = [(round(self.pos[0]) - 1, round(self.pos[1]) + 1), -135,"RIGHT135", True]           
            
            elif self.current_angle > 43 and self.current_angle < 48:
                target= [(round(self.pos[0]), round(self.pos[1]) + 1), -90,"RIGHT135", True]         
            
            elif self.current_angle > 87 and self.current_angle < 93:
                target = [(round(self.pos[0]) + 1, round(self.pos[1]) + 1),-45,"RIGHT135", True]
            
            elif self.current_angle > 132 and self.current_angle < 138:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])), 0,"RIGHT135", True]         
            
            elif (177 <= self.current_angle <= 180) or (-180 <= self.current_angle <= -177):
                target= [(round(self.pos[0] + 1), round(self.pos[1]) - 1), 45,"RIGHT135", True]         
            
            elif self.current_angle < -132 and self.current_angle > -138:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1), 90,"RIGHT135", True]
            
            elif self.current_angle < -87 and self.current_angle > -93:
                target = [(round(self.pos[0]) - 1, round(self.pos[1]) - 1), 135,"RIGHT135", True] 

            elif self.current_angle < -42 and self.current_angle > -48:
                target = [(round(self.pos[0]) - 1, round(self.pos[1])), 180,"RIGHT135", True]

            #return "RIGHT135", True
                
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)  

        if len(lst_targetcells) > 1:
            print("Interceção")
            if self.pos in self.corners.keys():
                aux = self.corners.get(self.pos)
                for cell in lst_targetcells:
                    if cell[0] not in aux and  cell[0] not in self.visitedCells:
                        self.corners[self.pos] += cell[0]
            else:
                self.corners[self.pos] = [cell[0] for cell in lst_targetcells]

            print(f"Corners = {self.corners}")

        #print(f"List of Target Cells {lst_targetcells}")
        aux = [cell for cell in lst_targetcells if cell[0] not in self.visitedCells]
        #print(f"List of Target Cells not visited {aux}")
        if aux == []:
            for elem in lst_targetcells:
                #Prioritises going forward
                if elem[2] == "CENTER":
                    cell = elem
                else:
                    cell = ""
            
            if cell == "":
                cell = choice(lst_targetcells)
            
            self.target_cell = cell[0]
            if cell[1] is not None:
                self.target_angle = cell[1]

            self.f += 1
            return cell[2], cell[3]
        
        else:
            cell = choice(aux)
            self.target_cell = cell[0]
            if cell[1] is not None:
                self.target_angle = cell[1]

            self.f = 0
            return cell[2], cell[3]
    
    def arrived_target_cell(self):
        dist = sqrt(pow(self.target_cell[0] - self.pos[0],2) + pow(self.target_cell[1] -self.pos[1],2))
        #print(dist)
        return dist < 0.03

    def remove_jitter(self):
        # Remove jitter 
        if self.target_angle == -180:
            
            if self.current_angle > 175:
                self.target_angle = 180
        
        if self.target_angle == 180:

            if self.current_angle < -175:
                self.target_angle = -180       

                
    def compute_speed(self):
        dist = sqrt(pow(self.target_cell[0] -self.pos[0],2) + pow(self.target_cell[1] -self.pos[1],2))
        
        if dist < 0.26 and dist > 0.18:         
            if self.ln_right == [1,1]:
                if "RIGHT" not in self.sensors:
                    self.sensors.append("RIGHT")
                
            if self.ln_left == [1,1]:
                if "LEFT" not in self.sensors:
                    self.sensors.append("LEFT")

        if dist > 0.8:
            return MAX_MOTOR

        elif dist < 0.8 and dist >= 0.6:
            return MAX_MOTOR - 0.01
        
        elif dist < 0.6 and dist >= 0.4:
            return MAX_MOTOR - 0.02
        
        elif dist < 0.4 and dist >= 0.20:
            return MAX_MOTOR - 0.04
            
        else:
            return MAX_MOTOR - 0.09
        
    def compute_rotation_speed(self):
        teta = abs(self.target_angle - self.current_angle)
        #print(f"Teta = {teta}")
        if teta > 60:
            return 0.2
        
        if teta >= 25 and teta <= 60:
            return 0.08

        if teta < 25:
            return 0.02
        
    def writeMap(self):
        print(int(self.map_posx), int(self.map_posy))

        # if MAP[int(self.map_posx)][int(self.map_posy)] == 'I':
        #     None
        # elif -5 < self.current_angle < 5 or -175 <self.current_angle < 185:
        #     MAP[int(self.map_posx)][int(self.map_posy)] = '-'
        # elif 85 < self.current_angle < 95 or -85 < self.current_angle < -95:
        #     MAP[int(self.map_posx)][int(self.map_posy)] = '|'
        # else:
        #     None

        if MAP[int(self.map_posx)][int(self.map_posy)] == 'I':
            None
        elif int(self.current_angle) == 5 or int(self.current_angle) == 180:
            MAP[int(self.map_posx)][int(self.map_posy)] = '-'
        elif int(self.current_angle) == 90 or int(self.current_angle) == 90:
            MAP[int(self.map_posx)][int(self.map_posy)] = '|'
        else:
            None
        
    def printMapFile(self):
        with open("output.map", "w") as map_file:
            for l in range(21):
                for c in range(49):
                    map_file.write(MAP[l][c])
            map_file.write("\n")

    def endCondition(self, current):
        print("Items: ")
        print(self.corners.items())
        count = len(self.corners)
        for k,v in self.corners.items():
            if current in v:
                print("Removing element")
                v.remove(current)
                self.corners[k] = v
                
            if v == []:
                count -= 1
        return count == 0

    def is_scruffy(self):
        if self.measures.compass == 90.0 and self.history == [['0','0','0','0','0','0','0']]:
            print("----------------------------------------------------------------NAO ME PEGA--------------------------------------------------------")
            self.sensors.append("RIGHT")
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            aux = self.target_cell
            self.sensors = []

        if self.measures.compass == -90.0 and self.history == [['0','0','0','0','0','0','0']]:
            print("----------------------------------------------------------------NAO ME PEGA--------------------------------------------------------")
            self.sensors.append("LEFT")
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            aux = self.target_cell
            self.sensors = []

        if (self.measures.compass == 0.0 or abs(self.measures.compass) == 180.0)  and self.history == [['0','0','0','0','0','0','0']]:
            print("----------------------------------------------------------------NAO ME PEGA--------------------------------------------------------")
            self.sensors.append("TURN_AROUND")
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            aux = self.target_cell
            self.sensors = []


    def wander(self):
        self.deconstruct()

        # print section debugging------------------------------------------------------------------------------------------------
        self.is_scruffy()

        #print(self.full)
        #print(self.history)
        #print("\n")
        # print(self.measures.compass)
        # print("\n")
        # print(self.pos)
        # print("Current Angle")
        # print(self.current_angle)
        # print("Target Angle")
        # print(self.target_angle)
        # print("Arrived at Target Cell")
        # print(self.arrived_target_cell())
        # print("Rotate State")
        # print(self.rotate_state)
        # print("Target Cell")
        # print(self.target_cell)
        # print("MAP_POSX")
        # print(self.map_posx)
        # print("MAP_POSY")
        # print(self.map_posy)
        #print("Current angle: ",self.current_angle)
        #------------------------------------------------------------------------------------------------------------------------------------------

        self.map_posx = (abs(self.measures.y - self.initial_pos[1]) + 10)
        self.map_posy = (self.measures.x - self.initial_pos[0] + 25)

        self.pos = ((self.measures.x - self.initial_pos[0]) / 2, (self.measures.y - self.initial_pos[1]) / 2)
        
        if len(self.history) < 3 and len(self.history) >= 0:
            self.history.append(self.measures.lineSensor)   
        elif len(self.history) == 3:
            self.history = self.history[1:]
            self.history.append(self.measures.lineSensor) 
    

        # if self.f == 5:
        #     print(MAP)
        #     self.printMapFile()
        #     self.finish()
        
        self.writeMap()
        # for i in range(21):
        #     print("\n")
        #     for j in range(49):
        #         print(MAP[i][j])

        if not self.rotate_state and self.arrived_target_cell():

            print("Computing new Target cell")
            if self.target_cell not in self.visitedCells:
                self.visitedCells.append(self.target_cell)

            if self.ln_center == [1,1,1]:
                self.sensors.append("CENTER") 

            aux = self.target_cell
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            self.sensors = []


            # if self.endCondition(aux) and len(self.corners) > 4:
            #     self.printMapFile()
            #     self.finish()
            
            print(f"Target Angle = {self.target_angle}\t Turn = {self.turn}")
            print(f"Current cel = {self.pos}\t Target cell = {self.target_cell}")
        
        # in case it bugs
        if self.measures.lineSensor == ['0','0', '0','0','0','0','0'] and not self.rotate_state and not self.arrived_target_cell:
            print("Finish")
            self.finish()


        elif self.history == [['0','0','1','1','1','0','0'],['0','0','1','1','1','0','0'],['0','0','0','0','0','0','0']]:
            print("----------------------------------------------------------------VIROUUU---------------------------------------------------------")
            self.sensors.append("TURN_AROUND")
            #print("LAST VISITED-1",self.allVisitedCells[-1])
            #print("LAST VISITED-2",self.allVisitedCells[-2])
            #print("LAST VISITED-3",self.allVisitedCells[-3])
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            aux = self.target_cell
            self.sensors = [] 
         

        if self.rotate_state and not self.arrived_target_angle:
            turnArroundFlag = False
            print("self turning")
            print("current angle: ",self.current_angle)
            print("target angle: ",self.target_angle)

            #                                -90                                                  90                                                                 90                                                        -90               
            if ((self.target_angle > -92.0 and self.target_angle < -88.0) and (self.current_angle > 85 and self.current_angle < 95)) or ((self.target_angle < 92.0 and self.target_angle > 88.0) and (self.current_angle < -85 and self.current_angle > -95)):
                print("DIFF ZEROO")
                turnArroundFlag = True
                diff = 0.0
            else:
                diff = abs(abs(self.target_angle) - abs(self.current_angle))

            print("Diff is equal to ", diff)

            if turnArroundFlag:
                print("FLAG TRUE")
            else:
                print("FLAG FALSE")

            if diff < 8 and turnArroundFlag == False:
                print("Arrived Target Angle")
                self.arrived_target_angle = True
                self.rotate_state = False

            elif diff == 0.0 and turnArroundFlag == True:
                pow = self.compute_rotation_speed()
                if self.turn == "TURN_AROUND":
                    #print("TURNING 180")
                    print("(",-pow,",",pow,")")
                    self.driveMotors(-pow, pow)

            else:
                turnArroundFlag = False
                print("POW POW POW")
                pow = self.compute_rotation_speed()
                print(pow)
                # in case of 180 degree
                if self.turn == "TURN_AROUND":
                    print("TURNING 180")
                    self.driveMotors(-pow, pow)


                if self.turn == "LEFT":
                    self.driveMotors(-pow, pow)

                if self.turn == "RIGHT":
                    self.driveMotors(pow, -pow)

                if self.turn == "LEFT45":
                    self.driveMotors(-pow, pow)

                if self.turn == "LEFT135":
                    self.driveMotors(-pow, pow)

                if self.turn == "RIGHT45":
                    self.driveMotors(pow, -pow)
                
                if self.turn == "RIGHT135":
                    self.driveMotors(pow, -pow)

        else:
            self.remove_jitter()
            controller_power = self.controller.compute_speed(self.current_angle, self.target_angle)
            pow = self.compute_speed()
            print(pow)
            # Adjust right a litle 
            if self.ln_center == [0,1,1]:
                self.driveMotors(pow - controller_power + 0.015, pow + controller_power)
            
            # Adjust right a lot 
            elif self.ln_center == [0,0,1]:
                self.driveMotors(pow - controller_power + 0.025, pow + controller_power)
            
            # Adjust left a little
            elif self.ln_center == [1,1,0]:
                self.driveMotors(pow - controller_power, pow + controller_power + 0.015)
            
            # Adjust left a lot
            elif self.ln_center == [1,0,0]:
                self.driveMotors(pow - controller_power, pow + controller_power + 0.025)

            else:
                self.driveMotors(pow - controller_power, pow + controller_power)


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
    def compute_speed(self, current_value, target_value):
        self.error = target_value - current_value
        self.integral += self.error
        self.derivative = self.error - self.last_error
        self.last_error = self.error
        self.output = self.kp * self.error + self.ki * self.integral + self.kd * self.derivative
        # clip control to avoid saturation
        if self.output > MAX_MOTOR:
            self.output = MAX_MOTOR
        if self.output < -MAX_MOTOR:
            self.output = -MAX_MOTOR
        return self.output


            
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
