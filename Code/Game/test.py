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
up_TM = upgrades.Temporal()

# Initializing Automators
active_autos = []
auto_Comp = automators.Compressor()
auto_Siph = automators.Siphoner()

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1100")

#Variables for Sizes
SPADDING = 5
PADDING = 10
LPADDING = 15

LEFT_COLUMN_WIDTH = 300
MIDDLE_COLUMN_WIDTH = 350
RIGHT_COLUMN_WIDTH = 500

RESOURCE_FRAME_HEIGHT = 30
RESOURCE_LABEL_NEXTY = 25

UPGRADE_FRAME_HEIGHT = 35
UPGRADE_BUTTON_WIDTH = 300
UPGRADE_BUTTON_HEIGHT = 75
UPGRADE_BUTTON_NEXTY = 50

PRODUCTION_FRAME_HEIGHT = 30
PRODUCTION_LABEL_NEXTY = 25

TEMPORAL_FRAME_HEIGHT = 30

#Variables for Position
TOP_Y = 180
LEFT_COLUMN_X = 20
MIDDLE_COLUMN_X = LEFT_COLUMN_WIDTH + 25
RIGHT_COLUMN_X = 0
PRODUCTION_FRAME_TOP = RESOURCE_FRAME_HEIGHT + TOP_Y + PADDING


sb = Scrollbar(root)
sb.pack(side = LEFT, fill = Y)

# GLOBAL LISTS
# Global Frames
resourcesF = None
upgradesF = None
productionF = None
temporalF = None

# Global Titles
resourcesL = None
upgradeL = None
productionL = None
temporalL = None

# Global Labels
# Resources
energyLab = None
microbeLab = None
# Production
compLab = None
compDescLab = None
compCostLab = None
siphCostLab = None
# Temporal
potentialLab = None
potentailDescLab = None
productivityBut = None
expansionBut = None
timeLab = None
innovationLab = None

# Global Buttons
# Upgrades
upBut_GC = None # Gravitational Compression
upBut_SS = None # Subatomic Synthesis
upBut_TM = None # Temporal Momentum

# Automators
autoBut_Comp = None # Compressor
autoBut_Siph = None # Siphoner


#CREATING Frames to go on root
timeline = Frame(root, relief = RAISED, bd = 5, bg = "white", height = 90, width = 2000)

lifeForms = Frame(root, relief= RAISED, bd = 5, bg = "purple", height = 40, width = 2000)

visuals = Frame(root, relief = RAISED, bd = 5, bg = "yellow", height = 450, width = 450)

createLabel = Frame(root, bg = "orange", height = 40, width = 100)

time = Frame (root, relief = RAISED, bd = 5, bg = "pink", height = 40, width = 175)

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)

lifeForms.place(x = 20, y = 90)

visuals.place(x = 900, y = TOP_Y)

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
    destroyUpgradeButton(upBut_GC, up_GC)

def buy_SS():
    game.buy_upgrade(up_SS)
    global upBut_SS
    up_SS.active = 2
    root.after(100)
    destroyUpgradeButton(upBut_SS, up_SS)

def buy_TM():
    game.buy_upgrade(up_TM)
    global upBut_TM
    up_TM.active = 2
    root.after(100)
    destroyUpgradeButton(upBut_TM, up_TM)

def increase_compression():
    auto_Comp.increase(game)
    global compLab
    global compressor_costs
    compLab.config(compLab, text = "Compressors: " + "{:,.0f}".format(auto_Comp.count))
    compCostLab.config(compCostLab, text = auto_Comp.showCost())
    productionF.update_idletasks()
    autoBut_Comp.place(x = (compLab.winfo_width() + LPADDING))

