import pygame
class Player():
    def __init__(self,game):
        self.game = game
        self.skinNo = "1"
        self.playerImage = ["skin"+self.skinNo+"still.png","skin"+self.skinNo+"left1.png","skin"+self.skinNo+"left2.png","skin"+self.skinNo+"right1.png","skin"+self.skinNo+"right2.png"]
        self.spawnX = 000
        self.spawnY = 800
        self.image = pygame.image.load(self.playerImage[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.spawnX
        self.rect.y = self.spawnY
        self.moveDistance = 2
        self.moveStop = False
        #Keys
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        #ANIMATATION
        self.direction = ""
        self.animeSpeed = 1
        self.AnimeCounter = 0
        #JUMP
        self.jumpIsTrue = False
        self.jumpCount = 15
        self.IsJumping = True
        #COLLOSION
        self.collide = False
        self.gravityOn = True
        #DEATH
        self.IsDead = False
        #FINISH
        self.playerFinished = False
        #cheat
        self.input = False
    def changeSkin(self):
        self.playerImage = ["skin"+self.skinNo+"still.png","skin"+self.skinNo+"left1.png","skin"+self.skinNo+"left2.png","skin"+self.skinNo+"right1.png","skin"+self.skinNo+"right2.png"]
    def draw(self):
        if self.playerFinished == False:
            self.game.screen.blit(self.image,(self.rect.x,self.rect.y))
##    def checkControl(self):
##        self.keyTest = pygame.key.get_pressed()
        
        
        
        


    def move(self,buttonControl):
        self.key = pygame.key.get_pressed()
        #self.keyLeft = (self.key[pygame.K_a])
        moveLeft = buttonControl.userTextL
        moveRight = buttonControl.userTextR
        moveUp = buttonControl.userTextU
        if buttonControl.userTextL == "<":
            moveLeft = "LEFT"
        if buttonControl.userTextL == ">":
            moveLeft = "RIGHT"
        if buttonControl.userTextL == "^":
            moveLeft = "UP"
        if buttonControl.userTextL == "_":
            moveLeft = "SPACE"
            
        if buttonControl.userTextR == "<":
            moveRight = "LEFT"
        if buttonControl.userTextR == ">":
            moveRight = "RIGHT"
        if buttonControl.userTextR == "^":
            moveRight = "UP"
        if buttonControl.userTextR == "_":
            moveRight = "SPACE"
            
        if buttonControl.userTextU == "<":
            moveUp = "LEFT"
        if buttonControl.userTextU == ">":
            moveUp = "RIGHT"
        if buttonControl.userTextU == "^":
            moveUp = "UP"
        if buttonControl.userTextU == "_":
            moveUp = "SPACE"
        exec("self.keyLeft = (self.key[pygame.K_"+moveLeft+"])")
        exec("self.keyRight = (self.key[pygame.K_"+moveRight+"])")
        exec("self.keyUp = (self.key[pygame.K_"+moveUp+"])")
##        if (self.key[pygame.K_a]) or (self.key[pygame.K_d]) or (self.key[pygame.K_w]):
        if (self.keyLeft):
                if self.rect.x >= 0:
                    self.rect.x -= self.moveDistance
                    self.direction = "left"
        if (self.keyRight):
            if self.rect.x <= self.game.screenSize[0] - self.rect.width:
                    self.rect.x += self.moveDistance       
                    self.direction = "right"
        if (self.keyUp) and (self.keyLeft) and self.collide == True:
            self.direction = "left"
            self.jumpIsTrue = True
            self.collide = False
        if (self.keyUp)  and (self.keyRight) and self.collide == True:
            self.direction = "right"
            self.jumpIsTrue = True
            self.collide = False
        if (self.keyUp) and self.collide == True:
            self.jumpIsTrue = True
            self.collide = False
        if (self.keyLeft) == False and (self.keyRight) == False:
            self.direction = "none"      
##        if self.moveStop == False:
##                if self.moveLeft == True:
##                        if self.rect.x >= 0:
##                            self.rect.x -= self.moveDistance
##                            self.direction = "left"
##                if self.moveRight == True:
##                    if self.rect.x <= self.game.screenSize[0] - self.rect.width:
##                            self.rect.x += self.moveDistance       
##                            self.direction = "right"
##                if self.moveUp == True and self.moveLeft == True and self.collide == True:
##                    self.direction = "left"
##                    self.jumpIsTrue = True
##                    self.collide = False
##                if self.moveUp == True  and self.moveRight == True and self.collide == True:
##                    self.direction = "right"
##                    self.jumpIsTrue = True
##                    self.collide = False
##                if self.moveUp == True and self.collide == True:
##                    self.jumpIsTrue = True
##                    self.collide = False
##        else:
##                self.direction = "none"                     
    def animation(self):
        self.AnimeCounter += self.animeSpeed
        if self.direction == "right":
                if self.AnimeCounter <= 100:
                    self.AnimeCounter += self.animeSpeed
                    self.image = pygame.image.load(self.playerImage[3]).convert_alpha()
                elif self.AnimeCounter > 100:
                    self.AnimeCounter += self.animeSpeed
                    self.image = pygame.image.load(self.playerImage[4]).convert_alpha()
                    
                if self.AnimeCounter >= 200:
                    self.AnimeCounter = 0
        if self.direction == "left":
                if self.AnimeCounter <= 100:
                    self.AnimeCounter += self.animeSpeed
                    self.image = pygame.image.load(self.playerImage[1]).convert_alpha()
                elif self.AnimeCounter > 100:
                    self.AnimeCounter += self.animeSpeed
                    self.image = pygame.image.load(self.playerImage[2]).convert_alpha()
                if self.AnimeCounter >= 200:
                    self.AnimeCounter = 0
        if self.direction == "none":
            self.image = pygame.image.load(self.playerImage[0]).convert_alpha()
    def jump(self):
        if self.input == False:
            if self.jumpIsTrue == False:
                      self.IsJumping = False
            else:
                    if self.jumpCount >= -15:
                          self.IsJumping = True
                          self.rect.y -= ((self.jumpCount * abs(self.jumpCount)) * 0.5)/16   #Uses quadratic fomula to create a perfect arc
                          self.jumpCount -= 0.25
                    else:
                          self.jumpCount = 15
                          self.jumpIsTrue = False
    def cheat(self):
        key = pygame.key.get_pressed()  
        if (key[pygame.K_l]) and (key[pygame.K_m]) and (key[pygame.K_o]):
            self.input = True
        if (key[pygame.K_k]):
            self.input = False
            self.IsDead = False
        if self.input == True:
            if (key[pygame.K_w]):
                self.rect.y -= 2
            if (key[pygame.K_s]):
                self.rect.y += 2
    def gravity(self):
        if self.input == False:
            if self.IsJumping == False:
                self.rect.y += 2

                   
    def update(self,buttonControl):
##        self.checkControl()
        self.draw()
        self.move(buttonControl)
        self.animation()
        self.gravity()
        self.jump()
        self.cheat()
        self.changeSkin()
