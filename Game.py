import tkinter as tk
from MasterMind import MasterMind

app = tk.Tk()
app.title("MasterMind")
Board = tk.Canvas(app,bg="beige")
Board.place(height=615, width = 300)

game = MasterMind()
column = 0
rowfilled = 0
Guess = []
circleList = []
responseCircleList = []
for i in range(10):
    circleRow = []
    responseCircleRow = []
    for j in range(4):
        circle = Board.create_oval(10+50*j,10+50*i,50+50*j,50+50*i,outline = "black",fill = "white",width = 2)
        circleRow.append(circle)
        if j < 2:
            circle = Board.create_oval(210+j*20,18+i*(8*5+10),218+j*20,26+i*(8*5+10), outline = "black",fill = "lightgrey",width = 2)
            responseCircleRow.append(circle)
        else:
            circle = Board.create_oval(210+(j-2)*20,34+i*(8*5+10),218+(j-2)*20,42+i*(8*5+10), outline = "black",fill = "lightgrey",width = 2)
            responseCircleRow.append(circle)
        
    responseCircleList.append(responseCircleRow)
    circleList.append(circleRow)

def color_button_click(color):
    global column
    global rowfilled
    global Guess
    global game
    if not rowfilled:
        Guess.append(color)
        Board.itemconfig(circleList[game.TotalAttempts][column], fill=color)
        if column == 3:
            rowfilled = 1
        else:
            column += 1

def check_button_click():
    global rowfilled
    global game
    global Guess
    global column
    if rowfilled:
        blacks,whites = game.checkAttempt(Guess)
        i=0
        while(i<blacks):
            Board.itemconfig(responseCircleList[game.TotalAttempts-1][i], fill="black")
            i += 1
        j = 0
        while(j<whites):
            Board.itemconfig(responseCircleList[game.TotalAttempts-1][j+i], fill="white")
            j += 1
        column = 0
        rowfilled = 0
        Guess = []

def clearGuess():
    global column
    global Guess
    global rowfilled
    global game
    rowfilled = 0
    Guess = []
    if column == 3:
        Board.itemconfig(circleList[game.TotalAttempts][column], fill="white")
    while(column >= 1):
        Board.itemconfig(circleList[game.TotalAttempts][column-1], fill="white")
        column -= 1
    column = 0

def new_game_click():
    global game
    global column
    global Guess
    global rowfilled
    rowfilled = 0
    Guess = []
    for i in range(10):
        for j in range(4):
            Board.itemconfig(circleList[i][j], fill="white")
            Board.itemconfig(responseCircleList[i][j], fill="lightgrey")
    column = 0
    game.restartGame()

   
redButton = tk.Button(Board, background="red", command=lambda: color_button_click("red"))
redButton.place(height=25, width=25, x=10, y= 550)
blueButton = tk.Button(Board, background="blue", command=lambda: color_button_click("blue"))
blueButton.place(height=25, width=25, x=40, y= 550)
greenButton = tk.Button(Board, background="green", command=lambda: color_button_click("green"))
greenButton.place(height=25, width=25, x=70, y= 550)
yellowButton = tk.Button(Board, background="yellow", command=lambda: color_button_click("yellow"))
yellowButton.place(height=25, width=25, x=100, y= 550)
brownButton = tk.Button(Board, background="brown", command=lambda: color_button_click("brown"))
brownButton.place(height=25, width=25, x=130, y= 550)
orangeButton = tk.Button(Board, background="orange", command=lambda: color_button_click("orange"))
orangeButton.place(height=25, width=25, x=160, y= 550)

ColorLabel = tk.Label(Board,text="Choose Colour",bg="White")
ColorLabel.place(x=50,y=525)

CheckButton = tk.Button(Board,text="Check", command=check_button_click)
CheckButton.place(x=75,y=580)

ClearButton = tk.Button(Board, text="Clear", command =clearGuess)
ClearButton.place(x=25,y=580)

newGameButton = tk.Button(Board, text="New Game", command=new_game_click)
newGameButton.place(x=125,y=580)

app.mainloop()