def increase_siphoner():
    auto_Siph.decrease(game)
    global siphLab
    global siphoner_costs
    siphLab.config(siphLab, text = "Siphoners: " + "{:,.0f}".format(auto_Siph.count))
    siphCostLab.config(siphCostLab, text = auto_Siph.showCost())
    

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
        global microbeLab
        # Creating and placing RESOURCE frame
        resourcesF = Frame(root, relief = RAISED, bd = 5, bg = "red", height = RESOURCE_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        resourcesF.place(x = LEFT_COLUMN_X, y = TOP_Y)
        # Creating and placing frame title
        resourcesL = Label(resourcesF, text = "Resources", font = ("Terminal", 10))
        resourcesL.place(relx = 0.5, y = 10, anchor="center")

        energyLab = createResourceLabel(energyLab, game.energy, "Energy")

        game.resourcesFrame = True

    # ACTIVATE UPGRADES FRAME at 10 energy
    global upgradesF
    if game.energy >= 10 and upgradesF == None:
        global upgradeL
        global upBut_GC
        global UPGRADE_BUTTON_NEXTY
        # Creating and placing UPGRADES frame
        upgradesF = Frame (root, relief = RAISED, bd = 5, bg = "teal", height = UPGRADE_FRAME_HEIGHT, width = MIDDLE_COLUMN_WIDTH)
        upgradesF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)
        # Creating and placing frame title
        upgradesL = Label(upgradesF, text = "Upgrades", font = ("Terminal", 10))
        upgradesL.place(relx = 0.5, y = 10, anchor="center")
        upgradesF.update_idletasks()
        UPGRADE_BUTTON_NEXTY = upgradesL.winfo_height() + upgradesL.winfo_y()
        # Creating first upgrade button (Gravitational Compression)
        upBut_GC = createUpgradeButton(upBut_GC, up_GC, buy_GC)
        game.upgradesFrame = True

    # ACTIVATE PRODUCTION FRAME after gravitational compression upgrade
    global productionF
    if game.productionFrame == False and productionF == None and up_GC.active == 2:
        global productionL
        global compLab
        global compDescLab
        global compCostLab
        global autoBut_Comp
        # Creating and placing PRODUCTION frame
        productionF = Frame(root, relief = RAISED, bd = 5, bg = "green", height = PRODUCTION_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        productionF.place(x = LEFT_COLUMN_X, y = TOP_Y + RESOURCE_FRAME_HEIGHT + 5)
        # Creating and placing frame title
        productionL = Label(productionF, text = "Production", font = ("Terminal", 10))
        productionL.place(relx = 0.5, y = 10, anchor="center")
        # Updating 'game' to recognize production frame is active
        game.productionFrame = True

        # Creating the compressor automator
        results = createProducer(compLab, "Compressors", autoBut_Comp, increase_compression, compCostLab, compDescLab, False, None, auto_Comp)
        compLab = results[0]
        autoBut_Comp = results[1]
        compCostLab = results[2]
        compDescLab = results[3]

        # Adds compressors to the list of active autos
        active_autos.append(auto_Comp)

    #Activate subatomic synthesis upgrade at 100 energy
    global upBut_SS
    global upBut_TM
    if up_GC.active == 2 and up_SS.active == 0 and game.energy >= 100 and up_TM.active == 0:
        upBut_SS = createUpgradeButton(upBut_SS, up_SS, buy_SS)
        upBut_TM = createUpgradeButton(upBut_TM, up_TM, buy_TM)
    
    #Creates Temporal Momentum Frame
    global temporalF
    if temporalF == None and up_TM.active == 2:
        global temporalL
        global potentialLab
        global potentialDescLab
        global productivityBut
        global productivityLab
        global expansionLab
        global expansionBut
        global timeLab
        global innovationLab
        global TEMPORAL_FRAME_HEIGHT
        temporalF = Frame(root, relief = RAISED, bd = 5, bg = "cyan", height = TEMPORAL_FRAME_HEIGHT, width = MIDDLE_COLUMN_WIDTH)
        temporalF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)

        temporalL = Label(temporalF, text = "Temporal Momentum", font = ("Terminal", 10))
        temporalL.place(relx = 0.5, y = 10, anchor="center")
        temporalF.update_idletasks()
        label_height = temporalL.winfo_height()

        potentialLab = Label(temporalF, text = "Potential: " + "{:,.0f}".format(game.maxpotential), font = ("Terminal", 10))
        potentialLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialLab.winfo_height()

        potentialDescLab = Label(temporalF, text = "+1 Potential at " + "{:,.0f}".format(game.potentialincrease) + " lifeforms", font = ("Terminal", 8))
        potentialDescLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialDescLab.winfo_height() + LPADDING

        productivityBut = tk.Button(temporalF, text = "Productivity", font = ("Terminal", 9), width = 13)
        productivityBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        productivityLab = Label(temporalF, text = "{:,.0f}".format(game.productivity), font = ("Terminal", 9))
        productivityLab.place(x = productivityBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + productivityBut.winfo_height() + SPADDING

        temporalF.update_idletasks()
        expansionBut = tk.Button(temporalF, text = "Expansion", font = ("Terminal", 9), width = 13)
        expansionBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        expansionLab = Label(temporalF, text = "{:,.0f}".format(game.expansion), font = ("Terminal", 9))
        expansionLab.place(x = expansionBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + expansionBut.winfo_height() + LPADDING

        timeLab = Label(temporalF, text = "Time: " + "{:,.0f}".format(game.time) + " / " + "{:,.0f}".format(game.expansion * 1000), font = ("Terminal", 10))
        timeLab.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        label_height = label_height + timeLab.winfo_height() + SPADDING

        innovationLab = Label(temporalF, text = "Innovation: " + "{:,.0f}".format(game.innovation), font = ("Terminal", 10))
        innovationLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + innovationLab.winfo_height()

        temporalF.update_idletasks()
        TEMPORAL_FRAME_HEIGHT = TEMPORAL_FRAME_HEIGHT + label_height
        temporalF.config(height=TEMPORAL_FRAME_HEIGHT)
        temporalF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)
        upgradesF.place(x = MIDDLE_COLUMN_X, y = TOP_Y + TEMPORAL_FRAME_HEIGHT + SPADDING)
        game.temporalFrame = True

    root.after(100, check_milestones)


# Function for adding a new resource to resources frame
def createResourceLabel(label, resource, name):
    global RESOURCE_FRAME_HEIGHT
    global RESOURCE_LABEL_NEXTY
    global PRODUCTION_FRAME_TOP
    label = Label(resourcesF, text = name + ": " + "{:,.0f}".format(resource), font = ('Terminal', 10))
    label.place(x = PADDING, y = RESOURCE_LABEL_NEXTY)
    resourcesF.update_idletasks()
    label_height = label.winfo_height()
    RESOURCE_FRAME_HEIGHT = RESOURCE_FRAME_HEIGHT + label_height + PADDING
    RESOURCE_LABEL_NEXTY = RESOURCE_LABEL_NEXTY + label_height + PADDING
    PRODUCTION_FRAME_TOP = PRODUCTION_FRAME_TOP + label_height + PADDING
    resourcesF.config(height=RESOURCE_FRAME_HEIGHT)
    if (productionF != None):
        productionF.place(y = PRODUCTION_FRAME_TOP)
    return label

# Function for destroying a button within upgrades frame
def destroyResourceLabel(label):
    global RESOURCE_FRAME_HEIGHT
    global RESOURCE_LABEL_NEXTY
    global PRODUCTION_FRAME_TOP
    label_height = label.winfo_height()
    label.destroy()
    RESOURCE_FRAME_HEIGHT = RESOURCE_FRAME_HEIGHT - label_height - PADDING
    RESOURCE_LABEL_NEXTY = RESOURCE_LABEL_NEXTY - label_height - PADDING
    PRODUCTION_FRAME_TOP = PRODUCTION_FRAME_TOP - 5 - label_height - PADDING
    resourcesF.config(height=RESOURCE_FRAME_HEIGHT)
    if (productionF != None):
        productionF.place(y = PRODUCTION_FRAME_TOP)


# Function for adding a new button to upgrades frame
def createUpgradeButton(button, upgrade, cmd):
    global UPGRADE_BUTTON_NEXTY
    global UPGRADE_BUTTON_HEIGHT
    global UPGRADE_FRAME_HEIGHT
    global upgradesF
    # Creating the button
    button = tk.Button(upgradesF, 
        text = "\u0332".join(upgrade.name) + "\n" + upgrade.description + "\n" + upgrade.showCosts(),
        command = cmd, font = ('Terminal', 10), state = DISABLED, wraplength=UPGRADE_BUTTON_WIDTH, width=37)
    upgradesF.update_idletasks()
    button_height = button.winfo_height()
    button.place(in_ = upgradesF, relx = 0.5, y = UPGRADE_BUTTON_NEXTY + (button_height // 2), anchor="center")
    upgradesF.update_idletasks()
    button_height = button.winfo_height()
    button.place(in_ = upgradesF, relx = 0.5, y = UPGRADE_BUTTON_NEXTY + (button_height // 2), anchor="center")
    # Updating frame height values
    UPGRADE_BUTTON_NEXTY = UPGRADE_BUTTON_NEXTY + button_height + PADDING
    UPGRADE_FRAME_HEIGHT = UPGRADE_FRAME_HEIGHT + button_height + PADDING
    upgradesF.config(height=UPGRADE_FRAME_HEIGHT)
    # Setting active status of upgrade
    upgrade.active = 1
    return button

# Function for destroying a button within upgrades frame
def destroyUpgradeButton(button, upgrade):
    global UPGRADE_BUTTON_NEXTY
    global UPGRADE_BUTTON_HEIGHT
    global UPGRADE_FRAME_HEIGHT
    global upgradesF

    # Getting info from button being deleted
    button_y = button.winfo_y()
    button_height = button.winfo_height()
    button.destroy()
    
    # Moving any widgets below deleted button up
    for widget in upgradesF.winfo_children():
        current_y = widget.winfo_y()
        if current_y > button_y:
            # Moving up 20 + 5 + button_heigh/2
            # widget.place(y=current_y - PADDING - 5 - button_height / 2)
            widget.place(y=current_y - SPADDING - button_height // 2)

    # Updating variables
    UPGRADE_BUTTON_NEXTY = UPGRADE_BUTTON_NEXTY - button_height - PADDING
    UPGRADE_FRAME_HEIGHT = UPGRADE_FRAME_HEIGHT - button_height - PADDING
    upgradesF.config(height=UPGRADE_FRAME_HEIGHT)
    # Updating upgrade status
    upgrade.active = 2

# Function for adding a new producer to productions
def createProducer(namelabel, name, button, cmd, costlabel, desclabel, toggleflag, togglebut, automator):
    global PRODUCTION_LABEL_NEXTY
    global PRODUCTION_FRAME_HEIGHT
    global productionF

    namelabel = Label(productionF, text = name + ": " + "{:,.0f}".format(automator.count), font = ('Terminal', 10))
    namelabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY)
    productionF.update_idletasks()
    button = tk.Button(productionF, text = "+", font = ("Terminal", 10), command = cmd)
    button.place(x = (namelabel.winfo_width() + LPADDING), y = PRODUCTION_LABEL_NEXTY)

    productionF.update_idletasks()
    costlabel = Label(productionF, text = automator.showCost(), font = ('Terminal', 9))
    costlabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + PADDING / 2 + namelabel.winfo_height())

    productionF.update_idletasks()
    desclabel = Label(productionF, text = automator.desc(), font = ('Terminal', 8), wraplength=LEFT_COLUMN_WIDTH - (PADDING * 2))
    desclabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + 2 * PADDING / 2 + namelabel.winfo_height() + costlabel.winfo_height())
    
    productionF.update_idletasks()
    if (toggleflag):
        desclength = desclabel.winfo_width()
        # Fix cmd later
        togglebut = tk.Button(productionF, text = "OFF", font = ("Terminal", 10), command = cmd)
        togglebut.place(x = desclength + PADDING, y = PRODUCTION_LABEL_NEXTY + 2 * PADDING)
    
        productionF.update_idletasks()
    totalheight = namelabel.winfo_height() + costlabel.winfo_height() + desclabel.winfo_height()

    PRODUCTION_LABEL_NEXTY = PRODUCTION_LABEL_NEXTY + totalheight + PADDING * 2
    PRODUCTION_FRAME_HEIGHT = PRODUCTION_FRAME_HEIGHT + totalheight + PADDING * 2
    productionF.config(height=PRODUCTION_FRAME_HEIGHT)

    # Adds automator to the list of active autos
    active_autos.append(automator)

    return namelabel, button, costlabel, desclabel

# Function for destroying a producer within productions frame
def destroyProducer(namelabel, costlabel, desclabel, button, togglebutton, automator):
    global PRODUCTION_LABEL_NEXTY
    global PRODUCTION_FRAME_HEIGHT
    global productionF

    totalheight = namelabel.winfo_height() + costlabel.winfo_height() + desclabel.winfo_height()

    yposition = namelabel.winfo_y()
    # Moving any widgets below deleted button up
    for widget in upgradesF.winfo_children():
        current_y = widget.winfo_y()
        if current_y > yposition:
            # Moving up 20 + 5 + button_heigh/2
            widget.place(y=current_y - PADDING - 5 - yposition / 2)

    namelabel.destroy()
    costlabel.destroy()
    desclabel.destroy()
    button.destroy()
    if (togglebutton != None):
        togglebutton.destroy()

    PRODUCTION_LABEL_NEXTY = PRODUCTION_LABEL_NEXTY - totalheight - PADDING * 2
    PRODUCTION_FRAME_HEIGHT = PRODUCTION_FRAME_HEIGHT - totalheight - PADDING * 2
    productionF.config(height=PRODUCTION_FRAME_HEIGHT)

    active_autos.remove(automator)


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

    if up_TM.active == 1:
        if up_TM.afford(game):
            upBut_TM.config(upBut_TM, state = ACTIVE)
        else:
            upBut_TM.config(upBut_TM, state = DISABLED)

    root.after(100, afford_upgrades)


#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    if game.resourcesFrame == True:
        global energyLab
        energyLab.config(energyLab, text = "Energy: " + "{:,.0f}".format(game.energy))

    if game.temporalFrame == True:
        global timeLab
        global innovationLab
        potentialLab.config(potentialLab, text = "Potential: " + "{:,.0f}".format(game.maxpotential))
        potentialDescLab.config(potentialDescLab, text = "+1 Potential at " + "{:,.0f}".format(game.potentialincrease) + " lifeforms")
        timeLab.config(timeLab, text = "Time: " + "{:,.0f}".format(game.time) + " / " + "{:,.0f}".format(game.expansion * 1000))
        innovationLab.config(innovationLab, text = "Innovation: " + "{:,.0f}".format(game.innovation))

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