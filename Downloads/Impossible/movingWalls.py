import pygame
from Player import *
from FinishLine import *
class movingWall():
    def __init__(self,game,player,finishline,x,y,endY,direction,image):
        self.image = image
        self.player = player
        self.finishline = finishline
        self.startY = y
        self.endY = endY
        self.game = game
        self.image2 = pygame.image.load(self.image).convert()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collide = False
        self.direction = direction
        self.defualtstartY = y
        self.defualtendY = endY
        
    def draw(self):
        if self.finishline.playerFinish == False:
                self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
    def collosion(self):
        if self.player.rect.colliderect(self.rect):
            if self.player.direction == "right" and self.player.rect.right <= self.rect.left + 10 :  
                self.player.rect.right = self.rect.left 
            elif self.player.direction == "left" and self.player.rect.left >= self.rect.right - 10:  
                self.player.rect.left = self.rect.right
            else:
                 if self.player.rect.bottom >= self.rect.bottom:
                    self.player.rect.y += 5
                    self.player.jumpIsTrue = False
                    self.player.jumpCount = 15

                 elif self.player.rect.top <= self.rect.bottom:
                    self.player.rect.bottom = self.rect.top
                    self.player.collide = True
                    if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.left - self.player.rect.width:
                                    self.player.x = self.rect.left - self.player.rect.width
                                    self.player.collide = False
                    if self.player.rect.left < self.rect.right and self.player.rect.right > self.rect.right + self.player.rect.width:
                                    self.player.x = self.rect.right
                                    self.player.collide = False
    def move(self):
        if self.direction == "up":
            self.rect.y -= 1
            if self.rect.y == self.endY:
                self.direction = "down"
        if self.direction == "down":
            self.rect.y += 1
            if self.rect.y == self.startY:
                self.direction = "up"
    def update(self):
        self.draw()
        self.collosion()
        self.move()
