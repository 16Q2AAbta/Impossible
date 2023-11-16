import pygame, sys
import time
from Player import *
from Platforms import *
from Walls import *
from Spike import *
from movingWalls import *
from Egg import *
pygame.init()
class Game():
    def __init__(self):
        self.screenSize = [1440,900]
        self.screen = pygame.display.set_mode((self.screenSize[0], self.screenSize[1])
                                              ,pygame.FULLSCREEN)
        self.bg = pygame.image.load("level1 v1.png").convert()
        self.menuConvert = "gameMenu"
        self.rect = self.bg.get_rect()
        self.rect.bottom = self.screenSize[1]
        self.cameraY = 0
        self.startTime = time.time()
        self.endTime = 0
        self.menuBg = pygame.image.load("menuPage.png").convert_alpha()
        self.menuBgrect = self.menuBg.get_rect()
        self.woodenWallBg = pygame.image.load("woodenWall.png").convert()
        self.woodenWallBgrect = self.woodenWallBg.get_rect()
        self.mapBg = pygame.image.load("backgroundP.png").convert()
        self.mapBgrect = self.mapBg.get_rect()
        self.mapBgrect.bottom = self.screenSize[1]
    def draw(self):
        self.screen.fill((0,0,0))
        if self.menuConvert == "gameMenu":
            self.screen.blit(self.bg,self.rect)
        if self.menuConvert == "buttonMenu":
            self.screen.blit(self.menuBg,self.menuBgrect)
        if self.menuConvert == "skinMenu":
            self.screen.blit(self.woodenWallBg,self.woodenWallBgrect)
        if self.menuConvert == "controlMenu":
            self.screen.blit(self.woodenWallBg,self.woodenWallBgrect)
        if self.menuConvert == "backgroundMenu":
            self.screen.blit(self.mapBg,self.mapBgrect)
    def update(self):
        self.draw()
