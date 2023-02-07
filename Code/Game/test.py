from tkinter import *
import tkinter as tk
from game import Game
# from tkinter.font import Font
#import pyglet
# import os

# root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# font_path = os.path.join(root_directory, 'Assets/Fonts/Minecraft.ttf')
# pyglet.font.add_file(font_path)


game = Game()
game.init()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1024")
#print(game.energy)
root.columnconfigure(0, minsize = 1250)
root.rowconfigure([0,1], minsize = 1000)
value = 0

sb = Scrollbar(root)
sb.pack(side = LEFT, fill = Y)
#sb.place(anchor = "w")


timeline = Frame(root, relief = RAISED, bd = 5, bg = "white", height = 110, width = 2000)

era = Frame(root, relief= RAISED, bd = 5, bg = "purple", height = 40, width = 2000)

resources = Frame(root, relief = RAISED, bd = 5, bg = "red", height = 390, width = 325)

visuals = Frame(root, relief = RAISED, bd = 5, bg = "yellow", height = 450, width = 503)

createLabel = Frame(root, bg = "orange", height = 40, width = 100)

production = Frame(root, relief = RAISED, bd = 5, bg = "green", height = 375, width = 325)

upgrades = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = 325, width = 503)


#timeline.grid(row = 0, column = 0, columnspan = 2, sticky = "new")
timeline.place(x = 20, y = 0)

#era.grid(row = 1, column = 0, columnspan = 4, sticky = "ew")
era.place(x = 20, y = 110)

#stats.grid(row = 2, column = 0, sticky= "w")
resources.place(y = 210, x = 20)

#visuals.grid(row = 1, column = 1)
visuals.place(y = 210, x = 350)

#createLabel.grid(row = 3, column = 0)
createLabel.place(y = 155, x = 20)

#production.grid(row = 4, column = 0)
production.place(y = 615, x = 20)

upgrades.place(y = 665, x = 350)

root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

def create_energy():
    game.create_energy()
    #print(game.energy)

energy = Label(resources, text = "Energy: " + str(game.energy), font = ('Terminal', 10))
energy.place(x = 0, y = 25)

tlL = Label(timeline, text = "Timeline:", font = ('Terminal', 10))
tlL.place(x = 0, y = 0)

eraL = Label(era, text = "Era: ", font = ("Terminal", 10))
eraL.place(x = 0, y = 0)

resourcesL = Label(resources, text = "Resources", font = ("Terminal", 10))
resourcesL.place(x = 90, y = 0)

productionL = Label(production, text = "Production", font = ("Terminal", 10))
productionL.place(x = 90, y = 0)

upgradesL = Label(upgrades, text = "Upgrades", font = ("Terminal", 10))
upgradesL.place(x = 200, y = 0)

#img = PhotoImage(file = "D:\VSCode\Python\capstone_project\Assets\Buttons\CasualGameButtonsVol03\PNG\CGB03-yellow_M_btn.png", height = 75, width = 275)

energyB = tk.Button(createLabel, text ="Energy", command = create_energy, font=('Terminal', 10))#, image = img)
energyB.place(in_ = createLabel, y = 10, x = 20)

upgrade1 = tk.Button(upgrades, text = "Energy Production +1 \n Auto-Energy + 0.1/sec", font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)
upgrade1.place(x = 35, y = 20)

#If statement for upgrade button DOES NOT CURRENTLY WORK
if str(game.energy) == 10:
        upgrade1.state = ACTIVE

def update_labels():
    game = Game() # get the instance of the game class
    energy.config(energy, text = "Energy: " + str(game.energy))
    root.after(10, update_labels) # schedule the function to be called again after 1000ms


root.after(1000, update_labels)

root.mainloop()