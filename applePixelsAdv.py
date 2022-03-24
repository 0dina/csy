from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#color of parts
b =(255, 51, 51) #body
h =(220, 129, 76) #head
l =(102, 204, 0) #leaf
g =(100,100,100) #BG

apple = {
    'leaf' : {'color' : l,
              'pos' : [(4,1)]
              },
    'head' : {'color' : h,
              'pos' : [(3,2),(3,3)]
              },
    'body' : {'color' : b,
              'pos' : [(2,3),(4,3),(1,4),(2,4),(3,4),(4,4),
                       (5,4),(1,5),(2,5),(3,5),(4,5),(5,5),
                       (1,6),(2,6),(3,6),(4,6),(5,6),
                       (2,7),(3,7),(4,7)]
              },
    'bg' : {'color' : g,
            'pos' : [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                     (0,1),(1,1),(2,1),(3,1),(5,1),(6,1),(7,1),(0,2),
                     (1,2),(2,2),(4,2),(5,2),(6,2),(7,2),(0,3),(1,3),
                     (5,3),(6,3),(7,3),(0,4),(6,4),(7,4),(0,5),(6,5),
                     (7,5),(0,6),(6,6),(7,6),(0,7),(1,7),(5,7),(6,7),
                     (7,7)]
                     }
            
    }


#sense.clhead()



sense.clear()

'''
for pos in apple['leaf']['pos']:
    sense.set_pixel(pos[0], pos[1], apple['leaf']['color'])
    sleep(0.1)

for pos in apple['head']['pos']:
    sense.set_pixel(pos[0], pos[1], apple['head']['color'])
    sleep(0.1)
    
for pos in apple['body']['pos']:
    sense.set_pixel(pos[0], pos[1], apple['body']['color'])
    sleep(0.1)
'''
def drawApple():
    sense.clear()
    for part in apple:
        for pos in apple[part]['pos']:
            rgb = apple[part]['color']
            sense.set_pixel(pos[0], pos[1], rgb)
            
                
def drawPart(part):
    for pos in apple[part]['pos']:
        rgb = apple[part]['color']
        sense.set_pixel(pos[0], pos[1], rgb)            
            
displacement = -1
intensitiy = 1
while True:
  
    #drawApple()
    sense.clear()
    sleep(2)
    drawPart('head')
    sleep(2)
    drawPart('body')
    sleep(2)
    drawPart('leaf')
    sleep(2)
    drawPart('bg')
    sleep(5)



