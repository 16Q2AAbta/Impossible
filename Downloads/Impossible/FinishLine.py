class Finishline():
    def __init__(self,game,player,x,y,length,width):
        self.player = player
        self.game = game
        #Draw
        self.playerFinish = False
        self.x = x
        self.y = y
        self.StartY = y
        self.length = length
        self.width = width
        self.image = pygame.image.load("finishline.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect((self.x,self.y),(self.length, self.width))
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
                        print(line)
                        textFile.write(line[0]+" ")
                        textFile.write(line[1] + '\n')
                        self.inputLeaderboardMethod = False
    def output(self):
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
                        print(self.medalTimer)

                        
                    pygame.draw.line(self.game.screen,self.textColor,lastLineStartH,lastLineEndH,width=10)
                    pygame.draw.line(self.game.screen,self.textColor,line1StartV,line1EndV,width=10)
                    pygame.draw.line(self.game.screen,self.textColor,line2StartV,line2EndV,width=10)
                    pygame.draw.line(self.game.screen,self.textColor,line3StartV,line3EndV,width=10)
                    pygame.draw.line(self.game.screen,self.textColor,line4StartV,line4EndV,width=10)
                    for self.y in range(10):
                        pygame.draw.line(self.game.screen,self.textColor,[coloumn1 - 593,row1 - 80],[coloumn3 - 400,row1 - 80],width=10)
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

