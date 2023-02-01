from tkinter import *
import tkinter as tk
from game import Game


game = Game()
game.init()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1500x1000")
print(game.pop)
root.columnconfigure(0, minsize = 250)
root.rowconfigure([0,1], minsize = 100)
value = 0


#Top label bar for welcome message
top = Frame(root, bg = "black", relief = RAISED, bd = 5)
top.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

#Notification bar at top just below welcome
notif = Frame(root, height = 8, width = 10, relief = RAISED, bd = 5)
notif.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

#Left side panel for upgrades
upgrades = Frame(root, width = 25, height = 25, bg = "red", relief = RAISED, bd = 5)
upgrades.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
#upgrades.place(height = 25, width = 25, anchor = "e")



def create_life():
    game.create_life()
    print(game.pop)
b = tk.Button(upgrades, text ="Create Life", command = create_life)
b.place(in_ = upgrades, relx = 0, rely = 0)


b1 = tk.Button(upgrades, text ="Click me?")
b1.place(in_ = upgrades, relx = 0, rely = 1)
#b1.grid(row = 1, column = 0, columnspan = 2)

b2 = tk.Button(upgrades, text ="No, Click me")
b2.place(in_ = upgrades, relx = 0, rely = 2)
#b2.grid(row = 2, column = 0, columnspan = 2)


#Right side panel for various in game stats
stats = Frame(root, width = 25, height = 25, bg = "blue", relief = RAISED, bd = 5)
stats.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)

popLife = Label(stats, text = str(game.pop))
popLife.pack()

pop = Label(stats, text = "Population: 0")
pop.place(anchor = "w", bordermode = INSIDE, y = 10)

dna = Label(stats, text = "DNA Points: ")
dna.place(anchor = "w", bordermode = INSIDE, y = 35)


#Middle panel with visuals for game
visuals = Frame(root, width = 575, height = 325, bg = "yellow", relief = RAISED, bd = 5)
visuals.pack(fill = tk.BOTH, expand = True)

#Bottom bar Species List
bottom = Frame(root, height = 5, relief = RAISED, bd = 5)
bottom.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)


def update_labels():
    game = Game() # get the instance of the game class
    popLife.config(stats, text = str(game.pop))
    root.after(10, update_labels) # schedule the function to be called again after 1000ms


root.after(1000, update_labels)

root.mainloop()