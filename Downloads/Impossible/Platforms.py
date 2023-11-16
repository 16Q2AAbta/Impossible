import pygame
from Player import *
from FinishLine import *
class Platform():
    def __init__(self,game,player,finishline,x,y,image):
        self.image = image
        self.player = player
        self.finishline = finishline
##        self.x = x
##        self.y = y
        self.game = game
        self.StartY = y
        self.image2 = pygame.image.load(self.image).convert()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collide = False
        self.topCollide = True
    def collosion(self):
        if self.player.rect.colliderect(self.rect):
            if self.player.direction == "right" and self.player.rect.right <= self.rect.left + 10 :  
                self.player.rect.right = self.rect.left
            elif self.player.direction == "left" and self.player.rect.left >= self.rect.right - 10:  
                self.player.rect.left = self.rect.right
            else:
                 if self.player.rect.bottom >= self.rect.bottom:
                    self.player.jumpIsTrue = False
                    self.player.jumpCount = 15

                 elif self.player.rect.top <= self.rect.bottom:
                    self.player.rect.bottom = self.rect.top
                    self.player.collide = True
                    self.topCollide = True
                 if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.left - self.player.rect.width:
                    self.player.x = self.rect.left - self.player.rect.width
                    self.player.collide = False
                    self.player.isJumping = False
                 if self.player.rect.left < self.rect.right and self.player.rect.right > self.rect.right + self.player.rect.width:
                    self.player.x = self.rect.right
                    self.player.collide = False
                    self.player.isJumping = False
            
            
                


    def draw(self):
        if self.finishline.playerFinish == False:
            self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
    def update(self):
        self.draw()
        self.collosion()
class movingPlatform(Platform):
    def __init__(self,game,player,finishline,x,y,endX,direction,image):
        self.player = player
        self.finishline = finishline
        self.image = image
        self.image2 = pygame.image.load(self.image).convert()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.startX = x
        self.endX = endX
        self.game = game
        self.collide = False
        self.direction = direction
        self.StartY = y
    def move(self):
        if self.direction == "right":
            self.rect.x += 1
            if self.rect.x == self.endX:
                self.direction = "left"
        if self.direction == "left":
            self.rect.x -= 1
            if self.rect.x == self.startX:
                self.direction = "right"
    def collosion(self):
        if self.player.rect.colliderect(self.rect):
            if self.player.direction == "right" and self.player.rect.right <= self.rect.left + 10 :  
                self.player.rect.right = self.rect.left 
            elif self.player.direction == "left" and self.player.rect.left >= self.rect.right - 10:  
                self.player.rect.left = self.rect.right
            else:
                 if self.player.rect.bottom >= self.rect.bottom:
                    self.player.jumpIsTrue = False
                 elif self.player.rect.top <= self.rect.bottom:
                    self.player.rect.bottom = self.rect.top
                    self.player.collide = True
                    if self.direction == "right":
                        self.player.rect.x += 1
                    if self.direction == "left":
                        self.player.rect.x -= 1
                 if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.left - self.player.rect.width:
                        self.player.x = self.rect.left - self.player.rect.width
                        self.player.collide = False
                 if self.player.rect.left < self.rect.right and self.player.rect.right > self.rect.right + self.player.rect.width:
                        self.player.x = self.rect.right
                        self.player.collide = False 

    def update(self):
        self.draw()
        self.collosion()
        self.move()
        
class fakePlatform(Platform):
    def __init__(self,game,player,finishline,x,y,image):
        self.image = image
        self.player = player
        self.finishline = finishline
        self.game = game
        self.image2 = pygame.image.load(self.image).convert()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collide = False
        self.StartY = y
    def collosion(self):
        x = 1
