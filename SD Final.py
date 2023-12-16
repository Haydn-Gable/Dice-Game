import tkinter as tk
from tkinter import PhotoImage
import random

def diceRoll():
    #Generates a random number between one and six to be seen in dice_label
    number = random.randint(1, 6)
    dice_label["text"] = number

def rollEight():
    #Generates a random number between one and eight to be seen in dice_label
    number = random.randint(1, 8)
    dice_label["text"] = number

def rollTwelve():
    #Generates a random number between one and twelve to be seen in dice_label
    number = random.randint(1, 12)
    dice_label["text"] = number
    
def rollTwenty():
    #Generates a random number between one and twenty to be seen in dice_label
    number = random.randint(1, 20)
    dice_label["text"] = number
    
def coin():
    #Shows the coin window and hides the dice window
    top_level.deiconify()
    window.withdraw()

def returnButton():
    #shows the dice window and re-hides the coin window
    top_level.withdraw()
    window.deiconify()
    
def coinFlip():
    #Generates a random number between 1 and 2. If 1, outputs "Heads", if 2, outputs "Tails"
        face = random.randint(1, 2)
        if face == 1:
            coin_label["text"] = "Heads"
        elif face == 2:
            coin_label["text"] = "Tails"
def reset():
    #Resets the dice label text
    dice_label["text"] = 0

def clear():
    #Resets the coin label text
    coin_label["text"] = "______"
    
def exit():
    #Closes the main window
    window.destroy()

#Generates the main dice window and configures it
window = tk.Tk()
window.title("Dice Game")

#Generates the widgets for the dice window
dicePhoto = PhotoImage(file="dice.png")
dice_photo_label = tk.Label(window, image = dicePhoto)
dice_label = tk.Label(window, text=0)
dice_button = tk.Button(window, text = "Roll Six", command = diceRoll)
eight_button = tk.Button(window, text="Roll Eight", command = rollEight)
twelve_button = tk.Button(window, text="Roll Twelve", command = rollTwelve)
twenty_button = tk.Button(window, text="Roll Twenty", command = rollTwenty)
coin_button = tk.Button(window,
                 text = "Coin Game",
                 command = coin)
reset_button = tk.Button(window,
                         text = "Reset",
                         command = reset)
exit_button = tk.Button(window, text="Exit", command= exit)

#Places the widgets on the dice window
dice_button.grid(row=0,column = 0, padx=5)
eight_button.grid(row=0,column=1, padx=5)
twelve_button.grid(row=0,column=2, padx=5)
twenty_button.grid(row=0,column=3, padx=5)
dice_label.grid(row=0, column = 4, padx=5)
coin_button.grid(row=1, column = 0, padx=5)
reset_button.grid(row=0, column=5, padx=5)
dice_photo_label.grid(row=2,column=0, padx=5)
exit_button.grid(row=2,column=2, padx=5)

#Generates and configures the coin window and hides it
#until coin game button is pressed

top_level = tk.Toplevel(window)
top_level.title("Coin Game")
top_level.withdraw()

#Generates widgets for the coin window
coinPhoto = PhotoImage(file="coin.png")
coin_photo_label = tk.Label(top_level, image= coinPhoto)

return_button = tk.Button(top_level,
                          text = "Return",
                          command = returnButton)

coin_flip = tk.Button(top_level, text="Flip", command = coinFlip)

coin_label = tk.Label(top_level, text="______")

clear_button = tk.Button(top_level,
                         text = "Clear",
                         command = clear)

#Places the widgets on the coin window
return_button.grid(row=1, column = 0, padx=5)
coin_label.grid(row=0,column=1, padx=5)
coin_flip.grid(row=0, column=0, padx=5)
clear_button.grid(row=1, column=1, padx=5)
coin_photo_label.grid(row=2,column=0, padx=5)
#Runs the program
window.mainloop()
