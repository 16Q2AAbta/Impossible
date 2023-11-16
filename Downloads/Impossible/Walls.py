import pygame
from Player import *
from FinishLine import *
class Wall():
    def __init__(self,game,player,finishline,x,y,image):
        self.image = image
        self.player = player
        self.finishline = finishline
        self.game = game
        self.image2 = pygame.image.load(self.image).convert()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.StartY = y
        self.collide = False
    def collosion(self):
        if self.player.rect.colliderect(self.rect):
            if self.player.direction == "right" and self.player.rect.right <= self.rect.left + 10 :  
                self.player.rect.right = self.rect.left 
            elif self.player.direction == "left" and self.player.rect.left >= self.rect.right - 10:  
                self.player.rect.left = self.rect.right
            else:
#Checks if the player collides with the the rectangles bottom and if it does it restarts the jump and therefore makes the player fall to the bottom
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
    def draw(self):
        if self.finishline.playerFinish == False:
            self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
    def update(self):
        self.draw()
        self.collosion()



