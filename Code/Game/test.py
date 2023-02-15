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
up_SS = upgrades.SubatomicSynthesis()

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
energyLab = None
compLab = None
compDescLab = None
compCostLab = None

# Global Buttons
# Upgrades
upBut_GC = None # Gravitational Compression
upBut_SS = None # Subatomic Synthesis

# Automators
autoBut_Comp = None # Compressor


#CREATING Frames to go on root
timeline = Frame(root, relief = RAISED, bd = 5, bg = "white", height = 90, width = 2000)

lifeForms = Frame(root, relief= RAISED, bd = 5, bg = "purple", height = 40, width = 2000)

visuals = Frame(root, relief = RAISED, bd = 5, bg = "yellow", height = 450, width = 450)

createLabel = Frame(root, bg = "orange", height = 40, width = 100)

time = Frame (root, relief = RAISED, bd = 5, bg = "pink", height = 40, width = 175)

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)

lifeForms.place(x = 20, y = 90)

visuals.place(x = 900, y = resourcePOS)

createLabel.place(x = 20, y = 135)

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
    global upBut_GC
    up_GC.active = 2
    root.after(100)
    upBut_GC.destroy()

def buy_SS():
    game.buy_upgrade(up_SS)
    global upBut_SS
    up_SS.active = 2
    root.after(100)
    upBut_SS.destroy()

def increase_compression():
    auto_Comp.increase(game)
    global compLab
    global compressor_costs
    compLab.config(compLab, text = "Compressors: " + str(auto_Comp.count))
    compCostLab.config(compCostLab, text = auto_Comp.showCost())
    

#CREATION of Labels that go onto Frames/Buttons
tlL = Label(timeline, text = "Timeline:", font = ('Terminal', 10))

lifeL = Label(lifeForms, text = "Lifeforms: ", font = ("Terminal", 10))

eraL = Label(visuals, text = "Era: ", font = ("Terminal", 10))

lifeL.place(x = 0, y = 0)

tlL.place(x = 0, y = 0)

eraL.place(x = 0, y = 0)

#CREATION of Buttons
energyB = tk.Button(createLabel, text ="Energy", command = create_energy, font=('Terminal', 10))#, image = img)

protonB = tk.Button()

neutronB = tk.Button()

timeB = tk.Button(time, text = "Advance Time", font=('Terminal', 10), state = DISABLED)

#PLACEMENT of Buttons in Frames
energyB.place(in_ = createLabel, y = 10, x = 20)

timeB.place(in_ = time, x = 25, y = 5)

# Checks milestone conditions, activating new game mechanics when achieved
def check_milestones():
    game = Game() # get the instance of the game class
    # Any preinitialized tk objects need a global call

    ## Cosmic Era
    # ACTIVATE RESOURCE FRAME after 1 energy is gained
    global resourcesF
    if game.energy >= 1 and resourcesF == None:
        global resourcesL
        global energyLab
        # Creating and placing RESOURCE frame
        resourcesF = Frame(root, relief = RAISED, bd = 5, bg = "red", height = resourceSize, width = 325)
        resourcesF.place(x = 20, y = resourcePOS)
        # Creating and placing frame title
        resourcesL = Label(resourcesF, text = "Resources", font = ("Terminal", 10))
        resourcesL.place(x = 90, y = 0)
        # Initializing ENERGY label
        energyLab = Label(resourcesF, text = "Energy: " + str(game.energy), font = ('Terminal', 10))
        energyLab.place(x = 0, y = 25)
        # Updating 'game' to recognize resource frame is active
        game.resourcesFrame = True

    # ACTIVATE UPGRADES FRAME at 10 energy
    global upgradesF
    if game.energy >= 10 and upgradesF == None:
        global upgradeL
        global upBut_GC
        # Creating and placing UPGRADES frame
        upgradesF = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = upgradeSize, width = 503)
        upgradesF.place(x = 350, y = resourcePOS)
        # Creating and placing frame title
        upgradesL = Label(upgradesF, text = "Upgrades", font = ("Terminal", 10))
        upgradesL.place(x = 200, y = 0)
        # Creating first upgrade button (Gravitational Compression)
        upBut_GC = tk.Button(upgradesF, 
            text = up_GC.name + "\n" + up_GC.description + "\n" + up_GC.showCosts(),
            command = buy_GC, font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)
        upBut_GC.place(in_ = upgradesF, x = 35, y = 20)
        # Setting upgrade instance (not button) to active = 1 (available to buy)
        up_GC.active = 1
        # Updating 'game' to recognize upgrades frame is active
        game.upgradesFrame = True

    # ACTIVATE PRODUCTION FRAME after gravitational compression upgrade
    global productionF
    if game.productionFrame == True and productionF == None:
        global productionL
        global compLab
        global compDescLab
        global compCostLab
        # Creating and placing PRODUCTION frame
        productionF = Frame(root, relief = RAISED, bd = 5, bg = "green", height = productionSize, width = 325)
        productionF.place(x = 20, y = resourcePOS + resourceSize + 5)
        # Creating and placing frame title
        productionL = Label(productionF, text = "Production", font = ("Terminal", 10))
        productionL.place(x = 90, y = 0)
        # Updating 'game' to recognize production frame is active
        game.productionFrame = True
        # Label for Compressors automator
        compLab = Label(productionF, text = "Compressors: " + str(auto_Comp.count), font = ('Terminal', 10))
        compLab.place(x = 0, y = 25)
        # Button for Compressor automator
        autoBut_Comp = tk.Button(productionF, text = "+", font = ("Terminal", 10), command = increase_compression)
        autoBut_Comp.place(x = ((len(compLab.cget("text")) * 10) - 15), y = 24)
        # Cost of Compressor (below)
        compCostLab = Label(productionF, text = auto_Comp.showCost(), font = ('Terminal', 9))
        compCostLab.place(x = 0, y = 50)
        # Description for Compressor (two below)
        compDescLab = Label(productionF, text = auto_Comp.description, font = ('Terminal', 8))
        compDescLab.place(x = 0, y = 65)
        # Adds compressors to the list of active autos
        active_autos.append(auto_Comp)

    #Activate subatomic synthesis upgrade at 100 energy
    global upBut_SS
    if game.energy >= 100 and up_SS.active == 0 and up_GC.active == 2:
        upBut_SS = tk.Button(upgradesF, 
            text = up_SS.name + "\n" + up_SS.description + "\n" + up_SS.showCosts(),
            command = buy_SS, font = ('Terminal', 10), height = 5, width = 50, state = DISABLED)
        upBut_SS.place(in_ = upgradesF, x = 35, y = 20)
        up_SS.active = 1
        
    root.after(100, check_milestones)

# Checks if upgrades are affordable, if not disables them
def afford_upgrades():
    # up_* represents the instance of the upgrade, check this for active call afford(game) function
    # upBut_ * represents the button for the upgrade, enable/disable this
    # Cosmic
    if up_GC.active == 1:
        if up_GC.afford(game):
            upBut_GC.config(upBut_GC, state = ACTIVE)
        else:
            upBut_GC.config(upBut_GC, state = DISABLED)

    if up_SS.active == 1:
        if up_SS.afford(game):
            upBut_SS.config(upBut_SS, state = ACTIVE)
        else:
            upBut_SS.config(upBut_SS, state = DISABLED)

    root.after(100, afford_upgrades)


#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    if game.resourcesFrame == True:
        global energyLab
        energyLab.config(energyLab, text = "Energy: " + str(round(game.energy)))

    root.after(100, update_labels) # schedule the function to be called again after 1000ms

def calculate_revenues():
    # For every active automator, calculate revenue in game
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