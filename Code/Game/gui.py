from tkinter import *
import tkinter as tk
from game import Game
from upgrades import *
import upgrades as upg


#Getting Instance of Game class & Initializing game
game = Game()
game.init()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1100")

#Values needed
value = 0
resourcePOS = 180
resourceSize = 55
productionSize = 55
upgradeSize = 100

sb = Scrollbar(root)
sb.pack(side = LEFT, fill = Y)

#CREATING Frames to go on root
timeline = Frame(root, relief = RAISED, bd = 5, bg = "white", height = 90, width = 2000)

lifeForms = Frame(root, relief= RAISED, bd = 5, bg = "purple", height = 40, width = 2000)

resources = Frame(root, relief = RAISED, bd = 5, bg = "red", height = resourceSize, width = 325)

visuals = Frame(root, relief = RAISED, bd = 5, bg = "yellow", height = 450, width = 450)

createLabel = Frame(root, bg = "orange", height = 40, width = 100)

production = Frame(root, relief = RAISED, bd = 5, bg = "green", height = productionSize, width = 325)

upgrades = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = upgradeSize, width = 503)

time = Frame (root, relief = RAISED, bd = 5, bg = "pink", height = 40, width = 175)

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)

lifeForms.place(x = 20, y = 90)

resources.place(x = 20, y = resourcePOS)

visuals.place(x = 900, y = resourcePOS)

createLabel.place(x = 20, y = 135)

production.place(x = 20, y = resourcePOS + resourceSize + 5)

upgrades.place(x = 350, y = resourcePOS)

time.place(x = 500, y = 135)

#Makes all Frames in GUI weighted the same
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

#FUNCTIONS connected to Game class for in-game Buttons
def create_energy():
    game.create_energy()

def buy_SiphonRadiation():
    game.buy_upgrade(upg.GravitationalCompression)
    
    

#CREATION of Labels that go onto Frames/Buttons
energy = Label(resources, text = "Energy: " + str(game.energy), font = ('Terminal', 10))

tlL = Label(timeline, text = "Timeline:", font = ('Terminal', 10))

lifeL = Label(lifeForms, text = "Lifeforms: ", font = ("Terminal", 10))

eraL = Label(visuals, text = "Era: ", font = ("Terminal", 10))

resourcesL = Label(resources, text = "Resources", font = ("Terminal", 10))

productionL = Label(production, text = "Production", font = ("Terminal", 10))

upgradesL = Label(upgrades, text = "Upgrades", font = ("Terminal", 10))

#PLACEMENT of Labels within respected Frame/Button
energy.place(x = 0, y = 25)

lifeL.place(x = 0, y = 0)

tlL.place(x = 0, y = 0)

eraL.place(x = 0, y = 0)

resourcesL.place(x = 90, y = 0)

productionL.place(x = 90, y = 0)

upgradesL.place(x = 200, y = 0)

#CREATION of Buttons
energyB = tk.Button(createLabel, text ="Energy", command = create_energy, font=('Terminal', 10))#, image = img)

protonB = tk.Button()

neutronB = tk.Button()

timeB = tk.Button(time, text = "Advance Time", font=('Terminal', 10), state = DISABLED)

upg_SiphonRadition = tk.Button(upgrades, text = GravitationalCompression().name + "\n" + GravitationalCompression().description + "\n" + GravitationalCompression().showCosts(),
    command = buy_SiphonRadiation, font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)



#PLACEMENT of Buttons in Frames
energyB.place(in_ = createLabel, y = 10, x = 20)

timeB.place(in_ = time, x = 25, y = 5)

upg_SiphonRadition.place(in_ = upgrades, x = 35, y = 20)

#If statement for upgrade button DOES NOT CURRENTLY WORK


#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    energy.config(energy, text = "Energy: " + str(round(game.energy)))
    if game.energy >= 10:
        upg_SiphonRadition.config(upg_SiphonRadition, state = ACTIVE)
    elif game.energy < 10:
        upg_SiphonRadition.config(upg_SiphonRadition, state = DISABLED)

    game.energy += game.energyRev
    # print(str(game.energy) + " " + str(game.energyRev))

    # Revenue Calculation
    game.energy += game.energyRev

    root.after(100, update_labels) # schedule the function to be called again after 1000ms

#Call to continously run update_labels function
root.after(1000, update_labels)

#Main call to run game and load in all frames/buttons/labels etc.
root.mainloop()