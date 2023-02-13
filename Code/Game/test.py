from tkinter import *
import tkinter as tk
from game import Game
import upgrades
import automators


#Getting Instance of Game class & Initializing game
game = Game()
game.init()

# Initializing Upgrades
up_GC = upgrades.GravitationalCompression()

# Initializing Automators
active_autos = []
auto_Comp = automators.Compressor()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1100")

#Values needed
value = 0
resourcePOS = 180
resourceSize = 55
productionSize = 100
upgradeSize = 100

sb = Scrollbar(root)
sb.pack(side = LEFT, fill = Y)

# GLOBAL LISTS
# Global Frames
resourcesF = None
upgradesF = None
productionF = None

# Global Titles
resourcesL = None
upgradeL = None
productionL = None

# Global Labels
energy = None
compressors = None
compressors_desc = None
compressors_cost = None

# Global Buttons
upB_GC = None
inc_Comp = None


#CREATING Frames to go on root
timeline = Frame(root, relief = RAISED, bd = 5, bg = "white", height = 90, width = 2000)

lifeForms = Frame(root, relief= RAISED, bd = 5, bg = "purple", height = 40, width = 2000)

# resourcesF = Frame(root, relief = RAISED, bd = 5, bg = "red", height = resourceSize, width = 325)

visuals = Frame(root, relief = RAISED, bd = 5, bg = "yellow", height = 450, width = 450)

createLabel = Frame(root, bg = "orange", height = 40, width = 100)

# production = Frame(root, relief = RAISED, bd = 5, bg = "green", height = productionSize, width = 325)

# upgrades = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = upgradeSize, width = 503)

time = Frame (root, relief = RAISED, bd = 5, bg = "pink", height = 40, width = 175)

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)

lifeForms.place(x = 20, y = 90)

# resourcesF.place(x = 20, y = resourcePOS)

visuals.place(x = 900, y = resourcePOS)

createLabel.place(x = 20, y = 135)

# production.place(x = 20, y = resourcePOS + resourceSize + 5)

# upgrades.place(x = 350, y = resourcePOS)

time.place(x = 500, y = 135)

#Makes all Frames in GUI weighted the same
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

#FUNCTIONS connected to Game class for in-game Buttons
def create_energy():
    game.create_energy()

def buy_GC():
    game.buy_upgrade(up_GC)
    global upB_GC
    upB_GC.destroy()
    up_GC.active = 2

def increase_compression():
    auto_Comp.increase(game)
    global compressors
    global compressor_costs
    compressors.config(compressors, text = "Compressors: " + str(auto_Comp.count))
    compressors_cost.config(compressors_cost, text = auto_Comp.showCost())
    

#CREATION of Labels that go onto Frames/Buttons
# energy = Label(resources, text = "Energy: " + str(game.energy), font = ('Terminal', 10))

tlL = Label(timeline, text = "Timeline:", font = ('Terminal', 10))

lifeL = Label(lifeForms, text = "Lifeforms: ?", font = ("Terminal", 10))

eraL = Label(visuals, text = "Era: ", font = ("Terminal", 10))

# resourcesL = Label(resources, text = "Resources", font = ("Terminal", 10))

# productionL = Label(production, text = "Production", font = ("Terminal", 10))

# upgradesL = Label(upgrades, text = "Upgrades", font = ("Terminal", 10))

#PLACEMENT of Labels within respected Frame/Button
# energy.place(x = 0, y = 25)

lifeL.place(x = 0, y = 0)

tlL.place(x = 0, y = 0)

eraL.place(x = 0, y = 0)

# resourcesL.place(x = 90, y = 0)

# productionL.place(x = 90, y = 0)

# upgradesL.place(x = 200, y = 0)

#CREATION of Buttons
energyB = tk.Button(createLabel, text ="Energy", command = create_energy, font=('Terminal', 10))#, image = img)

protonB = tk.Button()

neutronB = tk.Button()

timeB = tk.Button(time, text = "Advance Time", font=('Terminal', 10), state = DISABLED)

# upg_SiphonRadition = tk.Button(upgrades, text = GravitationalCompression().name + "\n" + GravitationalCompression().description + "\n" + GravitationalCompression().showCosts(),
#     command = buy_SiphonRadiation, font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)