class Finishline():
    def __init__(self,game,player,x,y,length,width):
        self.player = player
        self.game = game
        #Draw
        self.playerFinish = False
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.image = pygame.image.load("finishline.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect((self.x,self.y),(self.length, self.width))
        self.StartY = y
        #Collosion
        self.collide = False
        #Finish
        self.timeMethod = False
        self.printOnce = False
        #Time
        self.totalTime = 0
        self.timeSec = 0
        self.timeTakentext = ""
        #Username
        self.usernameMethod = False
        self.usernameClear = False
        self.userinput = True
        self.userText = ""
        self.usernameX = 400
        self.usernameY = 300
        self.usernameLength = 100
        self.usernameWidth = 340
        #Check Leaderboard
        self.checkLeaderboardMethod = False
        self.leaderboardCompared = False
        self.inputLeaderboardMethod = False
        self.lines = [""] 
        self.n = 0   
        #Input Leaderboard
        self.usernameEntered = False
        self.printOnce2 = False
        #returnArrowAllowed
        self.returnAllowed = False
        #Output
        self.textColor = (0,0,0)
        self.color = (255,255,255)
        self.timer = 0
        self.goldMedal = pygame.image.load(medals[0]).convert_alpha()
        self.silverMedal = pygame.image.load(medals[1]).convert_alpha()
        self.bronzeMedal = pygame.image.load(medals[2]).convert_alpha()
        self.medal = pygame.image.load(medals[0]).convert_alpha()
        self.medalTimer = 0
        self.timeOutput = False
    def draw(self):
        if self.playerFinish == False:
           self.game.screen.blit(self.image,(self.rect.x,self.rect.y))
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
                    if self.playerFinish == False:
                        self.playerFinish = True
                    if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.left - self.player.rect.width:
                                    self.player.x = self.rect.left - self.player.rect.width
                                    self.player.collide = False
                    if self.player.rect.left < self.rect.right and self.player.rect.right > self.rect.right + self.player.rect.width:
                                    self.player.x = self.rect.right
                                    self.player.collide = False

    def finish(self):
        if self.playerFinish == True:
            self.timeMethod = True  
            self.player.playerFinished = True
            self.game.screen.fill(self.color)
            self.checkLeaderboardMethod = True
    def time(self):
        if self.timeMethod == True:
            if self.printOnce == False:
                self.game.endTime = time.time()
                self.printOnce = True
            secs = self.game.endTime - self.game.startTime
            self.timeSec = secs
            mins = secs // 60
            secs = secs % 60
            hours = mins // 60
            mins = mins % 60
            secs = str(int(secs))
            mins = str(int(mins))
            hours = str(int(hours))
            self.totalTime = (hours+":"+mins+":"+secs)
            self.timeTakentext = ("Time Taken:" + (self.totalTime)  )
    def username(self):
         if self.usernameMethod == True:
            if self.usernameClear == False:
                base_font = pygame.font.Font(None, 64)
                input_rect = pygame.Rect(self.usernameX, self.usernameY, self.usernameWidth, self.usernameLength)
                color = pygame.Color('lightskyblue3')
                pygame.draw.rect(game.screen, color, input_rect)  
                text_surface = base_font.render(self.userText, True, self.textColor)
                game.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))      
                input_rect.w = max(100, text_surface.get_width()+10)
                timeTaken = ("Input Username")
                font = pygame.font.Font(None, 100)
                text = font.render(timeTaken, True, self.textColor)
                text_rect = text.get_rect(center = (self.usernameX + 240,self.usernameY - 100))
                clock = pygame.time.Clock()
                game.screen.blit(text, text_rect)
            
    def checkLeaderboard(self):
        if self.checkLeaderboardMethod == True:
            with open("leaderboard.txt", "r") as textFile:
                self.lines = [line.split() for line in textFile]
                for line in self.lines:
                    if self.n  < 10 and self.leaderboardCompared == False:
                            timeSplit = line[1].split(":")
                            hours = int(timeSplit[0])
                            minutes = int(timeSplit[1])
                            seconds = int(timeSplit[2])
                            compareTime = (hours * 3600 + minutes * 60 + seconds) 
                            if self.timeSec < compareTime:
                                self.leaderboardCompared = True
                                self.inputLeaderboardMethod = True
                            else:
                                self.n += 1
                    if self.n > 9:
                        self.timeOutput = True

    def inputLeaderboard(self):
        if self.inputLeaderboardMethod == True:            
            if self.usernameEntered == False:
                    self.usernameMethod = True
            if self.usernameEntered == True:
                    for i in range(9 - self.n):
                        self.lines[9 - i][0] = self.lines[8 - i][0]
                        self.lines[9 - i][1] = self.lines[8 - i][1]
                    if self.printOnce2 == False:
                            self.lines[(self.n)][0] = self.userText
                            self.lines[(self.n)][1] = str(self.totalTime)
                            self.printOnce2 = True
                    textFile = open("leaderboard.txt",'w')
                    for line in self.lines:
                        textFile.write(line[0]+" ")
                        textFile.write(line[1] + '\n')
                        self.inputLeaderboardMethod = False
    def output(self):
        if self.playerFinish == True:
            font = pygame.font.Font(None, 200)
            text = font.render(self.timeTakentext, True, self.textColor)
            text_rect = text.get_rect(center=(self.game.screenSize[0]/2,(self.game.screenSize[1]/2) - 50))
            clock = pygame.time.Clock()
            row1 = 300
            coloumn1 = 910
            coloumn2 = 1000
            coloumn3 = 1300
            self.y = 0
            line1StartV = [312,216]
            line1EndV = [312,725]
            line2StartV = [390,225]
            line2EndV = [390,725]
            line3StartV = [700,225]
            line3EndV = [700,725]
            line4StartV = [900,216]
            line4EndV = [900,725]
            lastLineStartH = [312,720]
            lastLineEndH = [900,720]
            medalCoordinates = [1100,250]
            if self.timeOutput == True:  
        
                if self.timer < 200:
                    self.game.screen.blit(text, text_rect)
                    self.timer += 1
                if self.timer > 199 and self.timer < 800:
                    font1 = pygame.font.Font(None, 50)
                    if self.n == 0:
                        self.medal = self.goldMedal
                    if self.n == 1:
                        self.medal = self.silverMedal
                    if self.n == 2:
                        self.medal = self.bronzeMedal
                    if self.n == 0 or self.n == 1 or self.n == 2:
                        if  self.medalTimer < 5:
                            image = pygame.transform.rotate(self.medal, 20)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 4 and self.medalTimer < 10 or self.medalTimer > 74 and self.medalTimer < 80:
                            image = pygame.transform.rotate(self.medal, 15)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 9 and self.medalTimer < 15 or self.medalTimer > 69 and self.medalTimer < 75:
                            image = pygame.transform.rotate(self.medal, 10)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 14 and self.medalTimer < 20 or self.medalTimer > 64 and self.medalTimer < 70:
                            image = pygame.transform.rotate(self.medal, 5)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 19 and self.medalTimer < 25 or self.medalTimer > 59 and self.medalTimer < 65:
                            image = pygame.transform.rotate(self.medal, 0)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 24 and self.medalTimer < 30 or self.medalTimer > 54 and self.medalTimer < 60:
                            image = pygame.transform.rotate(self.medal, -5)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if self.medalTimer > 29 and self.medalTimer < 35 or self.medalTimer > 49 and self.medalTimer < 55:
                            image = pygame.transform.rotate(self.medal, -10)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 34 and self.medalTimer < 40 or self.medalTimer > 44 and self.medalTimer < 50:
                            image = pygame.transform.rotate(self.medal, -15)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if  self.medalTimer > 39 and self.medalTimer < 45:
                            image = pygame.transform.rotate(self.medal, -20)
                            self.game.screen.blit(image,(medalCoordinates))
                            self.medalTimer +=1
                        if self.medalTimer > 79:
                            self.medalTimer = 0
                        

                        
                    
                    
                    for self.y in range(10):
                        text1 = font1.render(self.lines[self.y][0], True, self.textColor)                   
                        text2 = font1.render(self.lines[self.y][1], True, self.textColor)
                        text3 = font1.render(str(self.y + 1), True, self.textColor)
                        text_rect1 = text.get_rect(center=(coloumn2,row1))        
                        text_rect2 = text.get_rect(center=(coloumn3,row1))
                        text_rect3 = text.get_rect(center=(coloumn1,row1))
                        self.game.screen.blit(text1, text_rect1)
                        self.game.screen.blit(text2, text_rect2)
                        self.game.screen.blit(text3, text_rect3)
                        row1 += 50
                        self.y += 1
                    self.timer += 1
                if self.timer > 799:
                    self.timer = 0

        

    def update(self):
        self.draw()
        self.collosion()
        self.finish()
        self.time()
        self.checkLeaderboard()
        self.inputLeaderboard()
        self.username()
        self.output()        
class fakeFinishline(Finishline):
    def collosion(self):
        x = 1
    def output(self):
        x = 1
    def finish(self):
        x = 1
    def time(self):
        x = 1
    def username(self):
        x = 1
    def checkLeaderboard(self):
        x = 1
    def inputLeaderboard(self):
        x = 1
