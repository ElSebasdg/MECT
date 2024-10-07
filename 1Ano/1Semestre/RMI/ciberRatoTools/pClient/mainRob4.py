import math
import sys
from this import d
from croblink import *
from math import *
import xml.etree.ElementTree as ET

from dijkstra import Graph

CELLROWS=7
CELLCOLS=14

class MyRob(CRobLinkAngs):
    def __init__(self, rob_name, rob_id, angles, host):
        CRobLinkAngs.__init__(self, rob_name, rob_id, angles, host)
        self.flag = 'nada'
        self.matriz = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
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
        
        self.x_inicial = 0
        self.y_inicial = 0

        self.x_atual = 0
        self.y_atual = 0

        self.count = 0
        self.boost = 0

        self.intersecao = 'false'
        self.cond_inicial = 'true'

        self.char_anterior = ' '
        self.char_atual = ' '
        self.contador = 0

        self.orientacao_anterior = ''
        self.orientacao_atual = ''
        self.T_seguido = 0
        self.guarda_bits_nas_curvas = []
        
        self.intersecao_T = 'false'
        self.intersecao_MAIS = 'false'

        self.bussola_antes = 0
        self.tras = 0

        self.dic_Intersecoes = dict()

        self.dic_Intersecoes_distancias = dict()
        
        self.T_anterior = Coordenadas(10,24).toString()
        self.distancia= 0
        self.coord_anteriores = Coordenadas(0,0).toString()
        self.coord_atuais = Coordenadas(0,0).toString()
        
        self.lista_beacons = dict()
        self.beacons_mesmo = dict()
        self.turned_around = 'false'

        self.T_x = 0
        self.T_y = 0

        self.path = list()
        self.perdi = 0
        self.update_file = 0

        self.power_left = 0
        self.power_right = 0
        self.out_left = 0
        self.out_right = 0
        self.lin = 0
        self.angulo= 0

        self.goToI = 'false'
        self.coord_beacons = dict()
        self.flag_verify = 'false' 

        self.x_atras = 0
        self.y_atras = 0
        self.history = []

    # In this map the center of cell (i,j), (i in 0..6, j in 0..13) is mapped to labMap[i*2][j*2].
    # to know if there is a wall on top of cell(i,j) (i in 0..5), check if the value of labMap[i*2+1][j*2] is space or not
    def setMap(self, labMap):
        self.labMap = labMap

    def printMap(self):
        for l in reversed(self.labMap):
            print(''.join([str(l) for l in l]))

    
    def algoritmo(self,filename, start, end):
   
        graph = Graph(filename)
        returned_path, returned_distance = graph.shortest_path(start, end)

        print('\ngraph definition file: {0}'.format(filename))
        print('      start/end nodes: {0} -> {1}'.format(start, end))
        print('        shortest path: {0}'.format(list(returned_path)))
        print('       total distance: {0}'.format(returned_distance))
        auxxx = list(returned_path)

        self.path = self.path + auxxx[:-1]

    def algoritmo1(self,filename, start, end):
   
        graph = Graph(filename)
        returned_path, returned_distance = graph.shortest_path(start, end)

        # print('\ngraph definition file: {0}'.format(filename))
        # print('      start/end nodes: {0} -> {1}'.format(start, end))
        # print('        shortest path: {0}'.format(list(returned_path)))
        # print('       total distance: {0}'.format(returned_distance))
        return returned_distance

    def check_right(self):
        
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T' or (self.matriz[ self.x_atual ][self.y_atual]) == '+':
            if(self.orientacao_atual=='norte'):
                if (self.x_atual +1 >=21 ):
                    return 'false'
                if self.matriz[ self.x_atual +1][self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.x_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual -1 ][self.y_atual ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.y_atual +1 >= 49):
                    return 'false'
                if self.matriz[ self.x_atual][self.y_atual+1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual ][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='noroeste'):
                if (self.x_atual +1 >=21 ):
                    return 'false'
                if self.matriz[self.x_atual - 1][self.y_atual] != ' ' or self.matriz[self.x_atual][self.y_atual + 1] != ' ' or self.matriz[self.x_atual + 1][self.y_atual + 1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='nordeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual][self.y_atual - 1] != ' ' or self.matriz[self.x_atual + 1][self.y_atual] != ' ' or self.matriz[self.x_atual + 1][self.y_atual - 1] != ' ': 
                    return 'true'
            elif(self.orientacao_atual=='sudoeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual][self.y_atual + 1] != ' ' or self.matriz[self.x_atual - 1][self.y_atual] != ' ' or self.matriz[self.x_atual - 1][self.y_atual + 1] != ' ': 
                    return 'true'
            elif(self.orientacao_atual=='sudeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual - 1][self.y_atual] != ' ' or self.matriz[self.x_atual][self.y_atual - 1] != ' ' or self.matriz[self.x_atual - 1][self.y_atual - 1] != ' ': 
                    return 'true'
            return 'false'
        else:
            if(self.orientacao_atual=='norte'):
                if (self.x_atual +1 >=21 or self.y_atual +1 >= 49 ):
                    return 'false'
                if self.matriz[ self.x_atual +1][self.y_atual +1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.x_atual -1 <0 or self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual -1 ][self.y_atual -1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.x_atual -1 <0 or self.y_atual +1 >= 49 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual-1][self.y_atual+1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.x_atual +1 >=21 or self.y_atual -1 <0):
                    return 'false'
                if self.matriz[ self.x_atual +1][ self.y_atual-1] != ' ':
                    return 'true'
            return 'false'

    def round_up_to_nearest_even_number(self,num):
        return math.ceil(num / 2) * 2
    
    def round_to_nearest_even_number(self,num):
        return round(num / 2.) * 2
    
    def round_down_to_nearest_even_number(self,num):
        return math.floor(num / 2) * 2

    def check_left(self):
       
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T' or (self.matriz[ self.x_atual ][self.y_atual]) == '+':    
            if(self.orientacao_atual=='norte'):
                if (self.x_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual -1 ][ self.y_atual ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.x_atual +1 >=21 ):
                    return 'false'
                if self.matriz[ self.x_atual +1][ self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.y_atual +1 >= 49):
                    return 'false'
                if self.matriz[ self.x_atual][ self.y_atual +1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='noroeste'):
                if (self.x_atual +1 >=21 ):
                    return 'false'
                if self.matriz[self.x_atual][self.y_atual - 1] != ' ' or self.matriz[self.x_atual - 1][self.y_atual] != ' ' or self.matriz[self.x_atual - 1][self.y_atual - 1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='nordeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual][self.y_atual + 1] != ' ' or self.matriz[self.x_atual - 2][self.y_atual + 1] != ' ' or self.matriz[self.x_atual - 1][self.y_atual] != ' ': 
                    return 'true'
            elif(self.orientacao_atual=='sudoeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual + 1][self.y_atual] != ' ' or self.matriz[self.x_atual + 1][self.y_atual - 1] != ' ' or self.matriz[self.x_atual][self.y_atual - 1] != ' ': 
                    return 'true'
            elif(self.orientacao_atual=='sudeste'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[self.x_atual][self.y_atual + 1] != ' ' or self.matriz[self.x_atual + 1][self.y_atual + 1] != ' ' or self.matriz[self.x_atual + 1][self.y_atual] != ' ': 
                    return 'true'
            return 'false'
        else:   
            if(self.orientacao_atual=='norte'):
                if (self.x_atual -1 <0 or self.y_atual +1 >= 49  ):
                    return 'false'
                if self.matriz[ self.x_atual -1 ][ self.y_atual +1 ] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.x_atual +1 >=21 or self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual +1][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.x_atual -1 <0 or  self.y_atual -1 <0  ):
                    return 'false'
                if self.matriz[ self.x_atual-1][ self.y_atual-1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.x_atual +1 >=21 or self.y_atual +1 >= 49  ):
                    return 'false'
                if self.matriz[ self.x_atual+1][ self.y_atual +1] != ' ':
                    return 'true'
            return 'false'

    
    def check__front(self):
        if(self.matriz[ self.x_atual ][self.y_atual]) == '+' or  self.matriz[ self.x_atual ][self.y_atual]== 'T':   
            if(self.orientacao_atual=='norte'):
                if (self.y_atual +1 >= 49):
                    return 'false'
                if self.matriz[ self.x_atual ][ self.y_atual+1]  != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.y_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual  ][self.y_atual -1] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.x_atual -1 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual -1][ self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.x_atual +1 >=21 ):
                    return 'false'
                if self.matriz[ self.x_atual +1 ][ self.y_atual] != ' ':
                    return 'true'
            return 'false'
        else:

            if(self.orientacao_atual=='norte'):
                if (self.y_atual +2 >= 49):
                    return 'false'
                if self.matriz[ self.x_atual ][ self.y_atual+2]  != ' ':
                    return 'true'
            elif(self.orientacao_atual=='sul'):
                if (self.y_atual -2 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual  ][self.y_atual -2] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='oeste'):
                if (self.x_atual -2 <0 ):
                    return 'false'
                if self.matriz[ self.x_atual -2][ self.y_atual] != ' ':
                    return 'true'
            elif(self.orientacao_atual=='este'):
                if (self.x_atual +2 >=21 ):
                    return 'false'
                if self.matriz[ self.x_atual +2 ][ self.y_atual] != ' ':
                    return 'true'
            return 'false'


    def next_T(self):
        
        if self.matriz[self.x_atual][self.y_atual] == 'T':     
            return 'true'
        
        elif(self.orientacao_atual=='norte'): 
            if (self.y_atual +1 >= 49):
                return 'false'
            if self.matriz[ self.x_atual ][ self.y_atual + 1] == 'T':
                return 'true'
        elif(self.orientacao_atual=='sul'):
            if (self.y_atual -1 <0 ):
                return 'false'
            if self.matriz[ self.x_atual  ][self.y_atual -1] == 'T':
                return 'true'
        elif(self.orientacao_atual=='oeste'):
            if (self.x_atual -1 <0 ):
                return 'false'
            if self.matriz[ self.x_atual -1][ self.y_atual] == 'T':
                return 'true'
        elif(self.orientacao_atual=='este'):
            if (self.x_atual +1 >=21 ):
                return 'false'
            if self.matriz[ self.x_atual +1 ][ self.y_atual] == 'T':
                return 'true'
        return 'false'
      
    def next_Mais(self):    
        if self.matriz[self.x_atual][self.y_atual] == '+':   
            return 'true'
        
        elif(self.orientacao_atual=='norte'):

            if (self.y_atual +1 >= 49):
                return 'false'
            if self.matriz[ self.x_atual ][ self.y_atual + 1] == '+':
               
                
                return 'true'
        elif(self.orientacao_atual=='sul'):
            if (self.y_atual -1 <0 ):
                return 'false'
            if self.matriz[ self.x_atual  ][self.y_atual -1] == '+':
             
               
                return 'true'
        elif(self.orientacao_atual=='oeste'):
            if (self.x_atual -1 <0 ):
                return 'false'
            if self.matriz[ self.x_atual -1][ self.y_atual] == '+':
               
               
                return 'true'
        elif(self.orientacao_atual=='este'):
            if (self.x_atual +1 >=21 ):
                return 'false'
            if self.matriz[ self.x_atual +1 ][ self.y_atual] == '+':
               
               
                return 'true'
        return 'false'

    

    def get_lados_T(self):
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T':    
            if(self.orientacao_atual=='norte') :
                x = self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")"]
            elif self.orientacao_atual=='sul':
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                  
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                return ["(" + str(x1) +","+ str(y1)+")","("+ str(x) +","+ str(y)+")"]
            elif(self.orientacao_atual=='oeste') :
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
              
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                   
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")"]
                
            elif  self.orientacao_atual=='este':
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                return ["(" + str(x1) +","+ str(y1)+")","("+ str(x) +","+ str(y)+")"]
        else:   
            if(self.orientacao_atual=='norte'):
                x= self.x_atual
                y = self.y_atual +1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual +1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")"]
                
            elif(self.orientacao_atual=='sul'):
                
                x= self.x_atual
                y = self.y_atual -1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                  
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual -1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")","("+ str(x) +","+ str(y)+")"]
            elif(self.orientacao_atual=='oeste'):
                x= self.x_atual -1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or self.matriz[x][y] != 'I'  or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T'  or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
                x1= self.x_atual -1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")"]
                
            elif(self.orientacao_atual=='este'):
                x= self.x_atual +1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual +  1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")","("+ str(x) +","+ str(y)+")"]
                
    def get_T_left(self):
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T' or self.matriz[ self.x_atual ][self.y_atual] == '+' :    
            if(self.orientacao_atual=='norte') :
                x = self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
              
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x2) +","+ str(y2)+")"]
            elif self.orientacao_atual=='sul':
                
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='oeste') :
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x2) +","+ str(y2)+")"]
                
            elif  self.orientacao_atual=='este':
               
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x2) +","+ str(y2)+")"]
        else:   
            if(self.orientacao_atual=='norte'):
                x= self.x_atual
                y = self.y_atual +1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual+1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='sul'):
                
               
                x1= self.x_atual
                y1 = self.y_atual -1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual-1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
               
            elif(self.orientacao_atual=='oeste'):
                x= self.x_atual -1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or self.matriz[x][y] != 'I'  or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T'  or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
                
                
                x2 = self.x_atual-1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='este'):
                
                x1= self.x_atual +  1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                x2 = self.x_atual+1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x2) +","+ str(y2)+")"]        
    
    def get_T_right(self):

        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T' or self.matriz[ self.x_atual ][self.y_atual] == '+' :    
            if(self.orientacao_atual=='norte') :
                
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
            elif self.orientacao_atual=='sul':
               
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1-1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='oeste') :
               
              
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                   
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif  self.orientacao_atual=='este':
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
        else:   
            if(self.orientacao_atual=='norte'):
                
                x1= self.x_atual
                y1 = self.y_atual +1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual+1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='sul'):
                
                x= self.x_atual
                y = self.y_atual -1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                  
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                
                x2 = self.x_atual
                y2 = self.y_atual-1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
               
            elif(self.orientacao_atual=='oeste'):
               
                x1= self.x_atual -1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                x2 = self.x_atual-1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='este'):
                x= self.x_atual +1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                
                
                x2 = self.x_atual+1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
            
    def get_lados_Mais(self):
        if(self.matriz[ self.x_atual ][self.y_atual]) == 'T' or self.matriz[ self.x_atual ][self.y_atual] == '+' :    
            if(self.orientacao_atual=='norte') :
                x = self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
            elif self.orientacao_atual=='sul':
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                  
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or  self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='oeste') :
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
              
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                   
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif  self.orientacao_atual=='este':
                x= self.x_atual
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
               
                x2 = self.x_atual
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
        else:   
            if(self.orientacao_atual=='norte'):
                x= self.x_atual
                y = self.y_atual +1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual +1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual+1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='sul'):
                
                x= self.x_atual
                y = self.y_atual -1
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                  
                    x = x-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual
                y1 = self.y_atual -1
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    x1 = x1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                x2 = self.x_atual
                y2 = self.y_atual-1
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    y2 = y2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
               
            elif(self.orientacao_atual=='oeste'):
                x= self.x_atual -1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or self.matriz[x][y] != 'I'  or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                    
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T'  or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
               
                x1= self.x_atual -1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                x2 = self.x_atual-1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2-1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x) +","+ str(y)+")","(" + str(x1) +","+ str(y1)+")" ,"(" + str(x2) +","+ str(y2)+")"]
                
            elif(self.orientacao_atual=='este'):
                x= self.x_atual +1
                y = self.y_atual
                while self.matriz[x][y] != 'o' or self.matriz[x][y] != 'T' or  self.matriz[x][y] != 'I' or self.matriz[x][y] != '+' or self.matriz[x][y] != ' ':
                   
                    y = y-1
                    if self.matriz[x][y] == 'o' or self.matriz[x][y] == 'T' or  self.matriz[x][y] == 'I' or self.matriz[x][y] == '+' or self.matriz[x][y] == ' ':
                        break
                x1= self.x_atual +  1
                y1 = self.y_atual
                while self.matriz[x1][y1] != 'o' or self.matriz[x1][y1] != 'T' or self.matriz[x1][y1] != 'I' or self.matriz[x1][y1] != '+' or self.matriz[x1][y1] != ' ':
                    y1 = y1+1
                    if self.matriz[x1][y1] == 'o' or self.matriz[x1][y1] == 'T' or  self.matriz[x1][y1] == 'I' or self.matriz[x1][y1] == '+' or self.matriz[x1][y1] == ' ':
                        break
                
                x2 = self.x_atual+1
                y2 = self.y_atual
                while self.matriz[x2][y2] != 'o' or self.matriz[x2][y2] != 'T' or  self.matriz[x2][y2] != 'I' or self.matriz[x2][y2] != '+' or self.matriz[x2][y2] != ' ':
                    x2 = x2+1
                    if self.matriz[x2][y2] == 'o' or self.matriz[x2][y2] == 'T' or  self.matriz[x2][y2] == 'I' or self.matriz[x2][y2] == '+' or self.matriz[x2][y2] == ' ':
                        break
                
                return ["("+ str(x1) +","+ str(y1)+")","(" + str(x) +","+ str(y)+")" ,"(" + str(x2) +","+ str(y2)+")"]
    
    def gauss(self):
        return        
                
    
    def run(self):
        if self.status != 0:
            print("Connection refused or error")
            quit()

        state = 'stop'
        stopped_state = 'run'

        while True:
            self.readSensors()

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
   

    def wander(self):
        center_id = 0
        left_id = 1
        right_id = 2
        back_id = 3
        
        if self.measures.compass <= 105 and self.measures.compass > 75 :
            self.orientacao_atual = 'oeste'
        elif self.measures.compass > -105 and self.measures.compass <= -75:
            self.orientacao_atual = 'este'
        elif self.measures.compass <= 15 and self.measures.compass > -15  :
            self.orientacao_atual = 'norte'
        elif  self.measures.compass > 165 or self.measures.compass <= -165:
            self.orientacao_atual = 'sul'      
        
        # elif self.measures.compass <= 50 and self.measures.compass > 40:
        #     self.orientacao_atual = 'noroeste'
        # elif self.measures.compass <= 140 and self.measures.compass > 130 :
        #     self.orientacao_atual = 'sudoeste'
        # elif  self.measures.compass > -140 or self.measures.compass <= -130:
        #     self.orientacao_atual = 'sudeste'      
        # elif  self.measures.compass > -55 or self.measures.compass <= -35:
        #     self.orientacao_atual = 'nordeste' 


        if self.cond_inicial=='true':
            self.x_atual = 10
            self.y_atual = 24 

            self.power_left = 0
            self.power_right = 0

            self.round_x = 0
            self.round_y = 0

            self.matriz[self.x_atual][self.y_atual] = 'I'
            self.char_atual = 'I'
            self.cond_inicial='false'
            self.bussola_antes = self.measures.compass

        else:
            self.out_left = ((self.power_left + self.out_left)/2) 
            self.out_right = ((self.power_right + self.out_right)/2) 

            self.lin =  (self.out_left +  self.out_right)/2

            y_calc =  self.lin*math.cos(self.bussola_antes*(math.pi/180))
            x_calc =  -self.lin*math.sin(self.bussola_antes*(math.pi/180))

            rot = (self.out_left +  self.out_right)
            self.angulo = self.angulo + rot
            self.round_x = self.round_x + x_calc
            self.round_y = self.round_y + y_calc
            self.x_atual = 10 + self.round_x
            self.y_atual = 24 + self.round_y         

            if(self.flag_verify == 'true'):
                if self.orientacao_atual == 'norte':
                    if self.y_atual + 0.438 < self.round_up_to_nearest_even_number(self.y_atual)-0.1  :
                        self.y_atual = self.y_atual -  0.438
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                    elif self.y_atual + 0.438 > self.round_up_to_nearest_even_number(self.y_atual)+0.1:
                        self.y_atual = self.y_atual +  0.438
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                    else:
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)

                elif self.orientacao_atual == 'sul':
                    if self.y_atual - 0.438 > self.round_down_to_nearest_even_number(self.y_atual)+0.1:
                        self.y_atual = self.y_atual +  0.438
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                    elif self.y_atual - 0.438 < self.round_down_to_nearest_even_number(self.y_atual)-0.1:
                        self.y_atual = self.y_atual -  0.438
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                    else:
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)

                elif self.orientacao_atual == 'este':
                    if self.x_atual + 0.438 < self.round_up_to_nearest_even_number(self.x_atual)-0.1:
                        self.x_atual = self.x_atual -  0.438
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)
                    elif self.x_atual + 0.438 > self.round_up_to_nearest_even_number(self.x_atual)+0.1:
                        self.x_atual = self.x_atual +  0.438
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)
                    else:
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)

                elif self.orientacao_atual == 'oeste':
                    if self.x_atual - 0.438 > self.round_down_to_nearest_even_number(self.x_atual)+0.1:
                        self.x_atual = self.x_atual +  0.438
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)
                    elif self.x_atual - 0.438 < self.round_down_to_nearest_even_number(self.x_atual)-0.1:
                        self.x_atual = self.x_atual -  0.438
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)
                    else:
                        self.x_atual = self.round_to_nearest_even_number(self.x_atual)
                        self.y_atual = self.round_to_nearest_even_number(self.y_atual)
            
                self.flag_verify = 'false'
               
            self.x_atual = round(self.x_atual)
            self.y_atual =round(self.y_atual)
            self.char_atual = self.matriz[self.x_atual][self.y_atual]
           
        if self.measures.lineSensor == ['0', '0', '0', '0', '0', '0', '0']:           
            if self.flag == 'nada_esquerda':              
                self.driveMotors(0.0,-0.15)
                self.power_left = 0.0
                self.power_right = -0.15               
                self.flag = 'nada'
            elif self.flag == 'nada_direita':
                
                self.driveMotors(-0.15,0.0)
                self.power_left = -0.15
                self.power_right = 0.0
                self.flag = 'nada'
            else:
                if (abs(self.x_atras -self.x_atual >=1) or abs(self.y_atras -self.y_atual >=1)):
                    self.tras =0
                self.x_atras= self.x_atual
                self.y_atras = self.y_atual
                self.tras= self.tras +1
                               
                if self.tras > 20 and self.matriz[self.x_atual][self.y_atual] != 'I' and self.matriz[self.x_atual][self.y_atual] != 'T' and self.matriz[self.x_atual][self.y_atual] != '+' and self.matriz[self.x_atual][self.y_atual] != 'o':
                    if  self.flag == 'frente':
                        if self.orientacao_atual == 'norte':
                            self.flag = '180_norte'
                        elif self.orientacao_atual == 'sul':
                            self.flag = '180_sul'
                        elif self.orientacao_atual == 'este':
                            self.flag = '180_este'
                        elif self.orientacao_atual == 'oeste':
                            self.flag = '180_oeste'                      
                        self.tras = 0
                    else:
                        self.tras = 0      
                    
                elif self.matriz[self.x_atual][self.y_atual] != 'I' and self.matriz[self.x_atual][self.y_atual] != '+' and self.turned_around != 'true':
                    self.matriz[self.x_atual][self.y_atual] = ' '
                
                else:
                    self.flag ='perdido'
                    self.perdi = self.perdi+1
                    if self.perdi == 20:
                        self.perdi= 0
                        self.matriz[self.x_atual][self.y_atual] = ' '
             
                self.power_left = -0.02
                self.power_right =-0.02
                self.driveMotors(-0.02,-0.02)           
        elif self.measures.lineSensor == ['1', '0', '0', '0', '0', '0', '0']:     
            self.power_left = -0.03
            self.power_right =0.0
            self.driveMotors(-0.03,0.00) 
        elif self.measures.lineSensor == ['0', '0', '0', '0', '0', '0', '1']:    
            self.power_left = 0.0
            self.power_right = -0.03
            self.driveMotors(0.00,-0.03)   

        if self.flag == 'frente_intersecao'  :
            self.turned_around = 'false'
            if self.count < 5:
                self.power_left = 0.15
                self.power_right = 0.15
                self.driveMotors(0.15,0.15)
                self.count = self.count + 1              
            else:
                self.flag = 'nada'
                self.count = 0
                self.boost = 0
        
        elif self.flag == 'left' : 
            self.power_left = -0.02
            self.power_right = 0.08
            self.driveMotors(-0.02,0.08)
            self.guarda_bits_nas_curvas.append(self.measures.lineSensor)
            
            if(self.orientacao_atual != self.orientacao_anterior):   
                self.flag = 'nada_esquerda'
                matriz_x = self.x_atual
                matriz_y = self.y_atual

                if self.intersecao_T == 'true':
                    for x in self.guarda_bits_nas_curvas[3:]:
                        if x[4:] == ['1','1','1']:
                            self.intersecao_MAIS = 'true'
                            self.intersecao_T = 'false'                      
                else:
                    for x in self.guarda_bits_nas_curvas:
                        if x[4:] == ['1','1','1']:
                            self.intersecao = 'true'

                if (self.matriz[matriz_x][matriz_y] != 'I') and (self.matriz[matriz_x][matriz_y] != '+') and (self.intersecao == 'true' or self.intersecao_T == 'true') and matriz_x %2==0 and matriz_y%2==0:       
                    if self.matriz[matriz_x][matriz_y] == 'o' :
                        aux = {Coordenadas(matriz_x,matriz_y).toString():[1]}
                        self.dic_Intersecoes.update(aux)

                    self.matriz[matriz_x][matriz_y] = 'T'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                    
                elif (self.matriz[matriz_x][matriz_y] != 'I' ) and self.intersecao_MAIS == 'true' and matriz_x %2==0 and matriz_y%2==0:
                    self.matriz[matriz_x][matriz_y] = '+'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                elif (self.matriz[matriz_x][matriz_y] != 'I') and (self.matriz[matriz_x][matriz_y] != '+' ) and (self.intersecao != 'true' or self.intersecao_T != 'true' or self.intersecao_MAIS != 'true') and (self.turned_around != 'true') and matriz_x%2==0 and matriz_y%2==0:
                    self.matriz[matriz_x][matriz_y] = 'o'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                self.guarda_bits_nas_curvas = []
               
        elif self.flag == 'right' :
            self.power_left = 0.08
            self.power_right = -0.02
            self.driveMotors(0.08,-0.02)
            
            self.guarda_bits_nas_curvas.append(self.measures.lineSensor)
            if(self.orientacao_atual != self.orientacao_anterior):
                self.flag = 'nada_direita'
                matriz_x = self.x_atual
                matriz_y = self.y_atual

                if self.intersecao_T == 'true':
                    for x in self.guarda_bits_nas_curvas[3:]:
                        
                        if x[:3] == ['1','1','1']:
                            self.intersecao_MAIS = 'true'
                            self.intersecao_T = 'false'             
                else:
                    for x in self.guarda_bits_nas_curvas:
                        if x[:3] == ['1','1','1']:
                            self.intersecao = 'true'
                    
                if (self.matriz[matriz_x][matriz_y] != 'I') and (self.matriz[matriz_x][matriz_y] != '+') and (self.intersecao == 'true' or self.intersecao_T == 'true') and matriz_x %2==0 and matriz_y%2==0:
                    if self.matriz[matriz_x][matriz_y] == 'o' :
                        aux = {Coordenadas(matriz_x,matriz_y).toString():[1]}
                        self.dic_Intersecoes.update(aux)
                    self.matriz[matriz_x][matriz_y] = 'T'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                        
                elif  (self.matriz[matriz_x][matriz_y] != 'I') and self.intersecao_MAIS == 'true' and matriz_x %2==0 and matriz_y%2==0:
                    self.matriz[matriz_x][matriz_y] = '+'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                        
                elif (self.matriz[matriz_x][matriz_y] != 'I') and (self.matriz[matriz_x][matriz_y] != '+' ) and (self.intersecao != 'true' or self.intersecao_T != 'true' or self.intersecao_MAIS != 'true') and (self.turned_around != 'true') and matriz_x%2==0 and matriz_y%2==0:
                    self.matriz[matriz_x][matriz_y] = 'o'
                    self.intersecao = 'false'
                    self.intersecao_T = 'false'
                    self.intersecao_MAIS = 'false'
                    
                self.guarda_bits_nas_curvas = []

        elif self.flag == '180_norte' :
            if self.orientacao_atual == 'sul':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.08
                self.power_right = 0.08
                self.driveMotors(-0.08,0.08)
        elif self.flag == '180_sul':
            if self.orientacao_atual == 'norte':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.08
                self.power_right = 0.08
                self.driveMotors(-0.08,0.08)
        elif self.flag == '180_este':
            if self.orientacao_atual == 'oeste':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.08
                self.power_right = 0.08
                self.driveMotors(-0.08,0.08)  
        elif self.flag == '180_oeste':
            if self.orientacao_atual == 'este':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.08
                self.power_right = 0.08
                self.driveMotors(-0.08,0.08)   
        elif self.flag == '180_norte1' :
            if self.orientacao_atual == 'sul':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.15
                self.power_right = 0.15
                self.driveMotors(-0.15,0.15)
        elif self.flag == '180_sul1':
            if self.orientacao_atual == 'norte':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.15
                self.power_right = 0.15
                self.driveMotors(-0.15,0.15)
        elif self.flag == '180_este1':
            if self.orientacao_atual == 'oeste':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.15
                self.power_right = 0.15
                self.driveMotors(-0.15,0.15)  
        elif self.flag == '180_oeste1':
            if self.orientacao_atual == 'este':
                self.flag = 'nada_180'
                self.turned_around = 'true'
            else:
                self.power_left = -0.15
                self.power_right = 0.15
                self.driveMotors(-0.15,0.15)    
        else:
            if self.measures.lineSensor == ['0', '1', '1', '1', '0', '0', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.04
                self.power_right = 0.09
                self.driveMotors(0.04,0.09)
                self.flag = 'frente'
                self.turned_around = 'false'
                              
            elif self.measures.lineSensor == ['0', '1', '1', '0', '0', '0', '0']:
                self.flag_verify = 'false'
                self.power_left = 0.07
                self.power_right = 0.09
                self.driveMotors(0.07,0.09)
                self.flag = 'frente'
                self.turned_around = 'false'
                
                
            elif self.measures.lineSensor == ['0', '0', '1', '1', '1', '0', '0']:
                self.flag_verify = 'false'
                self.power_left = 0.09
                self.power_right = 0.09
                self.driveMotors(0.09,0.09)
                self.flag = 'frente' 
                self.turned_around = 'false'

            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '0', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.09
                self.power_right = 0.08
                self.driveMotors(0.09,0.08)
                self.flag = 'frente'
                self.turned_around = 'false'
                        
            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.09
                self.power_right = 0.04
                self.driveMotors(0.09,0.04)
                self.flag = 'frente'
                self.turned_around = 'false'    
                
            elif self.measures.lineSensor == ['0', '0', '0', '0', '1', '1', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.09
                self.power_right = 0.07
                self.driveMotors(0.09,0.07)
                self.flag = 'frente'
                self.turned_around = 'false'
                               
            elif self.measures.lineSensor == ['0', '1', '1', '1', '1', '1', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.04
                self.power_right = 0.04
                self.driveMotors(0.04,0.04)
                self.flag = 'frente'
                self.turned_around = 'false'
                
            elif self.measures.lineSensor == ['0', '0', '1', '1', '0', '0', '0'] :
                self.flag_verify = 'false'
                self.power_left = 0.08
                self.power_right = 0.09
                self.driveMotors(0.08,0.09)
                self.flag = 'frente'
                self.turned_around = 'false'
                               
            elif self.measures.lineSensor == ['0', '0', '0', '1', '1', '1', '1']:
                self.flag_verify = 'true'
                if  self.next_Mais() == 'true':
                    if (self.check_left() == 'true' and self.check_right() != 'true'):                   
                        self.flag = 'right'
                    elif (self.check_left() == 'true' and self.check_right() == 'true'):
                        self.flag = 'frente_intersecao'
                    else:
                        self.flag = 'left'
                   
                elif self.next_T() == 'true':
                    if (self.check_right() == 'true') and (self.check__front() != 'true') :
                        self.flag = 'frente_intersecao'
                    elif (self.check_right() == 'true') and (self.check__front() == 'true') :
                        y = self.dic_Intersecoes_distancias.keys()
                        lista = list()
                                             
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                        
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])
                            f.write(" ")
                            f.write(string[1])
                            f.write(" ")
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))
                            f.write("\n")
                            
                        f.close()
                        lista = list()
                        lados = self.get_T_right()
                      
                        for x in self.dic_Intersecoes.keys():
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000                       
                        flag = 'B'
                        
                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux  and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'C'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux  and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'E1'                                             
                        if flag == 'C':   
                            self.flag = 'right'
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte1'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul1'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este1'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste1'
                        elif flag == 'E1':
                            self.flag = 'frente_intersecao'
                        else:
                            self.flag ='right'
                else:
                    self.flag = 'right'

            elif self.measures.lineSensor == ['0', '0', '1', '1', '1', '1', '1']:
                self.flag_verify = 'true'
                if  self.next_Mais() == 'true':
                    if (self.check_left() == 'true' and self.check_right() != 'true'):  
                        
                        self.flag = 'right'
                    elif (self.check_left() == 'true' and self.check_right() == 'true'):
                        self.flag = 'frente_intersecao'
                    else:
                        self.flag = 'left'

                elif self.next_T() == 'true':                   
                    if (self.check_right() == 'true') and (self.check__front() != 'true') :
                        self.flag = 'frente_intersecao'
                    elif (self.check_right() == 'true') and (self.check__front() == 'true') :
                        y = self.dic_Intersecoes_distancias.keys()                        
                        lista = list()                                             
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                        
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])
                            f.write(" ")
                            f.write(string[1])
                            f.write(" ")                       
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))                       
                            f.write("\n")
                            
                        f.close()
                        lista = list()
                        lados = self.get_T_right()
                       
                        for x in self.dic_Intersecoes.keys() :
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000                      
                        flag = 'B'
                        
                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                        for l in lista:
                            print("lados0:",lados[0])
                            print("lados1:",lados[1])
                            print("l:",l)
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'C'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'E'

                        if flag == 'C':                            
                            self.flag = 'right'
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte1'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul1'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este1'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste1'
                        elif flag == 'E':
                            self.flag = 'frente_intersecao'
                        else:
                            self.flag ='right'
                else:
                    self.flag = 'right'
              
            elif self.measures.lineSensor == ['1', '1', '1', '1', '0', '0', '0']:
                self.flag_verify = 'true'
            
                if  self.next_Mais() == 'true':
                    if (self.check_left() == 'true' and self.check_right() != 'true'):                          
                        self.flag = 'right'
                    elif (self.check_left() == 'true' and self.check_right() == 'true'):
                        self.flag = 'frente_intersecao'
                    else:
                        self.flag = 'left'
                elif self.next_T() == 'true':                  
                    if (self.check_left() == 'true') and (self.check__front() != 'true') :
                        self.flag = 'frente_intersecao'
                    elif (self.check_left() == 'true') and (self.check__front() == 'true') :
                        y = self.dic_Intersecoes_distancias.keys()                       
                        lista = list()
                           
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                                             
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])
                            f.write(" ")
                            f.write(string[1])
                            f.write(" ")
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))
                            f.write("\n")                           
                        f.close()
                        lista = list()
                        lados = self.get_T_right()
                       
                        for x in self.dic_Intersecoes.keys():                           
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000                     
                        flag = 'B'
                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                        for l in lista:
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'A1'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'E'

                        if flag == 'A1':                           
                            self.flag = 'left'                    
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte1'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul1'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este1'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste1'
                        elif flag == 'E':
                            self.flag = 'frente_intersecao'
                        else:
                            self.flag ='left'
                else:
                    self.flag = 'left'
      
            elif self.measures.lineSensor == ['1', '1', '1', '1', '1', '0', '0']:
                self.flag_verify = 'true'
                if  self.next_Mais() == 'true':
                    if (self.check_left() == 'true' and self.check_right() != 'true'):                         
                        self.flag = 'right'
                    elif (self.check_left() == 'true' and self.check_right() == 'true'):
                        self.flag = 'frente_intersecao'
                    else:
                        self.flag = 'left'

                elif self.next_T() == 'true':
                    if (self.check_left() == 'true') and (self.check__front() != 'true') :
                        self.flag = 'frente_intersecao'
                    elif (self.check_left() == 'true') and (self.check__front() == 'true') :
                        y = self.dic_Intersecoes_distancias.keys()
                        
                        lista = list()
                                              
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                                       
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])                           
                            f.write(" ")                          
                            f.write(string[1])                           
                            f.write(" ")                      
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))                       
                            f.write("\n")                           
                        f.close()
                        lista = list()
                        lados = self.get_T_left()

                        for x in self.dic_Intersecoes.keys():
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000
                        
                        flag = 'B'
                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                        for l in lista:
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'A2'
                            
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux and l != "("+str(self.x_atual)+","+str(self.y_atual)+")":
                                distancia = distancia_aux
                                flag = 'E'    
                        if flag == 'A2':
                            self.flag = 'left'
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte1'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul1'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este1'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste1'
                        elif flag == 'E':
                            self.flag = 'frente_intersecao'
                        else:
                            self.flag ='left'
                else:
                    self.flag = 'left'
                           
            elif self.measures.lineSensor == ['1', '1', '1', '1', '1', '1', '1']:
                self.flag_verify = 'true'
                self.intersecao_T = 'true'
                if self.next_T() == 'true' :
                    if (self.check_left() == 'true' and  self.check_right() != 'true' ):  
                        self.flag = 'right'
                        
                    elif self.check_left() == 'true' and self.check_right() == 'true':
                        y = self.dic_Intersecoes_distancias.keys()
                        lista = list()
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                        
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])
                            f.write(" ")
                            f.write(string[1])
                            f.write(" ")
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))
                            f.write("\n")
                        f.close()
                        lista = list()
                        lados = self.get_lados_T()

                        for x in self.dic_Intersecoes.keys():
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000                       
                        flag = 'B'

                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                        for l in lista:
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'A'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'C'

                            if self.matriz[self.x_atual][self.y_atual] != 'T':
                                if self.orientacao_atual == 'norte':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual+1)+")",l)
                                elif self.orientacao_atual == 'sul':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual-1)+")",l)
                                elif self.orientacao_atual == 'este':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual+1)+","+str(self.y_atual)+")",l)
                                elif self.orientacao_atual == 'oeste':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual-1)+","+str(self.y_atual)+")",l)
                            else:
                                distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual)+")",l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'D'
                                               
                        if flag == 'A':                          
                            self.flag = 'left'
                        elif flag == 'C':                          
                            self.flag = 'right'
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte1'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul1'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este1'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste1'
                        else:
                            self.flag ='left'   
                    else:
                         self.flag = 'left'
                         
                elif  self.next_Mais() == 'true':                 
                    if (self.check_left() == 'true' and self.check_right() != 'true'):                         
                        self.flag = 'right'
                    elif (self.check_right() == 'true' and  self.check_left() == 'true'):                     
                        y = self.dic_Intersecoes_distancias.keys()
                        lista = list()
                       
                        for l in self.dic_Intersecoes_distancias.keys():
                            lista.append(l)
                                               
                        for l in lista:
                            string = l.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            dist = self.dic_Intersecoes_distancias.get(l)
                            if int(string[2])%2==0 and int(string[3])%2==0 and int(string[0])%2==0 and int(string[1])%2==0:
                                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                            
                        f = open("grafo2.txt", "w").close()
                        f = open("grafo2.txt", "a")
                        
                        for h in self.dic_Intersecoes_distancias.keys():
                            string = h.split()
                            f.write(string[0])
                            f.write(" ")
                            f.write(string[1])
                            f.write(" ")
                            f.write(str(self.dic_Intersecoes_distancias.get(h)))
                            f.write("\n")
                        f.close()
                        lista = list()
                        lados = self.get_lados_Mais()

                        for x in self.dic_Intersecoes.keys():
                            string = x.replace("(","")
                            string = string.replace(")","")
                            string = string.replace(","," ")
                            string = string.split()
                            if int(string[0])%2==0 and int(string[1])%2==0 and (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                                lista.append(x)
                       
                        distancia = 1000
                        flag = 'B'
                    
                        if self.goToI == 'true':
                            lista = {"(10,24)"}
                        for l in lista:
                            print("lados0:",lados[0])
                            print("lados1:",lados[1])
                            print("l:",l)
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[0],l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'A'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[1],l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'C'
                            distancia_aux = self.algoritmo1("grafo2.txt",lados[2],l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                                flag = 'E'
                            if self.matriz[self.x_atual][self.y_atual] != '+':
                                if self.orientacao_atual == 'norte':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual+1)+")",l)
                                elif self.orientacao_atual == 'sul':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual-1)+")",l)
                                elif self.orientacao_atual == 'este':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual+1)+","+str(self.y_atual)+")",l)
                                elif self.orientacao_atual == 'oeste':
                                    distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual-1)+","+str(self.y_atual)+")",l)
                            else:
                                distancia_aux = self.algoritmo1("grafo2.txt","("+str(self.x_atual)+","+str(self.y_atual)+")",l)
                            if distancia > distancia_aux:
                                distancia = distancia_aux
                        if flag == 'A':
                            self.flag = 'left'
                        elif flag == 'C':
                            self.flag = 'right'
                        elif flag =='D':
                            self.turned_around = 'true'
                            if self.orientacao_atual == 'norte':
                                self.flag = '180_norte'
                            elif self.orientacao_atual == 'sul':
                                self.flag = '180_sul'
                            elif self.orientacao_atual == 'este':
                                self.flag = '180_este'
                            elif self.orientacao_atual == 'oeste':
                                self.flag = '180_oeste'
                        elif flag == 'E':
                            self.flag = 'frente_intersecao'
                        else:
                            self.flag ='left'
                    else:
                        self.flag = 'left'
                else:
                    self.flag = 'left'
                  
        matriz_x = self.x_atual
        matriz_y = self.y_atual
        
        if self.matriz[matriz_x][matriz_y] == ' ' and self.matriz[matriz_x][matriz_y] != 'T' and self.matriz[matriz_x][matriz_y] != 'o' and self.matriz[matriz_x][matriz_y] != '+' :
            if self.measures.compass < 100 and self.measures.compass > 80 or self.measures.compass > -100 and self.measures.compass < -80:
                if self.flag != 'right' and self.flag != 'left' and self.flag != '180_norte' and self.flag != '180_sul' and self.flag != '180_este' and self.flag != '180_oeste' and self.flag != 'nada_180' :
                    if self.matriz[matriz_x][matriz_y] == ' ' and matriz_x % 2 != 0 :
                        self.distancia = self.distancia +1 
                    self.matriz[matriz_x][matriz_y] = '|'         
                    
            elif self.measures.compass < 10 and self.measures.compass > -10  or  self.measures.compass > 170  or self.measures.compass < -170:
                if self.flag != 'right' and self.flag != 'left' and self.flag != '180_norte' and self.flag != '180_sul' and self.flag != '180_este' and self.flag != '180_oeste' and self.flag != 'nada_180' :
                    if self.matriz[matriz_x][matriz_y] == ' ' and matriz_y %2 != 0:
                        self.distancia = self.distancia +1 
                    self.matriz[matriz_x][matriz_y] = '-'
            
            elif -130 > int(self.measures.compass) > -140 and matriz_x % 2 != 0 and matriz_y % 2 != 0:
                self.matriz[abs(int(matriz_x))][int(matriz_y)] = '/'
            elif 40 < int(self.measures.compass) < 50 and matriz_x % 2 != 0 and matriz_y % 2 != 0:
                self.matriz[abs(int(matriz_x))][int(matriz_y) ] = '/'
            elif 130 < int(self.measures.compass) < 140 and matriz_x % 2 != 0 and matriz_y % 2 != 0:
                self.matriz[abs(int(matriz_x))][int(matriz_y)] = '\\'
            elif -40 > int(self.measures.compass) > -50 and matriz_x % 2 != 0 and matriz_y % 2 != 0:
                self.matriz[abs(int(matriz_x))][int(matriz_y)] = '\\'

                    
        if self.matriz[matriz_x][matriz_y] == 'T':
            if self.dic_Intersecoes.get(Coordenadas(matriz_x,matriz_y).toString()) == [1] and self.char_anterior!= self.char_atual:             
                aux = {Coordenadas(matriz_x,matriz_y).toString():[0]}
                self.dic_Intersecoes.update(aux)
 
            elif self.dic_Intersecoes.get(Coordenadas(matriz_x,matriz_y).toString()) != [0] and self.char_anterior!= self.char_atual:
                aux = {Coordenadas(matriz_x,matriz_y).toString():[1]}
                self.dic_Intersecoes.update(aux)
              
        elif self.matriz[matriz_x][matriz_y] == '+':
            contador = 0
            if self.matriz[matriz_x][matriz_y-1] != ' ':
                contador = contador +1
            if self.matriz[matriz_x][matriz_y+1] != ' ':
                contador = contador +1
            if self.matriz[matriz_x-1][matriz_y] != ' ':
                contador = contador +1
            if self.matriz[matriz_x+1][matriz_y] != ' ':
                contador = contador +1
            
            if contador == 4:
                aux = {Coordenadas(matriz_x,matriz_y).toString():[0]}
                self.dic_Intersecoes.update(aux)
            elif contador == 3:
                aux = {Coordenadas(matriz_x,matriz_y).toString():[0]}
                self.dic_Intersecoes.update(aux)
            elif contador == 2:
                aux = {Coordenadas(matriz_x,matriz_y).toString():[1]}
                self.dic_Intersecoes.update(aux)
            elif contador == 1:
                aux = {Coordenadas(matriz_x,matriz_y).toString():[2]}
                self.dic_Intersecoes.update(aux)
        elif self.matriz[matriz_x][matriz_y] == 'o':
            aux = {Coordenadas(matriz_x,matriz_y).toString():[0]}
            self.dic_Intersecoes.update(aux)
        
        self.coord_atuais = Coordenadas(matriz_x,matriz_y).toString()
      
        if  self.measures.ground != -1:
            if self.lista_beacons.get(Coordenadas(matriz_x,matriz_y).toString()) == None:
                self.lista_beacons.update({Coordenadas(matriz_x,matriz_y).toString():0})
            else:
                self.lista_beacons.update({Coordenadas(matriz_x,matriz_y).toString():self.lista_beacons.get(Coordenadas(matriz_x,matriz_y).toString()) +1})
        
            if self.lista_beacons.get(Coordenadas(matriz_x,matriz_y).toString()) > 5:
                self.coord_beacons.update({Coordenadas(matriz_x,matriz_y).toString():str(self.measures.ground)})
                self.beacons_mesmo.update({Coordenadas(matriz_x,matriz_y).toString():self.measures.ground})

        if self.beacons_mesmo.get(Coordenadas(matriz_x,matriz_y).toString()) != None or self.matriz[matriz_x][matriz_y] == 'I' or self.matriz[matriz_x][matriz_y] == 'T' or self.matriz[matriz_x][matriz_y] == '+' or self.matriz[matriz_x][matriz_y] == 'o':           
            if self.T_anterior != Coordenadas(matriz_x,matriz_y).toString():
                aux = {self.T_anterior + " " + Coordenadas(matriz_x,matriz_y).toString() :self.distancia}
                if self.distancia != 0 and self.distancia != -1:
                    if self.dic_Intersecoes_distancias.get(self.T_anterior + " " + Coordenadas(matriz_x,matriz_y).toString() ) == None:
                        self.dic_Intersecoes_distancias.update(aux)
                    elif self.dic_Intersecoes_distancias.get(self.T_anterior + " " + Coordenadas(matriz_x,matriz_y).toString() ) > self.distancia:
                        self.dic_Intersecoes_distancias.update(aux)
                self.T_anterior = Coordenadas(matriz_x,matriz_y).toString()
                self.T_x = matriz_x
                self.T_y = matriz_y
                self.distancia = 0
        
        self.coord_anteriores = self.coord_atuais
        self.char_anterior = self.char_atual
        self.bussola_antes = self.measures.compass
        self.orientacao_anterior = self.orientacao_atual
        somador = 0

        for x in  self.dic_Intersecoes.values():         
            somador = x[0] + somador
        
        conta_x = 10
        conta_y = 24
        cnt = 0
        condicao = 'false'
        if(self.matriz[matriz_x][matriz_y]== '+'):
            if self.matriz[matriz_x+1][matriz_y] != ' ' and self.matriz[matriz_x-1][matriz_y] != ' ' and self.matriz[matriz_x][matriz_y+1] and self.matriz[matriz_x][matriz_y-1] != ' ':
                condicao = 'true'
        elif (self.matriz[matriz_x][matriz_y]== 'T'):
            if self.matriz[matriz_x+1][matriz_y] != ' ':
                cnt = cnt+1
            if self.matriz[matriz_x-1][matriz_y] != ' ':
                cnt = cnt+1
            if self.matriz[matriz_x][matriz_y+1] != ' ':
                cnt = cnt+1
            if self.matriz[matriz_x][matriz_y-1] != ' ':
                cnt = cnt+1
            if cnt == 3:
                condicao = 'true'
        
        if self.measures.time == 4500 or somador== 0 and len(self.dic_Intersecoes.values()) >4  and condicao == 'true' and len(self.coord_beacons) >= int(self.nBeacons):
            self.goToI = 'true'

        if self.goToI == 'true' and self.matriz[matriz_x][matriz_y]=='I':
            self.goToI = 'done'

        if  self.goToI == 'done':
            y = self.dic_Intersecoes_distancias.keys()
            lista = list()
            self.path = list()
            for x in self.dic_Intersecoes_distancias.keys():
                if  (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                    lista.append(x)
            
            for l in lista:
                string = l.replace("(","")
                string = string.replace(")","")
                string = string.replace(","," ")
                string = string.split()
                dist = self.dic_Intersecoes_distancias.get(l)
                frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                    self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                
            f = open("grafo.txt", "w").close()
            f = open("grafo.txt", "a")
            
            for h in self.dic_Intersecoes_distancias.keys():
                string = h.split()
                f.write(string[0])                
                f.write(" ")               
                f.write(string[1])              
                f.write(" ")             
                f.write(str(self.dic_Intersecoes_distancias.get(h)))              
                f.write("\n")
            f.close()
            
            dic2 = dict()
            for x in self.beacons_mesmo:
                string = x.replace("(","")
                string = string.replace(")","")
                string = string.replace(","," ")
                string = string.split()
                if int(string[0])%2==0 and int(string[1])%2==0:
                    dic2.update({self.beacons_mesmo.get(x):x})
            
            distancia_auxiliar = 0
            distt = 1000       
            lista_path = list()
            lista_path.append(0)
            for i in range(0,len(dic2)-1):
                for j in range(0,len(dic2)):
                    print("ult",lista_path[-1])
                    print("dic2",dic2.get(j))
                    distancia_auxiliar = self.algoritmo1("grafo.txt",dic2.get(lista_path[-1]),dic2.get(j))
                    if distancia_auxiliar < distt and distancia_auxiliar != 0 and self.beacons_mesmo.get(dic2.get(j)) not in lista_path:
                        distt = distancia_auxiliar
                        menor_dist = dic2.get(j)
                lista_path.append(self.beacons_mesmo.get(menor_dist))    
                distancia_auxiliar = 0
                distt = 1000   
                        
            ultima_lista = list()
            for x in lista_path:
                ultima_lista.append(dic2.get(x))

            for i in range(0,len(lista_path)-1): 
                for j in range(i+1,i+2):
                    self.algoritmo("grafo.txt",ultima_lista[i],ultima_lista[j])

            print(ultima_lista[-1])
            print(dic2.get(0))
            self.algoritmo("grafo.txt",ultima_lista[-1],dic2.get(0))
            self.path.append(self.path[0])

            self.path = self.path    
                    
            f = open("myrob.path", "w").close()
            f = open("myrob.path", "a")
            indice = 0
            cortar = 'false'
            for i in range(0,len(self.path)-1): 
                if (self.path[i] == self.path[i+1] and self.path[i] == '(10,24)'):
                    indice = i
                    cortar = 'true'
            
            if cortar == 'true':
                self.path = self.path[0:indice+1]

            x_anterior = 0
            y_anterior = 0
            for l in self.path:
                string = l.replace("(","")
                string = string.replace(")","")
                string = string.replace(","," ")
                string = string.split()
                x =  int(string[1]) - 24
                y =  -(int(string[0]) - 10)
                
                if x - x_anterior > 2 :
                      
                    auxxilar = int((x - x_anterior)/2)
                    for yy in range(0,auxxilar-1):
                        f.write(str(x_anterior + (yy+1)*2 ))
                        f.write(" ")
                        f.write(str(y))
                        f.write('\n')  
                                         
                    x_anterior = x
                    y_anterior = y
                elif x - x_anterior < -2 :
                    auxxilar = int(-(x - x_anterior)/2)
                    for yy in range(0,auxxilar-1):
                        f.write(str(x_anterior - (yy+1)*2 ))
                        f.write(" ")
                        f.write(str(y))
                        f.write('\n')
                     
                    x_anterior = x
                    y_anterior = y
                elif y - y_anterior > 2 :                        
                    auxxilar = int((y - y_anterior)/2)
                    for yy in range(0,auxxilar-1):
                        f.write(str(x))
                        f.write(" ")
                        f.write(str(y_anterior + (yy+1)*2 ))
                        f.write('\n')
                      
                    x_anterior = x
                    y_anterior = y
                elif y - y_anterior < -2 :
                    
                    auxxilar = int(-(y - y_anterior)/2)
                    for yy in range(0,auxxilar-1):
                        f.write(str(x))
                        f.write(" ")
                        f.write(str(y_anterior - (yy+1)*2 ))
                        f.write('\n')
                    x_anterior = x
                    y_anterior = y
                else:                  
                    x_anterior = x
                    y_anterior = y

                f.write(str(x))
                f.write(" ")
                f.write(str(y))
                f.write('\n')
                
            f.close()
            self.finish()

            for l in range(21):
                for c in range(49):
                    if c % 2 == 0:
                        if self.matriz[l][c] == 'o' or self.matriz[l][c] == '-' or self.matriz[l][c] == '/' or self.matriz[l][c] == '\\':
                            self.matriz[l][c] = ' '
        
            for c in range(49):
                for l in range(21):
                    if l % 2 == 0:
                        if self.matriz[l][c] == 'o' or self.matriz[l][c] == '|' or self.matriz[l][c] == '/' or self.matriz[l][c] == '\\':
                            self.matriz[l][c] = ' '

            f = open("grafo.txt", "w").close()
            f = open("grafo2.txt", "w").close()
            f = open("myrob.map", "w").close()
            conta_x = 0
            conta_y = 0
            for x in self.matriz:
                conta_y=0
                for y in x:
                    f = open("myrob.map", "a")
                    if y=='T' or y =='o' or y=='+':
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    elif y=='|' and conta_x%2 == 0:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    elif y=='-' and conta_y%2 == 0:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    else:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(y)                     
                    conta_y = conta_y + 1
                conta_x = conta_x + 1    
                f.write('\n')
                f.close()
       
        if self.update_file > 150 and self.flag == 'frente':
            print(len(self.coord_beacons))
            print(self.nBeacons )
           
            if len(self.coord_beacons) >= int(self.nBeacons) :              
                self.path = list()
                y = self.dic_Intersecoes_distancias.keys()
                lista = list()
                for x in self.dic_Intersecoes_distancias.keys():      
                    if  (self.dic_Intersecoes.get(x) ==[1] or self.dic_Intersecoes.get(x) ==[2]):
                        lista.append(x)
                
                for l in lista:
                    string = l.replace("(","")
                    string = string.replace(")","")
                    string = string.replace(","," ")
                    string = string.split()
                    dist = self.dic_Intersecoes_distancias.get(l)
                    
                    frase = (Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString()
                    if self.dic_Intersecoes_distancias.get(frase) == None or self.dic_Intersecoes_distancias.get(frase) > dist:
                        self.dic_Intersecoes_distancias.update( {(Coordenadas(int(string[2]),int(string[3])).toString()) + " " + (Coordenadas(int(string[0]),int(string[1]))).toString() : dist})
                    
                f = open("grafo.txt", "w").close()
                f = open("grafo.txt", "a")
                
                for h in self.dic_Intersecoes_distancias.keys():
                    string = h.split()
                    f.write(string[0])                   
                    f.write(" ")                   
                    f.write(string[1])                   
                    f.write(" ")               
                    f.write(str(self.dic_Intersecoes_distancias.get(h)))
                    f.write("\n")                   
                f.close()
                
                dic2 = dict()
                for x in self.beacons_mesmo:
                    string = x.replace("(","")
                    string = string.replace(")","")
                    string = string.replace(","," ")
                    string = string.split()
                    if int(string[0])%2==0 and int(string[1])%2==0:
                        dic2.update({self.beacons_mesmo.get(x):x})

                distancia_auxiliar = 0
                distt = 1000
                
                lista_path = list()
                lista_path.append(0)
                for i in range(0,len(dic2)-1):
                    for j in range(0,len(dic2)):
                        print("ult",lista_path[-1])
                        print("dic2",dic2.get(j))
                        distancia_auxiliar = self.algoritmo1("grafo.txt",dic2.get(lista_path[-1]),dic2.get(j))
                        if distancia_auxiliar < distt and distancia_auxiliar != 0 and self.beacons_mesmo.get(dic2.get(j)) not in lista_path:
                            distt = distancia_auxiliar
                            menor_dist = dic2.get(j)
                    lista_path.append(self.beacons_mesmo.get(menor_dist))    
                    distancia_auxiliar = 0
                    distt = 1000   
                            
                ultima_lista = list()
                for x in lista_path:
                    ultima_lista.append(dic2.get(x))
            
                for i in range(0,len(lista_path)-1): 
                    for j in range(i+1,i+2):
                        
                        self.algoritmo("grafo.txt",ultima_lista[i],ultima_lista[j])

                print(ultima_lista[-1])
                print(dic2.get(0))
                self.algoritmo("grafo.txt",ultima_lista[-1],dic2.get(0))
                self.path.append(self.path[0])

                print(self.path)
                self.path = self.path
                     
                f = open("myrob.path", "w").close()
                f = open("myrob.path", "a")
                indice = 0
                cortar = 'false'
                for i in range(0,len(self.path)-1): 
                    if (self.path[i] == self.path[i+1] and self.path[i] == '(10,24)'):
                        indice = i
                        cortar = 'true'
                
                if cortar == 'true':
                    self.path = self.path[0:indice+1]
             
                x_anterior = 0
                y_anterior = 0
                for l in self.path:
                    string = l.replace("(","")
                    string = string.replace(")","")
                    string = string.replace(","," ")
                    string = string.split()
                    x =  int(string[1]) - 24
                    y =  -(int(string[0]) - 10)
                    
                    if x - x_anterior > 2 :
                        
                        auxxilar = int((x - x_anterior)/2)
                        for yy in range(0,auxxilar-1):
                            f.write(str(x_anterior + (yy+1)*2 ))
                            f.write(" ")
                            f.write(str(y))
                            f.write('\n')  
                                            
                        x_anterior = x
                        y_anterior = y
                    elif x - x_anterior < -2 :
                        
                        auxxilar = int(-(x - x_anterior)/2)
                        for yy in range(0,auxxilar-1):
                            f.write(str(x_anterior - (yy+1)*2 ))
                            f.write(" ")
                            f.write(str(y))
                            f.write('\n')
                        
                        x_anterior = x
                        y_anterior = y
                    elif y - y_anterior > 2 :   
                                    
                        auxxilar = int((y - y_anterior)/2)
                        for yy in range(0,auxxilar-1):
                            f.write(str(x))
                            f.write(" ")
                            f.write(str(y_anterior + (yy+1)*2 ))
                            f.write('\n')
                        
                        x_anterior = x
                        y_anterior = y
                    elif y - y_anterior < -2 :
                        
                        auxxilar = int(-(y - y_anterior)/2)
                        for yy in range(0,auxxilar-1):
                            f.write(str(x))
                            f.write(" ")
                            f.write(str(y_anterior - (yy+1)*2 ))
                            f.write('\n')
                        
                        x_anterior = x
                        y_anterior = y

                    else:                  
                        x_anterior = x
                        y_anterior = y


                    f.write(str(x))
                    f.write(" ")
                    f.write(str(y))
                    f.write('\n')
                    
                f.close()
                
                f = open("grafo.txt", "w").close()
    

            
            self.update_file = 0
            f = open("myrob.map", "w").close()
            conta_x = 0
            conta_y = 0
            for x in self.matriz:
                conta_y=0
                for y in x:
                    f = open("myrob.map", "a")
                    if y=='T' or y =='o' or y=='+':
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    elif y=='|' and conta_x%2 == 0:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    elif y=='-' and conta_y%2 == 0:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(' ')
                    else:
                        if self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")") != None:
                            f.write(self.coord_beacons.get("("+str(conta_x)+","+str(conta_y)+")"))
                        else:
                            f.write(y)
                        
                        
                    conta_y = conta_y + 1
                conta_x = conta_x + 1    
                f.write('\n')
                f.close()

        self.update_file = self.update_file +1
    
        
        
   
        
        
        

    
class Coordenadas():
   
    def __init__(self, x,y):
        self.x = x
        self.y= y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def toString(self):
        return '(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
    

        

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