import random 

class MasterMind:
    
    def __init__(self):
       self.TotalAttempts = 0
       self.Code = []
       self.WinStatus = False
       self.LoseStatus = False
       self.generateCode()

    def generateCode(self):
        ColorsList = ["green", "red", "blue", "yellow", "brown", "orange"]
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
                    Guess[index] = "CHECKED"
                else:
                    for index2 in range(len(self.Code)):
                        if self.Code[index] == Guess[index2]:
                            Guess[index2] = "CHECKED"
                            break
                    whites += 1                
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
        self.generateCode()
        self.WinStatus = False
        self.LoseStatus = False
    
        
    
    

        
    
    