class Button:
    def __init__(self,game,player,x,y,text):
        self.text = text
        self.game = game
        self.player = player
        self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
        self.rect = self.image2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 1
        self.colorU = pygame.Color('lightskyblue3')
        self.colorR = pygame.Color('lightskyblue3')
        self.colorL = pygame.Color('lightskyblue3')
        self.userTextU = "w"
        self.userTextR = "d"
        self.userTextL = "a"
        self.textColor = (0,0,0)
        self.textAllowed = False
        self.highlight = False
        self.selected = False
    def draw(self):
        self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
        if self.text != "Invisible":
            self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
            if self.text == "Music0" or self.text == "Music1" or self.text == "Music2" or self.text == "Music3":
                self.game.screen.blit(self.image2,(self.rect.x,self.rect.y))
    def drawBorder(self):
        if self.highlight == True:
            self.rect2 = pygame.Rect((self.rect.x,self.rect.y),(110, 210))
            pygame.draw.rect(self.game.screen, (255,255,255), self.rect2,3)
    def drawBorder2(self):
        if self.selected == True:
            self.rect2 = pygame.Rect((self.rect.x,self.rect.y),(110, 210))
            pygame.draw.rect(self.game.screen, (255,255,255), self.rect2,3)
    def displaySkin1(self):
        self.game.screen.blit(pygame.image.load("skin1D.png").convert_alpha(),(89 + 17,100 + 20))
    def displaySkin2(self):
        self.game.screen.blit(pygame.image.load("skin2D.png").convert_alpha(),(89 + 17,400 + 20))
    def displaySkin3(self):
        self.game.screen.blit(pygame.image.load("skin3D.png").convert_alpha(),(377 + 17,100 + 20))
    def displaySkin4(self):
        self.game.screen.blit(pygame.image.load("skin4D.png").convert_alpha(),(377 + 17,400 + 20))
    def displaySkin5(self):
        self.game.screen.blit(pygame.image.load("skin5D.png").convert_alpha(),(665 + 17,100 + 20))
    def displaySkin6(self):
        self.game.screen.blit(pygame.image.load("skin6D.png").convert_alpha(),(665 + 17,400 + 20))
    def displaySkin7(self):
         self.game.screen.blit(pygame.image.load("skin7D.png").convert_alpha(),(953 + 17,100 + 20))
    def displaySkin8(self):
         self.game.screen.blit(pygame.image.load("skin8D.png").convert_alpha(),(953 + 17,400 + 20))
    def displaySkin9(self):
        self.game.screen.blit(pygame.image.load("skin9D.png").convert_alpha(),(1241 + 17,100 + 20))
    def displaySkin10(self):
            self.game.screen.blit(pygame.image.load("skin10D.png").convert_alpha(),(1241 + 17,400 + 20))
    def swap(self):
        if self.text == "Music0":
            self.text = "Music1"
            self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
            pygame.mixer.music.set_volume(0.3)
        elif self.text == "Music1":
            self.text = "Music2"
            self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
            pygame.mixer.music.set_volume(0.6)
        elif self.text == "Music2": 
            self.text = "Music3"
            self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
            pygame.mixer.music.set_volume(1)
        elif self.text == "Music3":
            self.text = "Music0"
            self.image2 = pygame.image.load("button"+self.text+".png").convert_alpha()
            pygame.mixer.music.set_volume(0)
    def pause(self):
        if self.player.moveStop == False:
            self.player.moveStop = True
            self.game.menuConvert = "buttonMenu"
    def unpause(self):
        if self.player.moveStop == True:
            self.player.moveStop = False
            self.game.menuConvert = "gameMenu"        
    def createControl(self):
        self.game.screen.blit(pygame.image.load("controlMenuText.png").convert_alpha(),(463,100))
        self.game.screen.blit(pygame.image.load("arrowControlU.png").convert_alpha(),(500,300))
        self.game.screen.blit(pygame.image.load("arrowControlR.png").convert_alpha(),(500,500))
        self.game.screen.blit(pygame.image.load("arrowControlL.png").convert_alpha(),(500,700))
        base_font = pygame.font.Font(None, 70)
        inputU_rect = pygame.Rect(900, 300, 60,50)
        pygame.draw.rect(game.screen, self.colorU, inputU_rect)  
        text_surface = base_font.render(self.userTextU, True, self.textColor)
        game.screen.blit(text_surface, (inputU_rect.x, inputU_rect.y))      
        inputU_rect.w = max(800, text_surface.get_width()+10)
        
        inputR_rect = pygame.Rect(900, 500, 60,50)
        pygame.draw.rect(game.screen, self.colorR, inputR_rect)  
        text_surface = base_font.render(self.userTextR, True, self.textColor)
        game.screen.blit(text_surface, (inputR_rect.x, inputR_rect.y))      
        inputR_rect.w = max(800, text_surface.get_width()+10)
        
        inputL_rect = pygame.Rect(900, 700, 60,50)
        pygame.draw.rect(game.screen, self.colorL, inputL_rect)  
        text_surface = base_font.render(self.userTextL, True, self.textColor)
        game.screen.blit(text_surface, (inputL_rect.x, inputL_rect.y))      
        inputU_rect.w = max(800, text_surface.get_width()+10)

    def update(self):
        self.draw()
        self.drawBorder()
        self.drawBorder2()



######################################################################
gravityOn = True
active = False
medals = ["gold.png","silver.png","bronze.png"]
pygame.display.set_caption("Torture")
pygame.mixer.music.load('music.wav')# Utopia - Cosmic Trance Mix
pygame.mixer.music.play(-1)

#colours
white = (255,255,255)
black = (0,0,0)



game = Game()
player = Player(game)
finishline = Finishline(game,player,1340,-5800,100,50)
fakeFinishLine = fakeFinishline(game,player,1200,-4000,100,50)
egg1 = Egg(game,player,finishline,970,-745,"EggBlackNWhite.png")
egg2 = Egg(game,player,finishline,560,-1600,"EggRich.png")
egg3 = Egg(game,player,finishline,1400,-2440,"EggCaveman.png")
egg4 = Egg(game,player,finishline,1400,-2800,"EggAverage.png")
egg5 = Egg(game,player,finishline,1300,-4450,"EggBear.png")
egg6 = Egg(game,player,finishline,940,-5370,"EggPirate.png")
eggs = [egg1,egg2,egg3,egg4,egg5,egg6]
button1 = Button(game,player,1390,0,"Settings")
buttonReturn = Button(game,player,570,200,"Return")
buttonMap = Button(game,player,570,650,"Map")
buttonControl = Button(game,player,570,350,"Controls")
buttonExit = Button(game,player,570,800,"Exit")
buttonSkin = Button(game,player,570,500,"Skins")
buttonReturnArrow = Button(game,player,0,863,"Arrow")
buttonReturnArrowFinish = Button(game,player,0,863,"Arrow")
buttonMusic = Button(game,player,5,0,"Music1")
buttonControlU = Button(game,player,900,300,"Invisible")
buttonControlR = Button(game,player,900,500,"Invisible")
buttonControlL = Button(game,player,900,700,"Invisible")
skinMenuButtons = []
buttonFrame1 = Button(game,player,89,100,"Frame")
skinMenuButtons.append(buttonFrame1)
buttonFrame2 = Button(game,player,89,400,"Frame")
skinMenuButtons.append(buttonFrame2)
buttonFrame3 = Button(game,player,377,100,"FrameLock")
skinMenuButtons.append(buttonFrame3)
buttonFrame4 = Button(game,player,377,400,"FrameLock")
skinMenuButtons.append(buttonFrame4)
buttonFrame5 = Button(game,player,665,100,"FrameLock")
skinMenuButtons.append(buttonFrame5)
buttonFrame6 = Button(game,player,665,400,"FrameLock")
skinMenuButtons.append(buttonFrame6)
buttonFrame7 = Button(game,player,953,100,"FrameLock")
skinMenuButtons.append(buttonFrame7)
buttonFrame8 = Button(game,player,953,400,"FrameLock")
skinMenuButtons.append(buttonFrame8)
buttonFrame9 = Button(game,player,1241,100,"FrameLock")
skinMenuButtons.append(buttonFrame9)
buttonFrame10 = Button(game,player,1241,400,"FrameLock")
skinMenuButtons.append(buttonFrame10)


