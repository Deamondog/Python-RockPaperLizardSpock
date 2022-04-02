import tkinter as tk
from tkinter import Toplevel, IntVar
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import random
from pip._internal.utils import filetypes
from cProfile import label

#class for the rules window
class rulesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
          
        rules = 'The rules: "Scissors cuts paper, paper covers rock,\
rock crushes lizard, lizard poisons Spock,\
Spock smashes scissors, scissors decapitates lizard, lizard eats paper,\
paper disproves Spock, Spock vaporizes rock,\
and as it always has, rock crushes scissors."'  
              
        self.title("Rules")
        self.geometry("660x700")
        self.resizable(False, False)
        self.config(background="burlywood2")
        rulesTxt = tk.Text(self, width=75, height=5,wrap='word')
        rulesTxt.grid(row=0,column=0, padx=5)
        rulesTxt.insert('end', rules)
        rulesTxt.config(state='disabled',background="burlywood1")
        closeBut = tk.Button(self,text="Close",command=self.destroy).grid(row=0,column=1)
        createMyCanvas.helpPage(self)

#main window class
class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        #initalize varables
        global wins; global loss; global tie; global hsTexttxt
        wins = IntVar(); loss = IntVar(); tie = IntVar(); hsTexttxt = tk.StringVar()
        
        #set up main window specs
        self.title("Rock Paper Scissors Lizard Spock")
        self.geometry("800x600")
        self.resizable(False, False)

        #set up menu bar
        myMenu = tk.Menu(self)
        self.config(menu=myMenu)
        file_menu = tk.Menu(myMenu)

        myMenu.add_cascade(label="File", menu=file_menu)
        file_menu.add_cascade(label="Rules", command = self.openRulesWin)
        file_menu.add_cascade(label="Exit", command=self.destroy)


        #add game buttons
        self.But = tk.Button(self,text="Spock",command=lambda m="Spock":self.plyrChoice(m)).place(x=5,y=50)
        self.But = tk.Button(self,text="Scissor",command=lambda m="Scissor":self.plyrChoice(m)).place(x=5,y=110)
        self.But = tk.Button(self,text="Paper",command=lambda m="Paper":self.plyrChoice(m)).place(x=5,y=170)
        self.But = tk.Button(self,text="Rock",command=lambda m="Rock":self.plyrChoice(m)).place(x=5,y=230)
        self.But = tk.Button(self,text="Lizard",command=lambda m="Lizard":self.plyrChoice(m)).place(x=5,y=290)

        #labels for wins, loss, ties
        self.wltLabel = tk.Label(self,text="WINS",font="Helvtica 12").place(x=600,y=50,anchor="n")
        self.wltLabel = tk.Label(self,text="LOSS",font="Helvtica 12").place(x=650,y=50,anchor="n")
        self.wltLabel = tk.Label(self,text="TIE",font="Helvtica 12").place(x=700,y=50,anchor="n")

        #results labels shows 
        self.winLabel = tk.Label(self,text="0",font="Helvtica 12")
        self.winLabel.place(x=600,y=75,anchor="n")
        self.lossLabel = tk.Label(self,text="0",font="Helvtica 12")
        self.lossLabel.place(x=650,y=75,anchor="n")
        self.tieLabel = tk.Label(self,text="0",font="Helvtica 12")
        self.tieLabel.place(x=700,y=75,anchor="n")


        #shows who wins
        self.resLabel = tk.Label(self,text="",font = "Helvetica 35")
        self.resLabel.place(x=250,y=375)


        #places the icons
        createMyCanvas.placeIcons(self)

    #opens the rules window
    def openRulesWin(self):
        rulesWin = rulesWindow(self)
        rulesWin.grab_set()

    #gets players choice randomizes pc choice and adds wins/loss/tie and shows calls 
    #the canvas to display choices
    def plyrChoice(self,button_press):

        #choice dictionaries
        winsList = {"Spock":"Scissor""Rock","Scissor":"Paper""Lizard",
                "Paper":"Spock""Rock","Rock":"Scissor""Lizard","Lizard":"Spock""Paper"}
        ties = {"Spock":"Spock", "Scissor":"Scissor",
                "Paper":"Paper", "Rock":"Rock","Lizard":"Lizard"}

        #pc random choice
        pcChoice = random.choice(["Spock","Scissor","Paper","Rock","Lizard"])

        #compares pc to choice dictionary and adds in win/loss/tie labels
        #prints resutls of game
        if pcChoice in winsList[button_press]:
            self.resLabel.config(text="Player Wins")
            wins.set(wins.get()+1)
        elif pcChoice in ties[button_press]:
            self.resLabel.config(text="It's a TIE")
            tie.set(tie.get()+1)
        else:
            self.resLabel.config(text="Computer Wins")
            loss.set(loss.get()+1)

        #calls to place pictures and win/loss/tie numbers
        self.displayResults(button_press,pcChoice)      
        self.winLabel.config(text=wins.get())
        self.lossLabel.config(text=loss.get())
        self.tieLabel.config(text=tie.get())

    def returnWins():
        return wins.get()

    #displays the player and pc choices pictures
    def displayResults(self,chosen,pcChosen):
        size = (181,181)
        plyrPos = (140,35)
        pcPos = (340, 80)
        if chosen == "Spock":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], plyrPos[0], plyrPos[1],275 ,183)
        if chosen == "Scissor":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], plyrPos[0], plyrPos[1],93 ,183)
        if chosen == "Paper":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], plyrPos[0], plyrPos[1],-87 ,183)
        if chosen == "Rock":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], plyrPos[0], plyrPos[1],275 ,3)
        if chosen == "Lizard":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1],plyrPos[0], plyrPos[1],93 ,3)


        if pcChosen == "Spock":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], pcPos[0], pcPos[1],275 ,183)
        if pcChosen == "Scissor":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1],pcPos[0], pcPos[1],93 ,183)
        if pcChosen == "Paper":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], pcPos[0], pcPos[1],-87 ,183)
        if pcChosen == "Rock":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], pcPos[0], pcPos[1],275 ,3)
        if pcChosen == "Lizard":
            createMyCanvas.createCanvas(self,"hand_sheet.png", size[0],size[1], pcPos[0], pcPos[1],93 ,3)


