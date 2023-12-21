import random

class MasterMind:
    
    def __init__(self):
       self.TotalAttempts = 0
       self.Code = self.generateCode()
       self.WinStatus = False
       self.LoseStatus = False

    def generateCode(self):
        ColorsList = ["GREEN", "RED", "BLUE", "YELLOW", "BROWN", "ORANGE"]
        Code = []
        for i in range(4):
            Code.append(random.choice(ColorsList))
        self.Code = Code

    def checkAttempt(self, Guess):
        self.TotalAttempts += 1
        whites,blacks = 0,0
        for index in range(len(self.Code)):
            if self.Code[index] in Guess:
                if Guess[index] == self.Code[index]:
                    blacks += 1
                else:
                    whites += 1
                Guess[index] = "CHECKED"
        
        if blacks == 4:
            self.WinStatus = True
        elif self.TotalAttempts == 10:
            self.LoseStatus = True
        return blacks, whites
    
    def checkWIN(self):
        return self.WinStatus
    
    def checkLOSE(self):
        return self.LoseStatus
    
    def restartGame(self):
        self.TotalAttempts = 0
        self.Code = self.generateCode()
        self.WinStatus = False
        self.LoseStatus = False
    
        
    
    

        
    
    