###Level 1
###Platforms
####Normal Platforms
Groundplatform = Platform(game,player,finishline,0,850,"groundPlatform.png")
platform1 = Platform(game,player,finishline,750,550,"W 150 50.png")
platform2 = Platform(game,player,finishline,1100,700,"W 100 50.png")
platform3 = Platform(game,player,finishline,550,400,"W 100 50.png")
platform4 = Platform(game,player,finishline,800,250,"W 300 50.png")
platform5 = Platform(game,player,finishline,500,200,"W 150 50.png")
platform6 = Platform(game,player,finishline,110,370,"W 100 50.png")
platform7 = Platform(game,player,finishline,0,200,"W 75 50.png")
platform8 = Platform(game,player,finishline,100,50,"W 50 50.png")
###Fake Platforms
fakePlatform1 = fakePlatform(game,player,finishline,350,200,"W 150 50.png")
###Walls
####Normal Walls
wall1 = Wall(game,player,finishline,300,200,"W 50 500.png")
wall2 = Wall(game,player,finishline,500,250,"W 50 450.png")
wall3 = Wall(game,player,finishline,400,750,"W 50 100.png")
wall4 = Wall(game,player,finishline,500,800,"W2 50 50.png")
wall5 = Wall(game,player,finishline,750,600,"W 50 150.png")
wall6 = Wall(game,player,finishline,150,00,"W 50 200.png")
###Spike
spike1 = Spike(game,player,finishline,115,150,185,850,850,780,black)
spike2 = Spike(game,player,finishline,300,324.5,349,700,700,750,black)
spike3 = Spike(game,player,finishline,150,174.5,199,200,200,250,black)
##
###Level2
###Platforms
####Normal Platforms
platform9 = Platform(game,player,finishline,150,-100,"C 100 50.png")
platform10 = Platform(game,player,finishline,400,-400,"C 300 50.png")
platform11 = Platform(game,player,finishline,1200,-400,"C 600 50.png")
platform12 = Platform(game,player,finishline,800,-520,"C 200 50.png")
platform13 = Platform(game,player,finishline,800,-720,"C 200 50.png")
####Moving Platforms
movingPlatform1 = movingPlatform(game,player,finishline,200,-200,600,"right","C 200 50.png")
####Moving Walls
movingWall1 = movingWall(game,player,finishline,900,-200,-400,"up","C 50 100.png")
movingWall2 = movingWall(game,player,finishline,0,-350,-600,"up","C 110 50.png") 
movingWall3 = movingWall(game,player,finishline,150,-650,-750,"up","C 50 50.png")
###Fake Platforms
fakePlatform2 = fakePlatform(game,player,finishline,1100,-300,"C 100 50.png")
###Spike
spike4 = Spike(game,player,finishline,700,800,700,-350,-400,-375,black)
spike5 = Spike(game,player,finishline,200,225,250,-450,-450,-500,black)
spike6 = Spike(game,player,finishline,200,225,250,-650,-650,-625,black)
####Normal Walls
wall7 = Wall(game,player,finishline,200,-450,"C 50 200.png")
wall8 = Wall(game,player,finishline,200,-750,"C 50 100.png")
###Level3
###Platforms
####Normal Platforms
platform14 = Platform(game,player,finishline,0,-1550,"S 100 50.png")
platform15 = Platform(game,player,finishline,1200,-1800,"S 100 50.png")
####Moving Platforms
movingPlatform2 = movingPlatform(game,player,finishline,100,-900,1200,"right","S 100 50.png")
movingPlatform3 = movingPlatform(game,player,finishline,0,-1400,1200,"right","S 100 50.png")
movingPlatform4 = movingPlatform(game,player,finishline,800,-1700,1400,"right","S 100 50.png")
####Normal Walls
wall9 = Wall(game,player,finishline,700,-1700,"S 50 100.png")
wall10 = Wall(game,player,finishline,200,-1700,"S 50 100.png")
wall11 = Wall(game,player,finishline,400,-1700,"S 50 100.png")
####Moving Walls
movingWall4 = movingWall(game,player,finishline,900,-1000,-1100,"up","S 25 75.png")
movingWall5 = movingWall(game,player,finishline,1000,-1100,-1300,"up","S 25 75.png")
###Fake Platforms
fakePlatform3 = fakePlatform(game,player,finishline,1100,-1200,"S 100 50.png")
fakePlatform4 = fakePlatform(game,player,finishline,800,-1700,"S 500 50.png")
##
###Spike
spike7 = Spike(game,player,finishline,700,725,750,-1400,-1400,-1470,black)
spike8 = Spike(game,player,finishline,200,225,250,-1400,-1400,-1470,black)
spike9 = Spike(game,player,finishline,400,425,450,-1400,-1400,-1470,black)
###Level4
###Platforms
####Normal Platforms
platform16 = Platform(game,player,finishline,1100,-1950,"Sp 100 50.png")
platform17 = Platform(game,player,finishline,950,-2100,"Sp 50 50.png")
platform18 = Platform(game,player,finishline,750,-2200,"Sp 100 50.png")
platform19 = Platform(game,player,finishline,100,-2200,"Sp 100 50.png")
platform20 = Platform(game,player,finishline,350,-2400,"Sp 30 50.png")
platform21 = Platform(game,player,finishline,650,-2400,"Sp 1000 50.png")
platform22 = Platform(game,player,finishline,950,-2520,"Sp 50 10.png")
platform23 = Platform(game,player,finishline,1080,-2570,"Sp 50 10.png")
platform24 = Platform(game,player,finishline,700,-2550,"Sp 50 10.png")
platform25 = Platform(game,player,finishline,750,-2690,"Sp 50 10.png")
platform26 = Platform(game,player,finishline,1390,-2750,"Sp 50 10.png")
##
###Fake Platforms
fakePlatform5 = fakePlatform(game,player,finishline,900,-2100,"Sp 50 50.png")
fakePlatform6 = fakePlatform(game,player,finishline,350,-2400,"Sp 100 50.png")
###Moving Platforms
movingPlatform5 = movingPlatform(game,player,finishline,300,-2100,600,"right","Sp 100 50.png")
###MOVINGsPIKE
movingSpike1 = movingSpike(game,player,finishline,200,225,200,-2125,-2155,-2140,white,700,"right",1)
movingSpike2 = movingSpike(game,player,finishline,1440,1420,1440,-2425,-2455,-2440,white,700,"left",2)
movingSpike3 = movingSpike(game,player,finishline,1440,1420,1440,-2550,-2580,-2565,white,700,"left",1)
movingSpike4 = movingSpike(game,player,finishline,1440,1420,1440,-2640,-2670,-2655,white,700,"left",2)
movingSpike5 = movingSpike(game,player,finishline,1440,1420,1440,-2725,-2755,-2740,white,700,"left",1)
####Moving Walls
movingWall6 = movingWall(game,player,finishline,000,-2200,-2600,"up","Sp 100 50.png")
###Level5
###Platforms
####Normal Platforms
platform27 = Platform(game,player,finishline,1000,-2800,"J 100 50.png")
platform28 = Platform(game,player,finishline,50,-2800,"J 100 50.png")
####Moving Walls80
movingWall7 = movingWall(game,player,finishline,750,-2800,-3100,"up","J 50 50.png")
movingWall8 = movingWall(game,player,finishline,750,-2940,-3240,"up","J 50 50.png")
movingWall9 = movingWall(game,player,finishline,750,-3080,-3380,"up","J 50 50.png")
movingWall10 = movingWall(game,player,finishline,750,-3220,-3520,"up","J 50 50.png")
movingWall11 = movingWall(game,player,finishline,150,-2800,-3520,"up","J 10 100.png")
###Level6
###platform
platform29 = Platform(game,player,finishline,150,-3600,"D 1440 50.png")
platform30 = Platform(game,player,finishline,700,-3750,"D 200 50.png")
platform31 = Platform(game,player,finishline,600,-4100,"D 350 50.png")
platform32 = Platform(game,player,finishline,350,-3750,"D 250 50.png")
platform33 = Platform(game,player,finishline,1000,-3750,"D 350 50.png")
platform34 = Platform(game,player,finishline,1400,-3750,"D 50 50.png")
platform35 = Platform(game,player,finishline,1000,-3900,"D 300 50.png")
platform36 = Platform(game,player,finishline,200,-3900,"D 350 50.png")
platform37 = Platform(game,player,finishline,0,-4000,"D 50 50.png")
platform38 = Platform(game,player,finishline,50,-4400,"D 850 50.png")
platform39 = Platform(game,player,finishline,1350,-3900,"D 50 50.png")
platform40 = Platform(game,player,finishline,1400,-4050,"D 40 50.png")
platform41 = Platform(game,player,finishline,1000,-4200,"D 200 50.png")
platform42 = Platform(game,player,finishline,1250,-4400,"D 200 50.png")
###wall
wall12 = Wall(game,player,finishline,700,-4100,"D 50 400.png")
wall13 = Wall(game,player,finishline,1300,-4200,"D 50 450.png")
wall14 = Wall(game,player,finishline,500,-4400,"D 50 400.png")
wall15 = Wall(game,player,finishline,1000,-4500,"D 50 300.png")
###Fake Platforms
fakePlatform7 = fakePlatform(game,player,finishline,50,-3750,"D 250 50.png")
fakePlatform8 = fakePlatform(game,player,finishline,1350,-3750,"D 50 50.png")
fakePlatform9 = fakePlatform(game,player,finishline,0,-3900,"D 200 50.png")
fakePlatform10 = fakePlatform(game,player,finishline,0,-4400,"D 50 50.png")
fakePlatform11 = fakePlatform(game,player,finishline,500,-4000,"D 50 100.png") 
fakePlatform12 = fakePlatform(game,player,finishline,1200,-4200,"D 100 50.png")
fakePlatform13 = fakePlatform(game,player,finishline,700,-3700,"D 50 100.png")
###movingWall
movingWall12 = movingWall(game,player,finishline,600,-3800,-4000,"up","D 50 100.png")
movingWall13 = movingWall(game,player,finishline,25,-4100,-4300,"up","D 100 50.png")
###Level7
platform43 = Platform(game,player,finishline,0,-4600,"P 900 50.png")
platform44 = Platform(game,player,finishline,30,-4650,"P 50 10.png")
platform45 = Platform(game,player,finishline,150,-4700,"P 50 10.png")
platform46 = Platform(game,player,finishline,350,-4750,"P 50 10.png")
platform47 = Platform(game,player,finishline,200,-4800,"P 50 10.png")
platform48 = Platform(game,player,finishline,700,-4850,"P 50 10.png")
platform49 = Platform(game,player,finishline,300,-4900,"P 50 10.png")
platform50 = Platform(game,player,finishline,250,-4950,"P 50 10.png")
platform51 = Platform(game,player,finishline,500,-5000,"P 50 10.png")
platform52 = Platform(game,player,finishline,800,-5050,"P 50 10.png")
platform53 = Platform(game,player,finishline,900,-5100,"P 50 10.png")
platform54 = Platform(game,player,finishline,1000,-5200,"P 440 50.png")
platform55 = Platform(game,player,finishline,1000,-5400,"P 100 50.png")
platform56 = Platform(game,player,finishline,1000,-5250,"P 100 50.png")
###movingSpike
movingSpike6 = movingSpike(game,player,finishline,0,25,0,-4625,-4655,-4640,black,900,"right",1)
movingSpike7 = movingSpike(game,player,finishline,-10,15,-10,-4725,-4755,-4740,black,900,"right",2)
movingSpike8 = movingSpike(game,player,finishline,-5,20,-5,-4825,-4855,-4840,black,900,"right",1)
movingSpike9 = movingSpike(game,player,finishline,0,25,0,-4925,-4955,-4940,black,900,"right",1)
movingSpike10 = movingSpike(game,player,finishline,-30,-5,-30,-5025,-5055,-5040,black,900,"right",2)
movingSpike11 = movingSpike(game,player,finishline,-10,15,-10,-5125,-5155,-5140,black,900,"right",1)
movingSpike12 = movingSpike(game,player,finishline,900,880,900,-4675,-4705,-4690,black,0,"left",1)
movingSpike13 = movingSpike(game,player,finishline,910,890,910,-4775,-4805,-4790,black,0,"left",1)
movingSpike14 = movingSpike(game,player,finishline,890,870,890,-4875,-4905,-4890,black,0,"left",1)
movingSpike15 = movingSpike(game,player,finishline,900,880,900,-4975,-5005,-4990,black,0,"left",1)
movingSpike16 = movingSpike(game,player,finishline,890,870,890,-4875,-4905,-4890,black,0,"left",1)
movingSpike17 = movingSpike(game,player,finishline,900,880,900,-4975,-5005,-4990,black,0,"left",1)
###Level8
###platform
platform57 = Platform(game,player,finishline,900,-5500,"F 100 50.png")
platform58 = Platform(game,player,finishline,300,-5700,"F 100 50.png")
platform59 = Platform(game,player,finishline,500,-5700,"F 1000 50.png")
platform60 = Platform(game,player,finishline,500,-6000,"F 1000 50.png")
###movingPlatform
movingPlatform6 = movingPlatform(game,player,finishline,100,-5500,800,"right","F 100 50.png")
###spike
spike10 = Spike(game,player,finishline,500,550,600,-5700,-5700,-5775,white)
spike11 = Spike(game,player,finishline,500,550,600,-5950,-5950,-5875,white)
###movingSpike
movingSpike18 = movingSpike(game,player,finishline,1400,1350,1400,-5500,-5550,-5525,white,0,"left",2)
###wall
movingWall14 = movingWall(game,player,finishline,100,-5500,-5650,"up","F 100 50.png")
###Fake Platforms
fakePlatform14 = fakePlatform(game,player,finishline,200,-5700,"F 100 50.png")


