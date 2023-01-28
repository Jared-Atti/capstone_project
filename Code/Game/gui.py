from tkinter import *
import tkinter as tk

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.columnconfigure(0, minsize= 250)
root.rowconfigure([0,1], minsize= 100)

#Top label bar for welcome message
top = Label(root, text = "Welcome to Eco-Evolution!", bg = "black", fg = "white", relief = RAISED, bd = 5)
top.pack(fill=tk.BOTH, side=tk.TOP, expand = True)

#Notification bar at top just below welcome
notif = Label(root, text = "Notifications", height = 8, width = 10, relief = RAISED, bd = 5)
notif.pack(fill=tk.BOTH, side=tk.TOP, expand = True)

#Left side panel for upgrades
upgrades = Label(root, text = "Upgrades", width = 25, height = 25, bg = "red", relief = RAISED, bd = 5)
upgrades.pack(fill=tk.BOTH, side=tk.LEFT, expand = True)

b = tk.Button(upgrades, text="Click to Split")
b.grid(column=0, row= 0)
b.pack()

#Right side panel for various in game stats
stats = Label(root, text = "Stats", width = 25, height = 25, bg = "blue", relief = RAISED, bd = 5)
stats.pack(fill=tk.BOTH, side=tk.RIGHT, expand = True)


#Middle panel with visuals for game
visuals = Label(root, text = "Visuals", width = 75, height = 25, bg = "yellow", relief = RAISED, bd = 5)
visuals.pack(fill=tk.BOTH, expand = True)

#Bottom bar tbd
bottom = Label(root, text = "bottom Bar", height = 5, relief = RAISED, bd = 5)
bottom.pack(fill=tk.BOTH, side=tk.BOTTOM, expand = True)




root.mainloop()