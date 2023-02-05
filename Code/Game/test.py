from tkinter import *
import tkinter as tk
from game import Game


game = Game()
game.init()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1024")
#print(game.pop)
root.columnconfigure(0, minsize = 1250)
root.rowconfigure([0,1], minsize = 1000)
value = 0


#Top label bar for welcome message
#top = Frame(root, bg = "black", relief = RAISED, bd = 5)
#top.pack(fill = tk.BOTH, side = tk.TOP, expand = True)

#Notification bar at top just below welcome
timeline = Frame(root, relief = RAISED, bd = 5, bg = "black", height = 110, width = 1440)

era = Frame(root,  relief= RAISED, bd = 5, bg = "purple", height = 10, width = 1440)

stats = Frame(root, width = 325, height = 525, bg = "red", relief = RAISED, bd = 5)

visuals = Frame(root, width = 503, height = 450, bg = "yellow", relief = RAISED, bd = 5)

createLabel = Frame(root, height = 50, width = 100, bg = "orange")

production = Frame(root, bg = "green", relief = RAISED, bd = 5, height = 75, width = 325)
#notif.place(anchor = "n", height = 178, width = 1167)
#notif.pack(fill = tk.BOTH, side = tk.TOP, expand = True)


#time.place(anchor = "ne", height = 178, width = 250)
#time.pack(expand = True)

timeline.grid(row = 0, column = 0, columnspan = 2, sticky = "new")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
era.grid(row = 1, column = 0, columnspan = 2, sticky = "new")
root.rowconfigure(1, weight = 1)


#Left side panel for upgrades

#upgrades.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
#upgrades.place(height = 25, width = 25, anchor = "e")
stats.grid(row = 2, column = 0, sticky= "w")
stats.place(y = 175, x = 10)

def create_life():
    game.create_life()
    print(game.pop)



b1 = tk.Button(stats, text ="Click me?")
#b1.place(in_ = upgrades, relx = 0, rely = 1)
#b1.grid(row = 1, column = 0, columnspan = 2)

b2 = tk.Button(stats, text ="No, Click me")
#sb2.place(in_ = upgrades, relx = 0, rely = 2)
#b2.grid(row = 2, column = 0, columnspan = 2)


#Right side panel for various in game stats
#stats = Frame(root, width = 225, height = 525, bg = "blue")
#stats.grid(row = 1, column = 2)


#popLife = Label(stats, text = str(game.pop))
#popLife.pack()

pop = Label(stats, text = "Population: 0")
#pop.place(anchor = "w", bordermode = INSIDE, y = 10)

dna = Label(stats, text = "DNA Points: ")
#dna.place(anchor = "w", bordermode = INSIDE, y = 35)


#Middle panel with visuals for game

#visuals.pack(fill = tk.BOTH, expand = True)
visuals.grid(row = 1, column = 1)
visuals.place(y = 175, x = 350)



#bottom.pack(fill = tk.BOTH, side = tk.BOTTOM, expand = True)
createLabel.grid(row = 3, column = 0)
createLabel.place(y = 115, x = 120)

b = tk.Button(createLabel, text ="Energy", command = create_life)
b.place(in_ = createLabel, y = 10, x = 25)



production.grid(row = 4, column = 0)
production.place(y = 710, x = 10)

def update_labels():
    game = Game() # get the instance of the game class
    popLife.config(stats, text = str(game.pop))
    root.after(10, update_labels) # schedule the function to be called again after 1000ms


root.after(1000, update_labels)

root.mainloop()