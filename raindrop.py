'''
name: Rain Art
hardware: RPI sensor HAT 
author : CHOI SY
support : BAEK DS
edit: 2020.1.20
'''
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

'''plate = {'xyPos' : (4,7),
         'color' : (100,0,100)}
'''


#case1
g = (0,0,0)

a = (0,50,50)
b = (0,100,100)
c = (0,200,200)
d = (0,255,255)

#case2
e = (0,0,0)#start
f = (50,50,50)
q = (100,100,100)

h = (150,150,150)
i = (200,200,200)
j = (255,255,255)

x1 = 0
x2 = 3

drops=[]
       
rain1 = [{'xy':(x1,0), 'color':j},
        {'xy':(x1,-1), 'color':i},
        {'xy':(x1,-2), 'color':h},
        {'xy':(x1,-3), 'color':q}]  #딕트 리스트, C언어에서 구조체 배열과 닮은꼴

rain2 = [{'xy':(x2,0), 'color':a},
        {'xy':(x2,-1), 'color':b},
        {'xy':(x2,-2), 'color':c},
        {'xy':(x2,-3), 'color':d}]  #딕트 리스트, C언어에서 구조체 배열과 닮은꼴
        
# define dictionary : rain
# property1 : x start postion
# part + color
# speedY

rain={}
rain['rain1'] = rain1
rain['rain2'] = rain2

def draw_rain(rainData, x,y):
    global drops 
    #반복 4번
    for i in range(4):
        y = y - i
        #print('1xy=',x,y)
        if( 0<= y <=7):
            n = x + (y*8)
            #print('rain1=',n)
            part = rainData[i]
            drops[n] = part['color']

    sense.set_pixels(drops)

    
    
y1 =0        
        
while True:

    x1 = 3  #randint(0,5)
    x2 = randint(0,5)
    drops =[g for i in range(64)]
    draw_rain(rain1, x1, y1)
    
    if y1==7:
        y1=0
    else:
        y1+=1
    #draw_rain(rain2)

        
    sleep(0.2)
  
