import pygame
from Player import *
from FinishLine import *
class Spike():
    def __init__(self,game,player,finishline,x1,x2,x3,y1,y2,y3,color):
        self.player = player
        self.color = color
        self.game = game
        self.finishline = finishline
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y3
        self.x3 = x3
        self.y3 = y2
        self.dissapear = False
        self.y1Start = y1
        self.y2Start = y3
        self.y3Start = y2 
    def draw(self):
            if self.finishline.playerFinish == False:
                pygame.draw.polygon(self.game.screen,self.color, points=[(self.x1,self.y1), (self.x2,self.y2), (self.x3,self.y3)])
    def collosion(self):
        n = 0
        m = 0
#Iterates through each point in the player
        for i in range(6):
            if i == 1:
                n = 0
                m = 0
            if i == 2:
                n = 12
                m = 25
            if i == 3:
                n = 25
                m = 50
            if i == 4:
                n = 0
                m = 50
            if i == 5:
                n = 25
                m = 0
#Uses Herons Formula which takes two points of the triangle and a point of a sprite and compares it to the area of the triangle and if equal it means they have collided.    
            areaOrig = abs( (self.x2-self.x1)*(self.y3-self.y1) - (self.x3-self.x1)*(self.y2-self.y1) )
            area1 =    abs( (self.x1-(self.player.rect.x+n))*(self.y2-(self.player.rect.y+m)) - (self.x2-(self.player.rect.x+n))*(self.y1-(self.player.rect.y+m)) )
            area2 =    abs( (self.x2-(self.player.rect.x+n))*(self.y3-(self.player.rect.y+m)) - (self.x3-(self.player.rect.x+n))*(self.y2-(self.player.rect.y+m)) )
            area3 =    abs( (self.x3-(self.player.rect.x+n))*(self.y1-(self.player.rect.y+m)) - (self.x1-(self.player.rect.x+n))*(self.y3-(self.player.rect.y+m)) )
            if (area1 + area2 + area3 == areaOrig):
                self.player.IsDead = True
    def update(self):
        self.draw()
        self.collosion()
class movingSpike(Spike):
    def __init__(self,game,player,finishline,x1,x2,x3,y1,y2,y3,color,endx,direction,speed):
        self.player = player
        self.color = color
        self.game = game
        self.finishline = finishline
        self.direction = direction
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y3
        self.x3 = x3
        self.y3 = y2
        self.spawnx1 = x1
        self.spawny1 = y1
        self.spawnx2 = x2
        self.spawny2 = y3
        self.spawnx3 = x3
        self.spawny3 = y2
        self.endX = endx
        self.startX = x1
        self.dissapear = False
        self.speed = speed
        self.y1Start = y1
        self.y2Start = y3
        self.y3Start = y2 
    def draw(self):
        if self.dissapear == False:
            if self.finishline.playerFinish == False:
                pygame.draw.polygon(self.game.screen,self.color, points=[(self.x1,self.y1), (self.x2,self.y2), (self.x3,self.y3)])
    def move(self):
        if self.dissapear == False:
            if self.direction == "right":
                self.x1 += self.speed
                self.x2 += self.speed
                self.x3 += self.speed
                if self.x1 == self.endX:
                       self.dissapear = True
                       self.x1 = self.spawnx1
                       self.x2 = self.spawnx2
                       self.x3 = self.spawnx3
                       self.dissapear = False
            if self.direction == "left":
                self.x1 -= self.speed
                self.x2 -= self.speed
                self.x3 -= self.speed
                if self.x1 == self.endX:
#Respwans the spike back to its positions
                    self.dissapear = True
                    self.x1 = self.spawnx1
                    self.x2 = self.spawnx2
                    self.x3 = self.spawnx3
                    self.dissapear = False
    def update(self):
        self.draw()
        self.collosion()
        self.move()
