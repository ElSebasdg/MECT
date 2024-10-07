
from pickle import FALSE
from random import random, choice
import sys
from textwrap import wrap
from this import d
from croblink import *
from math import *
import xml.etree.ElementTree as ET

CELLROWS=7
CELLCOLS=14

MAX_MOTOR = 0.135


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

        self.turn = ""

        self.rotate_state = False
        self.arrived_target_angle = True
        self.arrived_next_cell = False

        self.current_angle = self.measures.compass
        self.target_angle = self.measures.compass

        self.visitedCells = []
        self.allVisitedCells = []
        self.visitedCells.append((0,0))

        self.corners = {}

        self.history = []

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
            
            print("Current Angle: ", self.pos)
            print("Angulo current: ", self.current_angle)

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


        self.current_angle = self.measures.compass
    
    def find_turn(self):
        lst_targetcells = []
        target = []

        # Reached a dead end
        # Rotate 180 degress
        if "TURN_ARROUND" in self.sensors:
            print("DEAD END")

            # 0
            if self.current_angle < 10 and self.current_angle > -10:
                print("zero")
                print("last visited: ", )
                target = [(round(self.pos[0]-1), round(self.pos[1])), 180,"RIGHT" ,True]           # Ommits the jitter nonsense

            # 90
            elif self.current_angle > 80 and self.current_angle < 100:
                print("noventa")
                target = [(round(self.pos[0]), round(self.pos[1]) - 1),-90,"LEFT", True] 
            

            # -90
            elif self.current_angle < -80 and self.current_angle > -100:
                print("-noventa")
                target = [(round(self.pos[0]), round(self.pos[1])  + 1),90,"LEFT", True]       

            #
            elif abs(self.current_angle) > 170:     # In this case removes the jitter nonsense too 
                print("HERE")
                if self.current_angle  < 0:
                    target = [(round(self.pos[0] + 1), round(self.pos[1])), 0,"LEFT",True]  
                else:
                    target = [(round(self.pos[0] + 1), round(self.pos[1])), 0,"RIGHT",True]  

            lst_targetcells.append(target)
            self.allVisitedCells.append(target)
                
        if self.sensors == [] or "CENTER" in self.sensors:
            # Just to calculate target  cell
            if self.current_angle < 10 and self.current_angle > -10:
                target = [(round(self.pos[0]) + 1, round(self.pos[1])), None,"CENTER", False]   
            
            elif self.current_angle > 80 and self.current_angle < 100:

                target = [(round(self.pos[0]), round(self.pos[1] + 1)), None, "CENTER",False]     
            
            elif self.current_angle < -80 and self.current_angle > -100:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1), None, "CENTER",False]      
            
            elif abs(self.current_angle) > 170:
                print("siuuuuuuuuu")
                target = [(round(self.pos[0]) - 1, round(self.pos[1])), None, "CENTER",False]

            #return "FORWARD", False
            lst_targetcells.append(target) 
            self.allVisitedCells.append(target)  

        if "LEFT" in self.sensors:
            if self.current_angle < 10 and self.current_angle > -10:
                target= [(round(self.pos[0]), round(self.pos[1])+1), 90,"LEFT", True]           
            
            elif self.current_angle > 80 and self.current_angle < 100:
                target= [(round(self.pos[0] - 1), round(self.pos[1])), 180,"LEFT", True]         
            
            elif self.current_angle < -80 and self.current_angle > -100:
                target = [(round(self.pos[0] + 1), round(self.pos[1])), 0, "LEFT", True]         

            
            elif abs(self.current_angle) > 170:
                target = [(round(self.pos[0]), round(self.pos[1]) - 1),-90,"LEFT", True]        

            #return "LEFT", True
        
            lst_targetcells.append(target)
            self.allVisitedCells.append(target)   
        
        if "RIGHT" in self.sensors:

            # 0 
            if self.current_angle < 10 and self.current_angle > -10:
                target = [(round(self.pos[0]), round(self.pos[1])-1), -90,"RIGHT", True]           
            
            # 90
            elif self.current_angle > 80 and self.current_angle < 100:
                target= [(round(self.pos[0] + 1), round(self.pos[1])), 0,"RIGHT", True]         
            

            # -90
            elif self.current_angle < -80 and self.current_angle > -100:
                target = [(round(self.pos[0] - 1), round(self.pos[1])),-180,"RIGHT", True]
            
            # 180
            elif abs(self.current_angle) > 170:
                target = [(round(self.pos[0]), round(self.pos[1]) + 1), 90,"RIGHT", True]         
            
            #return "RIGHT", True
                
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
                
            
        aux = [cell for cell in lst_targetcells if cell[0] not in self.visitedCells]

        # If there is there is no visited cells to be found just 
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
        
        # If there is new cells to be visited randomly choose one 
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

    
    def access_last_visited_target(self):
        if self.visited_targets:
            last_visited_target = self.visited_targets[-1]
            return last_visited_target
        else:
            return None


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
        if self.map_posx >= 0:
            if self.rotate_state == True:
                MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] = 'O'
            elif -5 < int(self.current_angle) < 5 and self.rotate_state == False and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] != 'O' and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] != 'I':
                MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] = '-'
            elif (-175 > int(self.current_angle) or int(self.current_angle) > 175) and self.rotate_state == False and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] !='O'and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] != 'I':
                MAP[-int(self.map_posx) + 10][int(self.map_posy + 24)] = '-' 
            elif -85 > int(self.current_angle) > -95 and self.rotate_state == False and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] !='O' and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] != 'I':
                MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] = '|'
            elif 85 < int(self.current_angle) < 95 and self.rotate_state == False and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] !='O' and MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] != 'I':
                MAP[-int(self.map_posx) + 10][int(self.map_posy) + 24] = '|'
            else:
                None
        else:
            if self.rotate_state == True:
                MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] = 'O'
            elif -5 < int(self.current_angle) < 5 and self.rotate_state == False and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'O' and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'I':
                MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] = '-'
            elif (-175 > int(self.current_angle) or int(self.current_angle) > 175) and self.rotate_state == False and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'O' and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'I':
                MAP[abs(int(self.map_posx)) + 10][int(self.map_posy + 24)] = '-'
            elif -85 > int(self.current_angle) > -95 and self.rotate_state == False and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] !='O' and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'I':
                MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] = '|'
            elif 85 < int(self.current_angle) < 95 and self.rotate_state == False and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] !='O' and MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] != 'I':
                MAP[abs(int(self.map_posx)) + 10][int(self.map_posy) + 24] = '|'
            else:
                None

        
    def printMapFile(self):
        for l in range(21):
            for c in range(49):
                if MAP[l][c] == 'O':
                    MAP[l][c] = ' '

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

    def wander(self):


        if len(self.history) < 3 and len(self.history) >= 0:
            self.history.append(self.measures.lineSensor)   
        elif len(self.history) == 3:
            self.history = self.history[1:]
            self.history.append(self.measures.lineSensor) 
        
        #print(self.history)
        print("\n")


        if self.history == [['0','0','1','1','1','0','0'],['0','0','1','1','1','0','0'],['0','0','0','0','0','0','0']]:
            print("----------------------------------------------dead end--------------------------------------------")   

        self.deconstruct()

        self.map_posx = (self.measures.y - self.initial_pos[1])
        self.map_posy = (self.measures.x - self.initial_pos[0])
        

        self.pos = ((self.measures.x - self.initial_pos[0]) / 2, (self.measures.y - self.initial_pos[1]) / 2)
        
        # print("self.pos: ", self.pos)
        # print("self.measures.x: ", self.measures.x)
        # print("self.initial_pos[0]: ", self.initial_pos[0])
        # asa = (self.measures.x - self.initial_pos[0]) / 2
        # print("subtraction: ", asa)

        print(int(self.map_posx) + 10,int(self.map_posy) + 24)

        self.writeMap()

        if not self.rotate_state and self.arrived_target_cell():

            print("Computing new Target cell")


            if self.target_cell not in self.visitedCells:
                self.visitedCells.append(self.target_cell)

            if self.ln_center == [1,1,1]:
                print("centro")
                self.sensors.append("CENTER") 

            if self.history == [['0','0','1','1','1','0','0'],['0','0','1','1','1','0','0'],['0','0','0','0','0','0','0']]:
                print("----------------------------------------------------------------VIROUUU---------------------------------------------------------")
                self.sensors.append("TURN_ARROUND")
            aux = self.target_cell
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            self.sensors = []

            # if self.history == [['0','0','1','1','1','0','0'],['0','0','1','1','1','0','0'],['0','0','0','0','0','0','0']]:
            #     print("----------------------------------------------dead end--------------------------------------------")   


            if self.endCondition(aux) and len(self.corners) > 4:
                self.printMapFile()
                self.finish()
            
            print(f"Target Angle = {self.target_angle}\t Turn = {self.turn}")
            print(f"Current cel = {self.pos}\t Target cell = {self.target_cell}")
        
        elif self.history == [['0','0','1','1','1','0','0'],['0','0','1','1','1','0','0'],['0','0','0','0','0','0','0']]:
            print("----------------------------------------------------------------VIROUUU---------------------------------------------------------")
            self.sensors.append("TURN_ARROUND")
            print("LAST VISITED",self.allVisitedCells[-2])
            aux = self.target_cell
            self.turn, self.rotate_state = self.find_turn()
            self.arrived_target_angle = False
            self.sensors = []  
        # in case it bugs
        if self.measures.lineSensor == ['0','0', '0','0','0','0','0'] and not self.rotate_state and not self.arrived_target_cell:
            print("Finish")
            self.finish()
        

        if self.rotate_state and not self.arrived_target_angle:
            diff = abs(abs(self.target_angle) - abs(self.current_angle))

            if diff < 8:
                print("Arrived Target Angle")
                self.arrived_target_angle = True
                self.rotate_state = False
            else:
                pow = self.compute_rotation_speed()                    

                if self.turn == "LEFT":
                    self.driveMotors(-pow, pow)

                if self.turn == "RIGHT":
                    self.driveMotors(pow, -pow)
        else:

            self.remove_jitter()
            controller_power = self.controller.compute_speed(self.current_angle, self.target_angle)
            pow = self.compute_speed()
            # Adjust right a litle 
            if self.ln_center == [0,1,1,]:
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