spikes = [spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,movingSpike1,movingSpike2,movingSpike3,movingSpike4,movingSpike5,movingSpike6,
          movingSpike7,movingSpike8,movingSpike9,movingSpike10,movingSpike11,movingSpike12,movingSpike13,movingSpike14,movingSpike15,movingSpike16,movingSpike17,movingSpike18]
platforms = [finishline,fakeFinishLine,Groundplatform,platform1,platform2,platform3,platform4,platform5,platform6,platform7,platform8,platform9,platform10,platform11,platform12,
             platform13,platform14,platform15,platform16,platform17,platform18,platform19,platform20,platform21,platform22,platform23,platform24,platform25,platform26,
             platform27,platform28,platform29,platform30,platform31,platform32,platform33,platform34,platform35,platform36,platform37,platform38,platform39,platform40,
             platform41,platform42,platform43,platform44,platform45,platform46,platform47,platform48,platform49,platform50,platform51,platform52,platform53,platform54,
             platform55,platform56,platform57,platform58,platform59,platform60]
walls = [wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15]
movingWalls = [movingWall1,movingWall2,movingWall3,movingWall4,movingWall5,movingWall6,movingWall7,movingWall8,movingWall9,movingWall10,movingWall11,movingWall12,movingWall13,movingWall14]
movingPlatforms = [movingPlatform1,movingPlatform2,movingPlatform3,movingPlatform4,movingPlatform5,movingPlatform6]
fakePlatforms = [fakePlatform1,fakePlatform2,fakePlatform3,fakePlatform4,fakePlatform5,fakePlatform6,fakePlatform7,fakePlatform8,fakePlatform9,
                 fakePlatform10,fakePlatform11,fakePlatform12,fakePlatform13,fakePlatform14]
