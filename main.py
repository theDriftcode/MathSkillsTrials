##################################################################################################################################
#
#   Welcome to my MathSkillSet Python game, where you can trail yourself to be quicker with math problems at the simplest levels. 
#    
#   @author: Gabriel Garcia (theGcode)
#   @version 1.0
#   @date 2024-12-16
#
#   @Description
#   This is a simple math game uses tkinter to display the problems where the user is presented with a series of math problems.
#   The user is asked to solve the problem and the game keeps track of the user's score
#   The user can choose between different modes:
#   
#   Mode_01(Time_Deathrun):    
#       The User will get prompted with various math questions which they must correctly answer as quickly as possible. 
#       Each correct answer will increase the score by 1 point.
#       The game ends if the user answers 3 problems incorrectly (time ran out or incorrect answer) or reaches the end of the trial.
#
#   Mode_02(SpeedRun):
#       The User will get prompted with various math questions which they must correctly answer as quickly as possible
#       Each correct answer will increase the score by 1 point.
#       The game ends if the user answers 3 problems incorrectly
#       At the end the game will display the users final score
#       The user can skip however if they do, they automatically loose 2 hearts. Only have onw chance to get the rest of the answers correctly. 
#
#   Mode_03(BuildUP):
#       The User will get prompted with various math questions which they must correctly answer as quickly as possible
#       The game increase in difficulty as they progress more and more.
#       Each correct answer will increase the score by 1 point.
#       The game ends if the user answers 3 problems incorrectly
#       The user can skip however if they do, they automatically loose 1 heart
#       After a few questions right the user can regain a heart back. 

#
#
#
#
#
#########################################################################################################################################


#Imports
from random import randint, choice
import time
from ScreenDisplay import *

#Initialized variables
Score = 0
Hearts = 3



#Functions
def timedDeathrun():
    global Mode, Score, Hearts
    df.widgetDestroy()
    df.textDisplay("Mode: Timed Deathrun", "header2", 0,1)
    df.textDisplay("Score: " + str(Score), "header2", 0,20)
    df.buttonMake("Quit",modeSelection, "#f10f0f", "header2", 2, 10, 0, 0)
    
def speedRun():
    global Mode, Score, Hearts
    df.widgetDestroy()
    def hud():
        df.textDisplay("Mode: Speed Run", "header2", 0,0)
        df.textDisplay("Score: " + str(Score), "header2", 0,20)
        df.buttonMake("Quit",modeSelection, "#f10f0f", "header2", 2, 10, 0, 0)
    
        
        
        
        
        
        
    hud()

def infinate():
    global Mode, Score, Hearts
    df.widgetDestroy()
    df.textDisplay("Mode: Infinate", "header2", 0,00)
    df.textDisplay("Score: " + str(Score), "header2", 0,20)
    df.buttonMake("Quit",modeSelection, "#f10f0f", "header2", 2, 10, 0, 0)
    
    
    
df = DisplayFunctions
    
def modeSelection():
    global Mode, Score, Hearts
    # Destroy the start button
    df.widgetDestroy()
    # Create buttons for each game mode
    df.textDisplay("Welcome to the Math Trials!\n Ready to become a Math-ster?", "header1",150, 0)

    df.buttonMake("Speed Run",speedRun, "#ccffcc", "normal", 5, 45, 100, 10)
    df.buttonMake("Infinate",infinate, "#ccccff", "normal", 5, 45, 10, 10)
    df.buttonMake("Timed Deathrun",timedDeathrun, "#ffcccc", "normal", 5, 45, 10, 10)
        
    
    
    
    
    
    #252B2E
    

def startGame():
    global df
    global Mode, Score, Hearts
    df.textDisplay("Welcome to the Math Trials!\n Ready to become a Math-ster?", "header1",150, 0)
    df.buttonMake("Start",modeSelection, "#ffffff","header2",5, 45, 170, 0)
    df.TkRun()
    

#start the game with while main == main
if __name__ == "__main__":
    #Initialize the Screen for tk inter
    df = DisplayFunctions()
    
    startGame()
    
    

# Mode = choice(["timedDeathrun", "speedRun", "infinate"])
