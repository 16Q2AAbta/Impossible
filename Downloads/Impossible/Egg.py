import pygame
from Player import *
from FinishLine import *
class Egg():
    def __init__(self,game,player,finishline,x,y,image):
        self.image = image
        self.player = player
        self.finishline = finishline
##        self.x = x
##        self.y = y
        self.game = game
        self.image2 = pygame.image.load(self.image).convert_alpha()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.Starty = y
        self.collide = False
        self.topCollide = True
        self.capture = False
        self.StartY = y
    def collosion(self):
        if self.player.rect.colliderect(self.rect):
            self.capture = True


            
                


    def draw(self):
        if self.finishline.playerFinish == False:
            if self.capture == False:
                self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
    def update(self):
        self.draw()
        self.collosion()