#class to setup the canvases 
class createMyCanvas():
    #puts icons next to buttons
    def placeIcons(self):
        y=35;

        for row1 in range(-87,-237,-50):
            image = Image.open("hand_sheet.png")
            imgCanvas = tk.Canvas(self, width=50,height=50)
            imgCanvas.image = ImageTk.PhotoImage(image)

            imgCanvas.place(x=60,y=y)
            imgCanvas.create_image(row1,3,image=imgCanvas.image)
            y = y + 60

        for row2 in range(-87,-187,-50):
            image = Image.open("hand_sheet.png")
            imgCanvas = tk.Canvas(self, width=50,height=50)
            imgCanvas.image = ImageTk.PhotoImage(image)
            print(row2)
            imgCanvas.place(x=60,y=y)
            imgCanvas.create_image(row2,-47,image=imgCanvas.image)
            y = y + 60

    #displays the help picture
    def helpPage(self):

        image = Image.open("RPSLS2.png")
        imgCanvas = tk.Canvas(self,bg="steel blue", width=600,height=600)
        imgCanvas.image = ImageTk.PhotoImage(image)

        imgCanvas.place(x=5,y=85)
        imgCanvas.create_image(300,300,image=imgCanvas.image)

    #displays the pictures of choices
    def createCanvas(self,img,width,height,x,y,startX,startY):
        imgCanvas = tk.Canvas(self, width=width,height=height)
        imgCanvas.place(x=x,y=y)

        image = Image.open(img)
        imgCanvas.image = ImageTk.PhotoImage(image)
        imgCanvas.create_image(startX,startY,image=imgCanvas.image)


        
#main setup     
if __name__ =="__main__":
    win = mainWindow()
    win.mainloop()