entity = []
buttonFrame1.selected = True 
#game loop
for item in eggs:
    entity.append(item)
for item in platforms:
    entity.append(item)
for item in walls:
    entity.append(item)
for item in movingPlatforms:
    entity.append(item)
for item in fakePlatforms:
    entity.append(item)
while True:
    
    for event in pygame.event.get():   #event listener
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game.menuConvert == "backgroundMenu":
                    if game.mapBgrect.y <= 0 and game.mapBgrect.y >= -6300:
                        if event.type == pygame.MOUSEWHEEL:
                            game.mapBgrect.y += (event.y * 100)

                    if game.mapBgrect.y > 0:
                        game.mapBgrect.y = 0

                    if game.mapBgrect.y < -6300:
                        game.mapBgrect.y = -6300
##        keys=pygame.key.get_pressed()
##
##        if keyboard.is_pressed("buttonControl.userTextR"):
##                player.moveRight = True
##        else:
##            player.moveRight = False
##        if keyboard.is_pressed("buttonControl.userTextL"):
##                player.moveLeft = True
##        else:
##            player.moveLeft = False
##        if keyboard.is_pressed("buttonControl.userTextU"):
##                player.moveUp = True
##        else:
##            player.moveUp = False


        #Collosions
        if event.type == pygame.MOUSEBUTTONDOWN:
            if finishline.playerFinish == True:        
                if buttonReturnArrowFinish.rect.collidepoint(pygame.mouse.get_pos()):
                    player.rect.x = 800
                    player.rect.y = 300
                    game.rect.y = 0
                    finishline.playerFinish = False
                    player.playerFinished = False
                    buttonFrame10.text = "Frame"
            if button1.rect.collidepoint(pygame.mouse.get_pos()):
                button1.pause()
            if game.menuConvert == "controlMenu" or game.menuConvert == "skinMenu" or game.menuConvert == "backgroundMenu":
                if buttonReturnArrow.rect.collidepoint(pygame.mouse.get_pos()):
                    game.menuConvert = "buttonMenu"
            if game.menuConvert == "buttonMenu":
                if buttonControl.rect.collidepoint(pygame.mouse.get_pos()):
                    game.menuConvert = "controlMenu"
                if buttonMusic.rect.collidepoint(pygame.mouse.get_pos()):
                    buttonMusic.swap()
                if buttonSkin.rect.collidepoint(pygame.mouse.get_pos()):
                    game.menuConvert = "skinMenu"
                if buttonReturn.rect.collidepoint(pygame.mouse.get_pos()):
                    buttonReturn.unpause()
                if buttonMap.rect.collidepoint(pygame.mouse.get_pos()):
                    game.menuConvert = "backgroundMenu"
                if buttonExit.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()
            if game.menuConvert == "controlMenu":
                if buttonControlU.rect.collidepoint(pygame.mouse.get_pos()):
                        buttonControlU.textAllowed = True
                        buttonControlR.textAllowed = False
                        buttonControlL.textAllowed = False
                        buttonControl.colorU = pygame.Color(57,255,20)
                        buttonControl.colorR = pygame.Color(135,206,235)
                        buttonControl.colorL = pygame.Color(135,206,235)
                        buttonControl.userTextU = buttonControl.userTextU[:-1]
                elif buttonControlR.rect.collidepoint(pygame.mouse.get_pos()):
                        buttonControlU.textAllowed = False
                        buttonControlR.textAllowed = True
                        buttonControlL.textAllowed = False
                        buttonControl.colorU = pygame.Color(135,206,235)
                        buttonControl.colorR = pygame.Color(57,255,20)
                        buttonControl.colorL = pygame.Color(135,206,235)
                        buttonControl.userTextR = buttonControl.userTextR[:-1]
                elif buttonControlL.rect.collidepoint(pygame.mouse.get_pos()):
                        buttonControlU.textAllowed = False
                        buttonControlR.textAllowed = False
                        buttonControlL.textAllowed = True
                        buttonControl.colorU = pygame.Color(135,206,235)
                        buttonControl.colorR = pygame.Color(135,206,235)
                        buttonControl.colorL = pygame.Color(57,255,20)
                        buttonControl.userTextL = buttonControl.userTextL[:-1]
                else:
                        buttonControlU.textAllowed = False
                        buttonControlR.textAllowed = False
                        buttonControlL.textAllowed = False
                        buttonControl.colorU = pygame.Color(135,206,235)
                        buttonControl.colorR = pygame.Color(135,206,235)
                        buttonControl.colorL = pygame.Color(135,206,235)
            if game.menuConvert == "skinMenu":
                for button in skinMenuButtons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()) and button.text == "Frame":
                        for otherButton in skinMenuButtons:
                            otherButton.selected = False
                        button.selected = True                        
                        player.skinNo = str(skinMenuButtons.index(button)+1)
        if buttonControlU.textAllowed == True:
                if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_BACKSPACE:
                                buttonControl.userTextU = buttonControl.userTextU[:-1]
                         elif event.key == pygame.K_UP:
                             if len(buttonControl.userTextU) < 1:
                                buttonControl.userTextU += ("^").lower()
                         elif event.key == pygame.K_SPACE:
                             if len(buttonControl.userTextU) < 1:
                                buttonControl.userTextU += ("_").lower()
                         elif event.key == pygame.K_LEFT:
                             if len(buttonControl.userTextU) < 1:
                                buttonControl.userTextR += ("<").lower()
                         elif event.key == pygame.K_RIGHT:
                             if len(buttonControl.userTextU) < 1:
                                buttonControl.userTextR += (">").lower()
                         else:
                             if len(buttonControl.userTextU) < 1:
                                buttonControl.userTextU += (event.unicode).lower()
        elif len(buttonControl.userTextU) == 0:
                buttonControl.userTextU += "w"
        if buttonControlR.textAllowed == True:
                if event.type == pygame.KEYDOWN:
                         buttonControl.colorR = pygame.Color('white')
                         if event.key == pygame.K_BACKSPACE:
                                buttonControl.userTextR = buttonControl.userTextR[:-1]
                         elif event.key == pygame.K_RIGHT:
                             if len(buttonControl.userTextR) < 1:
                                buttonControl.userTextR += (">").lower()
                         elif event.key == pygame.K_UP:
                             if len(buttonControl.userTextR) < 1:
                                buttonControl.userTextR += ("^").lower()
                         elif event.key == pygame.K_SPACE:
                             if len(buttonControl.userTextR) < 1:
                                buttonControl.userTextR += ("_").lower()
                         elif event.key == pygame.K_LEFT:
                             if len(buttonControl.userTextR) < 1:
                                buttonControl.userTextR += ("<").lower()
                         else:
                            if len(buttonControl.userTextR) < 1:
                                buttonControl.userTextR += (event.unicode).lower()
        elif len(buttonControl.userTextR) == 0:
                buttonControl.userTextR += "d"
        if buttonControlL.textAllowed == True:
                if event.type == pygame.KEYDOWN:
                         buttonControl.colorL = pygame.Color('white')
                         
                         if event.key == pygame.K_BACKSPACE:
                                buttonControl.userTextL = buttonControl.userTextL[:-1]
                         elif event.key == pygame.K_LEFT:
                             if len(buttonControl.userTextL) < 1:
                                buttonControl.userTextL += ("<").lower()
                         elif event.key == pygame.K_RIGHT:
                             if len(buttonControl.userTextL) < 1:
                                buttonControl.userTextL += (">").lower()
                         elif event.key == pygame.K_UP:
                             if len(buttonControl.userTextL) < 1:
                                buttonControl.userTextL += ("^").lower()
                         elif event.key == pygame.K_SPACE:
                             if len(buttonControl.userTextL) < 1:
                                buttonControl.userTextL += ("_").lower()
                         else:
                            if len(buttonControl.userTextL) < 1:
                                buttonControl.userTextL += (event.unicode).lower()
                            if len(buttonControl.userTextL) == 0:
                                buttonControl.userTextL = "a"
        elif len(buttonControl.userTextL) == 0:
                buttonControl.userTextL += "a"
        if buttonControl.userTextU == "l" and buttonControl.userTextR == "o" and buttonControl.userTextL== "l":
            buttonFrame9.text = "Frame"
        if game.menuConvert == "skinMenu":
            for button in skinMenuButtons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.highlight = True
                    else:
                        button.highlight = False
        for egg in eggs:
            if egg.capture:
                    exec("buttonFrame"+str(eggs.index(egg)+3)+ ".text = 'Frame'")
                
                
                


            
        if  finishline.usernameMethod == True:
            if finishline.playerFinish == True:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                                    finishline.userText = finishline.userText[:-1]
                        elif event.key == pygame.K_RETURN:
                                    finishline.usernameClear = True
                                    finishline.usernameEntered = True
                                    finishline.timeMethod = True
                                    finishline.timeOutput = True
                                    finishline.returnAllowed = True
                        else:
                            if len(finishline.userText) < 10:
                                finishline.userText += (event.unicode).upper()
                        
        
    
    if game.menuConvert == "gameMenu":    
        if player.IsJumping == False:
            if player.rect.y < (game.screenSize[1] / 2):
                game.rect.y += 1
            if Groundplatform.rect.y > 850 :
                if player.rect.y > (game.screenSize[1] / 2):
                    game.rect.y -= 1
                        
        for i in range(len(spikes)):
            if player.IsJumping == False:
                if player.rect.y < (game.screenSize[1] / 2):
                    spikes[i].y1 += 1
                    spikes[i].y2 += 1
                    spikes[i].y3 += 1
                if Groundplatform.rect.y > 850 :
                        if player.rect.y > (game.screenSize[1] / 2):
                            spikes[i].y1 -= 1
                            spikes[i].y2 -= 1
                            spikes[i].y3 -= 1
        
        for i in range(len(movingWalls)):
            if player.IsJumping == False:
                if player.rect.y < (game.screenSize[1] / 2):
                    movingWalls[i].startY += 1
                    movingWalls[i].endY += 1
                    movingWalls[i].rect.y += 1
                if Groundplatform.rect.y > 850 :
                    if player.rect.y > (game.screenSize[1] / 2):
                        movingWalls[i].startY -= 1
                        movingWalls[i].endY -= 1
                        movingWalls[i].rect.y -= 1
                
        for i in range(len(entity)):
            if player.IsJumping == False:
                if player.rect.y < (game.screenSize[1] / 2):
                    entity[i].rect.y += 1                
                if Groundplatform.rect.y > 850 :
                    if player.rect.y > (game.screenSize[1] / 2):
                        entity[i].rect.y -= 1
        if Groundplatform.rect.y <= 850 :
            for item in entity:
                item.rect.y = item.StartY
            for spike in spikes:
                spike.y1 = spike.y1Start
                spike.y2 = spike.y2Start
                spike.y3 = spike.y3Start
            for movingWall in movingWalls:
                movingWall.startY = movingWall.defualtstartY
                movingWall.endY = movingWall.defualtendY
        if player.input == False:
            if player.IsDead == True:
                while Groundplatform.rect.y > 850:
                    for i in range(len(entity)):
                                entity[i].rect.y -= 1
                    for i in range(len(spikes)):
                                spikes[i].y1 -= 1
                                spikes[i].y2 -= 1
                                spikes[i].y3 -= 1
                    for i in range(len(movingWalls)):
                                movingWalls[i].startY -= 1
                                movingWalls[i].endY -= 1
                                movingWalls[i].rect.y -= 1
                    game.rect.y -= 1
                player.rect.x = player.spawnX
                player.rect.y = player.spawnY
                player.IsDead = False
                player.jumpCount = False
    game.update()
    if game.menuConvert == "buttonMenu":
        buttonReturn.update()
        buttonControl.update()
        buttonSkin.update()
        buttonExit.update()
        buttonMusic.update()
        buttonMap.update()
    if game.menuConvert == "skinMenu":
        for button in skinMenuButtons:
            button.update()
        buttonReturnArrow.update()
        if buttonFrame1.text == "Frame":
            buttonFrame1.displaySkin1()
        if buttonFrame2.text == "Frame":
            buttonFrame1.displaySkin2()
        if buttonFrame3.text == "Frame":
            buttonFrame1.displaySkin3()
        if buttonFrame4.text == "Frame":
            buttonFrame1.displaySkin4()
        if buttonFrame5.text == "Frame":
            buttonFrame1.displaySkin5()
        if buttonFrame6.text == "Frame":
            buttonFrame1.displaySkin6()
        if buttonFrame7.text == "Frame":
            buttonFrame1.displaySkin7()
        if buttonFrame8.text == "Frame":
            buttonFrame1.displaySkin8()
        if buttonFrame9.text == "Frame":
            buttonFrame1.displaySkin9()
        if buttonFrame10.text == "Frame":
            buttonFrame1.displaySkin10()
    if game.menuConvert == "controlMenu":
        buttonControl.createControl()
        buttonControlU.update()
        buttonControlR.update()
        buttonControlL.update()
        buttonReturnArrow.update()
    if game.menuConvert == "gameMenu":
        button1.update()
        player.update(buttonControl)
        finishline.update()
        for platform in platforms:
            platform.update()
        for spike in spikes:
            spike.update()
        for wall in walls:
            wall.update()
        for movingPlatform in movingPlatforms:
            movingPlatform.update()
        for movingWall in movingWalls:
            movingWall.update()
        for fakePlatform in fakePlatforms:
             fakePlatform.update()
        for egg in eggs:
           egg.update()
        if finishline.playerFinish == False:
            button1.update()
        if finishline.playerFinish == True and finishline.inputLeaderboardMethod == False and player.playerFinished == True:
            buttonReturnArrowFinish.update()
    if game.menuConvert == "backgroundMenu":
        buttonReturnArrow.update()
    pygame.display.flip()
    
