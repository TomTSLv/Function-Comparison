import time
import random
import pygame
from pygame.locals import *
import os.path
import sys
import Functions


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BAR_HEIGHT = 30
MARGIN_LEFT = 30
MARGIN_RIGHT = 30
MARGIN_TOP = 30
FONT_SIZE = 20
myfont = pygame.font.SysFont("arial", FONT_SIZE)

pygame.display.set_caption('Time Graph')

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))

def timer(f, *p):
    begin_time = time.clock()
    f(*p)
    end_time = time.clock()
    
    return(end_time - begin_time)

def main():
    functionList=[Functions.countEvens,
                  Functions.myMin,
                  Functions.myMax,
                  Functions.median,
                  Functions.secondBiggest,
                  Functions.LIS,
                  Functions.dot,
                  Functions.instersect1,
                  Functions.instersect2,
                  Functions.fib2]
    sim(functionList)

def randColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def sim(functionList):
    global screen
    global myfont
    value=5
    step=5
    count=0
    pointsList=[]
    yAxis=[]
    color=[]
    running=True
    highest=0
    pause=False
    default=0
    nameList=[functionList[i].__name__ for i in range(len(functionList))]
    for function in functionList:
        pointsList.append([])
        yAxis.append([])
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==KEYDOWN:
                if event.key==K_e:
                    running=False
                if event.key==K_p and pause==True:
                    default=0
                    count=0
            else:
                if default==1:
                    spam=100
                else: 
                    while count>=0:
                        screen.fill((0, 0, 0))
                        if pause==True:
                            pause=False
                            count=flag
                        for function in functionList:
                            pointsList[functionList.index(function)].append((value,timer(function,value)))
                            yAxis[functionList.index(function)].append(timer(function,value))
                            color.append(randColor())
                        for function in yAxis:
                            for y in function:
                                if y>highest:
                                   highest=y
                        for i in range (len(functionList)):
                            script = myfont.render(nameList[i] + ': ' + str(yAxis[i][-1]),1,color[i])
                            instruction1=myfont.render('Press E to exit.(Please exit when paused)',1,(255,255,255))
                            instruction2=myfont.render('Press P to pause and continue.',1,(255,255,255))
                            screen.blit(script,(SCREEN_WIDTH*0.06,SCREEN_HEIGHT*0.04*(i+3)))
                            screen.blit(instruction1,(0,0))
                            screen.blit(instruction2,(0,15))
                        for function in functionList:          
                            if count>=2:
                                # N=len(pointsList[functionList.index(function)])
                                for i in range(1,len(pointsList[functionList.index(function)])):
                                    # pointPrev=(SCREEN_WIDTH*pointsList[functionList.index(function)][i-1][0]/N, \
                                    #     SCREEN_HEIGHT-SCREEN_HEIGHT*pointsList[functionList.index(function)][i-1][1]/highest)
                                    # pointCurrent=(SCREEN_WIDTH*pointsList[functionList.index(function)][i][0]/N,\
                                    #     SCREEN_HEIGHT-SCREEN_HEIGHT*pointsList[functionList.index(function)][i][1]/highest)
                                    # pygame.draw.line(screen,color[functionList.index(function)],pointCurrent,pointPrev)
                                    pointPrev=(pointsList[functionList.index(function)][i-1][0],SCREEN_HEIGHT-SCREEN_HEIGHT*pointsList[functionList.index(function)][i-1][1]/highest)
                                    pointCurrent=(pointsList[functionList.index(function)][i][0],SCREEN_HEIGHT-SCREEN_HEIGHT*pointsList[functionList.index(function)][i][1]/highest)
                                    pygame.draw.line(screen,color[functionList.index(function)],pointCurrent,pointPrev)    
                        value+=step
                        count+=1
                        pygame.display.update()
                        if event.type==KEYDOWN:
                            if event.key==K_p:
                                pause=True
                                flag=count
                                count=-1
                        event=pygame.event.poll()
        pygame.display.update()
    pygame.quit()

main()
