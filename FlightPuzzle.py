#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 17:45:58 2018

@author: an-chiangchu
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 300))
done = False
y1 = 50
y2 = 100 
y3 = 150 
x1=0
x2=0
x3=0
width=30
height=10
of = 180
o1 = 180
o2 = 180
o3 = 180
t= 0
speed  = 2

while not done:
        pygame.time.delay(30)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((0,0,0))
        t+=1
        if (t<45):
            x1+= speed
            x2+= speed
            x3+= speed
            o3 -= 3
        elif (t >= 45 and t< 90):
            x1 += 1*speed
            x2 += 1*speed
            x3 -= 1*speed
            o2 -= 2
            o3 -= 1
        elif (t >= 90 and t< 180):
            x1 += 1*speed
            x2 += -1*speed
            o2 -= 1
            o1 -= 1
            o3 = of
        elif (t >= 180 and t< 270):
            x1 += -1*speed
            x3 += 1*speed
            o3 -= 1
            o1 -= 1
            o2 = of
        elif (t >= 270 and t< 315):
            x1 += -1*speed
            x2 += 1*speed
            x3 += -1*speed
            o3 -= 2
            o1 -= 0
            o2 -= 1
        elif (t >= 315 and t< 360):
            x1 += -1*speed
            x2 += -1*speed
            x3 += -1*speed
            o3 -= 0
            o1 -= 0
            o2 -= 3
        else:
            pass 
        pygame.draw.rect(screen, (255,0,0),(x1,y1, 0.2*of,height))
        pygame.draw.rect(screen, (255,250,0),(x1,y1, 0.2*o1,height))
        pygame.draw.rect(screen, (255,0,0),(x2,y2,  0.2*of,height))
        pygame.draw.rect(screen, (255,250,0),(x2,y2, 0.2*o2,height))
        pygame.draw.rect(screen, (255,0,0),(x3,y3,  0.2*of,height))
        pygame.draw.rect(screen, (255,250,0),(x3,y3, 0.2*o3,height))
        
        
        pygame.display.flip()


pygame.quit()