#PLACEMENT of Buttons in Frames
energyB.place(in_ = createLabel, y = 10, x = 20)

timeB.place(in_ = time, x = 25, y = 5)

# upg_SiphonRadition.place(in_ = upgrades, x = 35, y = 20)

#If statement for upgrade button DOES NOT CURRENTLY WORK

# Checks milestone conditions, activating new game mechanics when achieved
def check_milestones():
    game = Game() # get the instance of the game class
    ## Cosmic Era
    # Activate resources after 1 energy is gained
    global resourcesF
    if game.energy >= 1 and resourcesF == None:
        global resourcesL
        global energy
        resourcesF = Frame(root, relief = RAISED, bd = 5, bg = "red", height = resourceSize, width = 325)
        resourcesF.place(x = 20, y = resourcePOS)
        resourcesL = Label(resourcesF, text = "Resources", font = ("Terminal", 10))
        resourcesL.place(x = 90, y = 0)
        energy = Label(resourcesF, text = "Energy: " + str(game.energy), font = ('Terminal', 10))
        energy.place(x = 0, y = 25)
        game.resources = True
    # Activate upgrades frame at 10 energy
    global upgradesF
    if game.energy >= 10 and upgradesF == None:
        global upgradeL
        global upB_GC
        upgradesF = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = upgradeSize, width = 503)
        upgradesF.place(x = 350, y = resourcePOS)
        upgradesL = Label(upgradesF, text = "Upgrades", font = ("Terminal", 10))
        upgradesL.place(x = 200, y = 0)
        upB_GC = tk.Button(upgradesF, 
            text = up_GC.name + "\n" + up_GC.description + "\n" + up_GC.showCosts(),
            command = buy_GC, font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)
        upB_GC.place(in_ = upgradesF, x = 35, y = 20)
        up_GC.active = 1
        game.upgrades = True
    # Activate production frame after gravitational compression upgrade
    global productionF
    if game.production == True and productionF == None:
        global productionL
        global compressors
        global compressors_desc
        global compressors_cost
        productionF = Frame(root, relief = RAISED, bd = 5, bg = "green", height = productionSize, width = 325)
        productionF.place(x = 20, y = resourcePOS + resourceSize + 5)
        productionL = Label(productionF, text = "Production", font = ("Terminal", 10))
        productionL.place(x = 90, y = 0)
        game.production = True
        compressors = Label(productionF, text = "Compressors: " + str(auto_Comp.count), font = ('Terminal', 10))
        compressors.place(x = 0, y = 25)
        inc_Comp = tk.Button(productionF, text = "+", font = ("Terminal", 10), command = increase_compression)
        inc_Comp.place(x = ((len(compressors.cget("text")) * 10) - 15), y = 24)
        compressors_desc = Label(productionF, text = auto_Comp.description, font = ('Terminal', 8))
        compressors_desc.place(x = 0, y = 65)
        compressors_cost = Label(productionF, text = auto_Comp.showCost(), font = ('Terminal', 9))
        compressors_cost.place(x = 0, y = 50)
        active_autos.append(auto_Comp)
        
    root.after(100, check_milestones)

# Checks if upgrades are affordable, if not disables them
def afford_upgrades():
    # Cosmic
    if up_GC.active == 1:
        if up_GC.afford(game):
            upB_GC.config(upB_GC, state = ACTIVE)
        else:
            upB_GC.config(upB_GC, state = DISABLED)

    root.after(100, afford_upgrades)


#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    if game.resources == True:
        global energy
        energy.config(energy, text = "Energy: " + str(round(game.energy)))
    # if game.production == True:
    #     None

    root.after(100, update_labels) # schedule the function to be called again after 1000ms

def calculate_revenues():
    for a in active_autos:
        game.calculate_revenue(a)
    
    root.after(100, calculate_revenues)

#Call to continously run update_labels function
root.after(100, update_labels)
root.after(100, check_milestones)
root.after(100, afford_upgrades)
root.after(100, calculate_revenues)

#Main call to run game and load in all frames/buttons/labels etc.
root.mainloop()