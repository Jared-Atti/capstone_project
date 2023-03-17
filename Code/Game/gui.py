from tkinter import *
import tkinter as tk
from game import Game
import upgrades
import automators


#Getting Instance of Game class & Initializing game
game = Game()
game.init()

# Initializing Upgrades
u1_GC = upgrades.GravitationalCompression()
u2_SS = upgrades.SubatomicSynthesis()
u3_TM = upgrades.Temporal()
u4_IN = upgrades.Innovation()
u5_NS = upgrades.Nucleosynthesis()
u6_GA = upgrades.Gravitational_Amplification()
u7_QF = upgrades.Quark_Fusion()
u8_AF = upgrades.Atomic_Fabrication()
u9_DH = upgrades.Discover_Helium()
u10_P1 = upgrades.Cosmic_Burst()
u11_P2 = upgrades.Starlight_Path()
u12_P3 = upgrades.Quantum_Leap()
u13_P4 = upgrades.Galatic_Investment()
u14_P5 = upgrades.Nova_Catalyst()
u15_GF = upgrades.Gravitational_Flucuations
u16_QA = upgrades.Quark_Acceleration()
u17_PS = upgrades.Proton_Synthesizer()
u18_NP = upgrades.Neutron_Processor()
u19_HC = upgrades.Hydrogenic_Catalyst()
u20_HE = upgrades.Helium_Extractor()
u21_CS = upgrades.Create_Sun()
u22_NF = upgrades.Nuclear_Fusion()
u23_CE = upgrades.Create_Earth()
u24_TE = upgrades.Travel_Earth()


# Initializing Automators
active_autos = []
a1_GC = automators.Compressor()
a2_QS = automators.Quark_Synthesizer()
a3_PS = automators.Proton_Synthesizer()
a4_NS = automators.Neutron_Synthesizer()

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
# root.configure(yscrollcommand=sb.set)

# GLOBAL LISTS
# Global Frames
resourcesF = None
upgradesF = None
productionF = None
temporalF = None

# Global Titles
resourcesTitleLabel = None
upgradeTitleLabel = None
productionTitleLabel = None
temporalTitleLabel = None

# Global Labels
# Resources
energyLab = None
microbeLab = None
quarkLab = None
protonLab = None
neutronLab = None
# Production
a1_GC_Name = None
a1_GC_Desc = None
a1_GC_Cost = None
a2_QS_Name = None
a2_QS_Desc = None
a2_QS_Cost = None
a2_QS_Toggle = None
a3_PS_Name = None
a3_PS_Desc = None
a3_PS_Cost = None
a3_PS_Toggle = None
a4_NS_Name = None
a4_NS_Desc = None
a4_NS_Cost = None
a4_NS_Toggle = None
# Temporal
potentialLab = None
potentailDescLab = None
productivityLab = None
expansionLab = None
productivityBut = None
expansionBut = None
timeLab = None
innovationLab = None
respecBut = None

# Global Buttons
# Upgrades
u1_GC_Button = None # Gravitational Compression
u2_SS_Button = None # Subatomic Synthesis
u3_TM_Button = None # Temporal Momentum
u4_IN_Button = None # Innovation
u5_NS_Button = None # Nucleosynthesis
u6_GA_Button = None
u7_QF_Button = None
u8_AF_Button = None
u9_DH_Button = None
u10_P1_Button = None
u11_P2_Button = None
u12_P3_Button = None
u13_P4_Button = None
u14_P5_Button = None
u15_GF_Button = None
u16_QA_Button = None
u17_PS_Button = None
u18_NP_Button = None
u19_HC_Button = None
u20_HE_Button = None
u21_CS_Button = None
u22_NF_Button = None
u23_CE_Button = None
u24_TE_Button = None

# Automators
a1_GC_Button = None # Compressor
a2_QS_Button = None # Quark Synthesizer
a3_PS_Button = None # Proton Synthesizer
a4_NS_Button = None # Neutron Synthesizer


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

def buy_Productivity():
    global productivityBut
    global expansionBut
    global productivityLab
    if (productivityLab):
        if game.potential > 0:
            game.productivity += 1
            productivityLab.config(productivityLab, text = game.productivity)
            game.potential -= 1
        if game.potential == 0:
            productivityBut.config(productivityBut, state = DISABLED)
            expansionBut.config(expansionBut, state = DISABLED)
        respecBut.config(respecBut, state = ACTIVE)

def buy_Expansion():
    global productivityBut
    global expansionBut
    global expansionLab
    if (expansionLab):
        if game.potential > 0:
            game.expansion += 1
            expansionLab.config(expansionLab, text = game.expansion)
            game.potential -= 1
        if game.potential == 0:
            productivityBut.config(productivityBut, state = DISABLED)
            expansionBut.config(expansionBut, state = DISABLED)
        respecBut.config(respecBut, state = ACTIVE)

def respec_temporal():
    global productivityBut
    global expansionBut
    global productivityLab
    global productivityBut
    global expansionBut
    global expansionLab
    if (game.productivity + game.expansion > 2):
        game.potential = game.potential + game.productivity + game.expansion - 2
        game.productivity = 1
        game.expansion = 1
        expansionLab.config(expansionLab, text = game.expansion)
        productivityLab.config(productivityLab, text = game.productivity)
        if (game.potential > 0):
            productivityBut.config(productivityBut, state = ACTIVE)
            expansionBut.config(expansionBut, state = ACTIVE)
        else:
            productivityBut.config(productivityBut, state = DISABLED)
            expansionBut.config(expansionBut, state = DISABLED)
        respecBut.config(respecBut, state = DISABLED)

def buy_GC():
    game.buy_upgrade(u1_GC)
    global u1_GC_Button
    u1_GC.active = 2
    root.after(100)
    destroyUpgradeButton(u1_GC_Button, u1_GC)

    global u15_GF_Button
    u15_GF_Button = createUpgradeButton(u15_GF_Button, u15_GF, buy_GF)

def buy_SS():
    global u2_SS
    global u2_SS_Button
    global a2_QS_Button
    global a2_QS_Name
    global a2_QS_Cost
    global a2_QS_Desc
    global a2_QS_Toggle
    global quarkLab
    game.buy_upgrade(u2_SS)
    u2_SS.active = 2
    root.after(100)
    destroyUpgradeButton(u2_SS_Button, u2_SS)
    results = createProducer(a2_QS_Name, "Quark Synthesizers", a2_QS_Button, increase_a2_QS, a2_QS_Cost, a2_QS_Desc, True, a2_QS_Toggle, toggle_a2_QS, a2_QS)
    a2_QS_Name = results[0]
    a2_QS_Button = results[1]
    a2_QS_Cost = results[2]
    a2_QS_Desc = results[3]
    a2_QS_Toggle = results[4]
    active_autos.append(a2_QS)
    quarkLab = createResourceLabel(quarkLab, game.quarks, "Quarks")
    global u5_NS_Button
    global u7_QF_Button
    u5_NS_Button = createUpgradeButton(u5_NS_Button, u5_NS, buy_NS)
    u7_QF_Button = createUpgradeButton(u7_QF_Button, u7_QF, buy_QF)

def buy_TM():
    game.buy_upgrade(u3_TM)
    global u3_TM_Button
    u3_TM.active = 2
    root.after(100)
    destroyUpgradeButton(u3_TM_Button, u3_TM)

def buy_IN():
    game.buy_upgrade(u4_IN)
    global u4_IN_Button
    u4_IN.active = 2
    root.after(100)
    destroyUpgradeButton(u4_IN_Button, u4_IN)

    global u10_P1_Button
    u10_P1_Button = createUpgradeButton(u10_P1_Button, u10_P1, buy_P1)

    # Testing, remove later
    # game.potential += 10
    # game.set_max_potential()
    # productivityBut.config(productivityBut, state = ACTIVE)
    # expansionBut.config(expansionBut, state = ACTIVE)


def buy_NS():
    game.buy_upgrade(u5_NS)
    global u5_NS_Button
    global a3_PS_Button
    global a3_PS_Name
    global a3_PS_Cost
    global a3_PS_Desc
    global a3_PS_Toggle
    global a4_NS_Button
    global a4_NS_Name
    global a4_NS_Cost
    global a4_NS_Desc
    global a4_NS_Toggle
    global protonLab
    global neutronLab
    u5_NS.active = 2
    root.after(100)
    destroyUpgradeButton(u5_NS_Button, u5_NS)
    results = createProducer(a3_PS_Name, "Proton Synthesizers", a3_PS_Button, increase_a3_PS, a3_PS_Cost, a3_PS_Desc, True, a3_PS_Toggle, toggle_a3_PS, a3_PS)
    a3_PS_Name = results[0]
    a3_PS_Button = results[1]
    a3_PS_Cost = results[2]
    a3_PS_Desc = results[3]
    a3_PS_Toggle = results[4]
    active_autos.append(a3_PS)
    results = createProducer(a4_NS_Name, "Neutron Synthesizers", a4_NS_Button, increase_a4_NS, a4_NS_Cost, a4_NS_Desc, True, a4_NS_Toggle, toggle_a4_NS, a4_NS)
    a4_NS_Name = results[0]
    a4_NS_Button = results[1]
    a4_NS_Cost = results[2]
    a4_NS_Desc = results[3]
    a4_NS_Toggle = results[4]
    active_autos.append(a4_NS)
    protonLab = createResourceLabel(protonLab, game.protons, "Protons")
    neutronLab = createResourceLabel(neutronLab, game.neutrons, "Neutron")

def buy_GA():
    global a1_GC
    a1_GC = game.buy_autoupgrade(u6_GA, a1_GC)
    global u6_GA_Button
    u6_GA.active = 2
    root.after(100)
    destroyUpgradeButton(u6_GA_Button, u6_GA)
    global a1_GC_Desc
    a1_GC_Desc.config(a1_GC_Desc, text = a1_GC.desc())

def buy_QF():
    global a2_QS
    a2_QS = game.buy_autoupgrade(u7_QF, a2_QS)
    global u7_QF_Button
    u7_QF.active = 2
    root.after(100)
    destroyUpgradeButton(u7_QF_Button, u7_QF)
    global a2_QS_Desc
    a2_QS_Desc.config(a2_QS_Desc, text = a2_QS.desc())

    global u16_QA_Button
    u16_QA_Button = createUpgradeButton(u16_QA_Button, u16_QA, buy_QA)

def buy_AF():
    game.buy_upgrade(u8_AF)
    global u8_AF_Button
    u8_AF.active = 2
    root.after(100)
    destroyUpgradeButton(u8_AF_Button, u8_AF)

def buy_DH():
    game.buy_upgrade(u9_DH)
    global u9_DH_Button
    u9_DH.active = 2
    root.after(100)
    destroyUpgradeButton(u9_DH_Button, u9_DH)

    global u21_CS_Button
    u21_CS_Button = createUpgradeButton(u21_CS_Button, u21_CS, buy_CS)

def buy_P1():
    game.buy_upgrade(u10_P1)
    global u10_P1_Button
    u10_P1.active = 2
    root.after(100)
    destroyUpgradeButton(u10_P1_Button, u10_P1)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

    global u11_P2_Button
    u11_P2_Button = createUpgradeButton(u11_P2_Button, u11_P2, buy_P2)

def buy_P2():
    game.buy_upgrade(u11_P2)
    global u11_P2_Button
    u11_P2.active = 2
    root.after(100)
    destroyUpgradeButton(u11_P2_Button, u11_P2)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

    global u12_P3_Button
    u12_P3_Button = createUpgradeButton(u12_P3_Button, u12_P3, buy_P3)

def buy_P3():
    game.buy_upgrade(u12_P3)
    global u12_P3_Button
    u12_P3.active = 2
    root.after(100)
    destroyUpgradeButton(u12_P3_Button, u12_P3)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

    global u13_P4_Button
    u13_P4_Button = createUpgradeButton(u13_P4_Button, u13_P4, buy_P4)

def buy_P4():
    game.buy_upgrade(u13_P4)
    global u13_P4_Button
    u13_P4.active = 2
    root.after(100)
    destroyUpgradeButton(u13_P4_Button, u13_P4)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

    # global u14_P5_Button
    # u14_P5_Button = createUpgradeButton(u14_P5_Button, u13_P5, buy_P5)

def buy_P5():
    game.buy_upgrade(u14_P5)
    global u14_P5_Button
    u14_P5.active = 2
    root.after(100)
    destroyUpgradeButton(u14_P5_Button, u14_P5)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

def buy_GF():
    game.buy_upgrade(u15_GF)
    global u15_GF_Button
    u15_GF.active = 2
    root.after(100)
    destroyUpgradeButton(u15_GF_Button, u15_GF)

def buy_QA():
    game.buy_autoupgrade(u16_QA)
    global u16_QA_Button
    u16_QA.activve = 2
    root.after(100)
    destroyUpgradeButton(u16_QA_Button, u16_QA)

def buy_PS():
    game.buy_upgrade(u17_PS)
    global u17_PS_Button
    u17_PS.active = 2
    root.after(100)
    destroyUpgradeButton(u17_PS_Button, u17_PS)

    global u18_NP_Button
    u18_NP_Button = createUpgradeButton(u18_NP_Button, u18_NP, buy_NP)

def buy_NP():
    game.buy_upgrade(u18_NP)
    global u18_NP_Button
    u18_NP.active = 2
    root.after(100)
    destroyUpgradeButton(u18_NP_Button, u18_NP)

    global u19_HC_Button
    u19_HC_Button = createUpgradeButton(u19_HC_Button, u19_HC, buy_HC)

def buy_HC():
    game.buy_upgrade(u19_HC)
    global u19_HC_Button
    u19_HC.active = 2
    root.after(100)
    destroyUpgradeButton(u19_HC_Button, u19_HC)

    global u20_HE_Button
    u20_HE_Button = createUpgradeButton(u20_HE_Button, u20_HE, buy_HE)

def buy_HE():
    game.buy_upgrade(u20_HE)
    global u20_HE_Button
    u20_HE.active = 2
    root.after(100)
    destroyUpgradeButton(u20_HE_Button, u20_HE)

def buy_CS():
    game.buy_upgrade(u21_CS)
    global u21_CS_Button
    u21_CS.active = 2
    root.after(100)
    destroyUpgradeButton(u21_CS_Button, u21_CS)

    global u22_NF_Button
    global u23_CE_Button
    u22_NF_Button = createUpgradeButton(u22_NF_Button, u22_NF, buy_NF)
    u23_CE_Button = createUpgradeButton(u23_CE_Button, u23_CE, buy_CE)

def buy_NF():
    game.buy_upgrade(u22_NF)
    global u22_NF_Button
    u22_NF.active = 2
    root.after(100)
    destroyUpgradeButton(u22_NF_Button, u22_NF)

def buy_CE():
    game.buy_upgrade(u23_CE)
    global u23_CE_Button
    u23_CE.active = 2
    root.after(100)
    destroyUpgradeButton(u23_CE_Button, u23_CE)

    global u24_TE_Button
    u24_TE_Button = createUpgradeButton(u24_TE_Button, u24_TE, buy_TE)

def buy_TE():
    game.buy_upgrade(u24_TE)
    global u24_TE_Button
    u24_TE.active = 2
    root.after(100)
    destroyUpgradeButton(u24_TE_Button, u24_TE)

# Increasing Automators
def increase_a1_GC():
    a1_GC.increase(game)
    global a1_GC_Name
    global compressor_costs
    a1_GC_Name.config(a1_GC_Name, text = "Compressors: " + "{:,.0f}".format(a1_GC.count))
    a1_GC_Cost.config(a1_GC_Cost, text = a1_GC.showCost())
    productionF.update_idletasks()
    a1_GC_Button.place(x = (a1_GC_Name.winfo_width() + LPADDING))

def increase_a2_QS():
    a2_QS.increase(game)
    global a2_QS_Name
    global a2_QS_Cost
    global a2_QS_Button
    global a2_QS_Toggle
    a2_QS_Name.config(a2_QS_Name, text = "Quark Synthesizers: " + "{:,.0f}".format(a2_QS.count))
    a2_QS_Cost.config(a2_QS_Cost, text = a2_QS.showCost())
    productionF.update_idletasks()
    a2_QS_Button.place(x = (a2_QS_Name.winfo_width() + LPADDING))
    a2_QS_Toggle.place(x = (a2_QS_Name.winfo_width() + a2_QS_Button.winfo_width() + LPADDING + SPADDING))

def increase_a3_PS():
    a3_PS.increase(game)
    global a3_PS_Name
    global a3_PS_Cost
    global a3_PS_Button
    global a3_PS_Toggle
    a3_PS_Name.config(a3_PS_Name, text = "Proton Synthesizers: " + "{:,.0f}".format(a3_PS.count))
    a3_PS_Cost.config(a3_PS_Cost, text = a3_PS.showCost())
    productionF.update_idletasks()
    a3_PS_Button.place(x = (a3_PS_Name.winfo_width() + LPADDING))
    a3_PS_Toggle.place(x = (a3_PS_Name.winfo_width() + a3_PS_Button.winfo_width() + LPADDING + SPADDING))

def increase_a4_NS():
    a4_NS.increase(game)
    global a4_NS_Name
    global a4_NS_Cost
    global a4_NS_Button
    global a4_NS_Toggle
    a4_NS_Name.config(a4_NS_Name, text = "Neutron Synthesizers: " + "{:,.0f}".format(a4_NS.count))
    a4_NS_Cost.config(a4_NS_Cost, text = a4_NS.showCost())
    productionF.update_idletasks()
    a4_NS_Button.place(x = (a4_NS_Name.winfo_width() + LPADDING))
    a4_NS_Toggle.place(x = (a4_NS_Name.winfo_width() + a4_NS_Button.winfo_width() + LPADDING + SPADDING))





# Toggling Automators
def toggle_a2_QS():
    global a2_QS_Toggle
    if (a2_QS.toggle == 1):
        a2_QS.toggle = 0
        a2_QS_Toggle.config(a2_QS_Toggle, text = "OFF")
    else:
        a2_QS.toggle = 1
        a2_QS_Toggle.config(a2_QS_Toggle, text = "ON")

def toggle_a3_PS():
    global a3_PS_Toggle
    if (a3_PS.toggle == 1):
        a3_PS.toggle = 0
        a3_PS_Toggle.config(a3_PS_Toggle, text = "OFF")
    else:
        a3_PS.toggle = 1
        a3_PS_Toggle.config(a3_PS_Toggle, text = "ON")

def toggle_a4_NS():
    global a4_NS_Toggle
    if (a4_NS.toggle == 1):
        a4_NS.toggle = 0
        a4_NS_Toggle.config(a4_NS_Toggle, text = "OFF")
    else:
        a4_NS.toggle = 1
        a4_NS_Toggle.config(a4_NS_Toggle, text = "ON")




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
        global resourcesTitleLabel
        global energyLab
        global microbeLab
        # Creating and placing RESOURCE frame
        resourcesF = Frame(root, relief = RAISED, bd = 5, bg = "red", height = RESOURCE_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        resourcesF.place(x = LEFT_COLUMN_X, y = TOP_Y)
        # Creating and placing frame title
        resourcesTitleLabel = Label(resourcesF, text = "Resources", font = ("Terminal", 10))
        resourcesTitleLabel.place(relx = 0.5, y = 10, anchor="center")

        energyLab = createResourceLabel(energyLab, game.energy, "Energy")

        game.resourcesFrame = True

    # ACTIVATE UPGRADES FRAME at 10 energy
    global upgradesF
    if game.energy >= 5 and upgradesF == None:
        global upgradeTitleLabel
        global u1_GC_Button
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
        u1_GC_Button = createUpgradeButton(u1_GC_Button, u1_GC, buy_GC)
        game.upgradesFrame = True

    # ACTIVATE PRODUCTION FRAME after gravitational compression upgrade
    global productionF
    if game.productionFrame == False and productionF == None and u1_GC.active == 2:
        global productionTitleLabel
        global a1_GC_Name
        global a1_GC_Desc
        global a1_GC_Cost
        global a1_GC_Button
        # Creating and placing PRODUCTION frame
        productionF = Frame(root, relief = RAISED, bd = 5, bg = "green", height = PRODUCTION_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        productionF.place(x = LEFT_COLUMN_X, y = TOP_Y + RESOURCE_FRAME_HEIGHT + 5)
        # Creating and placing frame title
        productionTitleLabel = Label(productionF, text = "Production", font = ("Terminal", 10))
        productionTitleLabel.place(relx = 0.5, y = 10, anchor="center")
        # Updating 'game' to recognize production frame is active
        game.productionFrame = True

        # Creating the compressor automator
        results = createProducer(a1_GC_Name, "Compressors", a1_GC_Button, increase_a1_GC, a1_GC_Cost, a1_GC_Desc, False, None, None, a1_GC)
        a1_GC_Name = results[0]
        a1_GC_Button = results[1]
        a1_GC_Cost = results[2]
        a1_GC_Desc = results[3]

        # Adds compressors to the list of active autos
        active_autos.append(a1_GC)

    #Activate subatomic synthesis upgrade at 100 energy
    global u2_SS_Button
    global u3_TM_Button
    if u1_GC.active == 2 and u2_SS.active == 0 and game.energy >= 50 and u3_TM.active == 0:
        u2_SS_Button = createUpgradeButton(u2_SS_Button, u2_SS, buy_SS)
        u3_TM_Button = createUpgradeButton(u3_TM_Button, u3_TM, buy_TM)

    #Creates Temporal Momentum Frame
    global temporalF
    if temporalF == None and u3_TM.active == 2:
        global temporalTitleLabel
        global potentialLab
        global potentialDescLab
        global productivityBut
        global productivityLab
        global expansionLab
        global expansionBut
        global timeLab
        global innovationLab
        global u4_IN_Button
        global TEMPORAL_FRAME_HEIGHT
        global respecBut
        temporalF = Frame(root, relief = RAISED, bd = 5, bg = "cyan", height = TEMPORAL_FRAME_HEIGHT, width = MIDDLE_COLUMN_WIDTH)
        temporalF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)

        temporalTitleLabel = Label(temporalF, text = "Temporal Momentum", font = ("Terminal", 10))
        temporalTitleLabel.place(relx = 0.5, y = 10, anchor="center")
        temporalF.update_idletasks()
        label_height = temporalTitleLabel.winfo_height()

        potentialLab = Label(temporalF, text = "Potential: " + "{:,.0f}".format(game.maxpotential), font = ("Terminal", 10))
        potentialLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialLab.winfo_height()

        potentialDescLab = Label(temporalF, text = "+1 Potential at " + "{:,.0f}".format(game.potential_lifeforms_req) + " lifeforms", font = ("Terminal", 8))
        potentialDescLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialDescLab.winfo_height() + LPADDING

        productivityBut = tk.Button(temporalF, text = "Productivity", font = ("Terminal", 9), width = 13, command = buy_Productivity, state = DISABLED)
        productivityBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        productivityLab = Label(temporalF, text = "{:,.0f}".format(game.productivity), font = ("Terminal", 9))
        productivityLab.place(x = productivityBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + productivityBut.winfo_height() + SPADDING

        temporalF.update_idletasks()
        expansionBut = tk.Button(temporalF, text = "Expansion", font = ("Terminal", 9), width = 13, command = buy_Expansion, state = DISABLED)
        expansionBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        expansionLab = Label(temporalF, text = "{:,.0f}".format(game.expansion), font = ("Terminal", 9))
        expansionLab.place(x = expansionBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + expansionBut.winfo_height() + LPADDING

        respecBut = tk.Button(temporalF, text = "Respec", font = ("Terminal", 8), width = 8, command = respec_temporal, state = DISABLED)
        respecBut.place(x = PADDING, y = label_height + SPADDING)
        label_height = label_height + respecBut.winfo_height() + LPADDING

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

        global u4_IN_Button
        u4_IN_Button = createUpgradeButton(u4_IN_Button, u4_IN, buy_IN)

    # u6_GA Unlock milestone
    if (a1_GC.count >= 10 and u6_GA.active == 0):
        global u6_GA_Button
        u6_GA_Button = createUpgradeButton(u6_GA_Button, u6_GA, buy_GA)

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
            current_height = widget.winfo_height()
            if current_height < button_height:
                widget.place(y=current_y - button_height // 2 - current_height // 2)
            else: 
                widget.place(y=current_y - SPADDING - button_height // 2)

    # Updating variables
    UPGRADE_BUTTON_NEXTY = UPGRADE_BUTTON_NEXTY - button_height - PADDING
    UPGRADE_FRAME_HEIGHT = UPGRADE_FRAME_HEIGHT - button_height - PADDING
    upgradesF.config(height=UPGRADE_FRAME_HEIGHT)
    # Updating upgrade status
    upgrade.active = 2

# Function for adding a new producer to productions
def createProducer(namelabel, name, button, cmd, costlabel, desclabel, toggleflag, togglebut, togglecommand, automator):
    global PRODUCTION_LABEL_NEXTY
    global PRODUCTION_FRAME_HEIGHT
    global productionF

    namelabel = Label(productionF, text = name + ": " + "{:,.0f}".format(automator.count), font = ('Terminal', 10))
    namelabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY)
    productionF.update_idletasks()
    button = tk.Button(productionF, text = "+", font = ("Terminal", 10), command = cmd)
    button.place(x = (namelabel.winfo_width() + LPADDING), y = PRODUCTION_LABEL_NEXTY)
    productionF.update_idletasks()

    if (toggleflag):
        length = button.winfo_width() + namelabel.winfo_width() + LPADDING + SPADDING
        togglebut = tk.Button(productionF, text = "ON", font = ("Terminal", 10), command = togglecommand)
        togglebut.place(x = length, y = PRODUCTION_LABEL_NEXTY)
    
        productionF.update_idletasks()

    productionF.update_idletasks()
    costlabel = Label(productionF, text = automator.showCost(), font = ('Terminal', 9))
    costlabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + PADDING / 2 + namelabel.winfo_height())

    productionF.update_idletasks()
    desclabel = Label(productionF, text = automator.desc(), font = ('Terminal', 8), wraplength=LEFT_COLUMN_WIDTH - (PADDING * 2))
    desclabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + 2 * PADDING / 2 + namelabel.winfo_height() + costlabel.winfo_height())
    
    productionF.update_idletasks()
    
    totalheight = namelabel.winfo_height() + costlabel.winfo_height() + desclabel.winfo_height()

    PRODUCTION_LABEL_NEXTY = PRODUCTION_LABEL_NEXTY + totalheight + PADDING * 2
    PRODUCTION_FRAME_HEIGHT = PRODUCTION_FRAME_HEIGHT + totalheight + PADDING * 2
    productionF.config(height=PRODUCTION_FRAME_HEIGHT)

    # Adds automator to the list of active autos
    active_autos.append(automator)

    return namelabel, button, costlabel, desclabel, togglebut

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
    game = Game()
    # Cosmic
    if u1_GC.active == 1:
        if u1_GC.afford(game):
            u1_GC_Button.config(u1_GC_Button, state = ACTIVE)
        else:
            u1_GC_Button.config(u1_GC_Button, state = DISABLED)

    if u2_SS.active == 1:
        if u2_SS.afford(game):
            u2_SS_Button.config(u2_SS_Button, state = ACTIVE)
        else:
            u2_SS_Button.config(u2_SS_Button, state = DISABLED)

    if u3_TM.active == 1:
        if u3_TM.afford(game):
            u3_TM_Button.config(u3_TM_Button, state = ACTIVE)
        else:
            u3_TM_Button.config(u3_TM_Button, state = DISABLED)

    if u4_IN.active == 1:
        if u4_IN.afford(game):
            u4_IN_Button.config(u4_IN_Button, state = ACTIVE)
        else:
            u4_IN_Button.config(u4_IN_Button, state = DISABLED)

    if u5_NS.active == 1:
        if u5_NS.afford(game):
            u5_NS_Button.config(u5_NS_Button, state = ACTIVE)
        else:
            u5_NS_Button.config(u5_NS_Button, state = DISABLED)
    
    if u6_GA.active == 1:
        if u6_GA.afford(game):
            u6_GA_Button.config(u6_GA_Button, state = ACTIVE)
        else:
            u6_GA_Button.config(u6_GA_Button, state = DISABLED)
    
    if u7_QF.active == 1:
        if u7_QF.afford(game):
            u7_QF_Button.config(u7_QF_Button, state = ACTIVE)
        else:
            u7_QF_Button.config(u7_QF_Button, state = DISABLED)
    
    if u8_AF.active == 1:
        if u8_AF.afford(game):
            u8_AF_Button.config(u8_AF_Button, state = ACTIVE)
        else:
            u8_AF_Button.config(u8_AF_Button, state = DISABLED)

    if u9_DH.active == 1:
        if u9_DH.afford(game):
            u9_DH_Button.config(u9_DH_Button, state = ACTIVE)
        else:
            u9_DH_Button.config(u9_DH_Button, state = DISABLED)

    if u10_P1.active == 1:
        if u10_P1.afford(game):
            u10_P1_Button.config(u10_P1_Button, state = ACTIVE)
        else:
            u10_P1_Button.config(u10_P1_Button, state = DISABLED)

    if u11_P2.active == 1:
        if u11_P2.afford(game):
            u11_P2_Button.config(u11_P2_Button, state = ACTIVE)
        else:
            u11_P2_Button.config(u11_P2_Button, state = DISABLED)

    if u12_P3.active == 1:
        if u12_P3.afford(game):
            u12_P3_Button.config(u12_P3_Button, state = ACTIVE)
        else:
            u12_P3_Button.config(u12_P3_Button, state = DISABLED)

    if u13_P4.active == 1:
        if u13_P4.afford(game):
            u13_P4_Button.config(u13_P4_Button, state = ACTIVE)
        else:
            u13_P4_Button.config(u13_P4_Button, state = DISABLED)

    if u13_P4.active == 1:
        if u13_P4.afford(game):
            u13_P4_Button.config(u13_P4_Button, state = ACTIVE)
        else:
            u13_P4_Button.config(u13_P4_Button, state = DISABLED)

    root.after(100, afford_upgrades)


#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    if game.resourcesFrame == True:
        global energyLab
        global quarkLab
        global protonLab
        global neutronLab
        if (energyLab):
            energyLab.config(energyLab, text = "Energy: " + "{:,.0f}".format(game.energy))
        if (quarkLab):
            quarkLab.config(quarkLab, text = "Quarks: " + "{:,.0f}".format(game.quarks))
        if (protonLab):
            protonLab.config(protonLab, text = "Protons: " + "{:,.0f}".format(game.protons))
        if (neutronLab):
            neutronLab.config(neutronLab, text = "Neutrons: " + "{:,.0f}".format(game.neutrons))

    if game.temporalFrame == True:
        global timeLab
        global innovationLab
        potentialLab.config(potentialLab, text = "Potential: " + "{:,.0f}".format(game.maxpotential))
        potentialDescLab.config(potentialDescLab, text = "+1 Potential at " + "{:,.0f}".format(game.potential_lifeforms_req) + " lifeforms")
        timeLab.config(timeLab, text = "Time: " + "{:,.0f}".format(game.time) + " / " + "{:,.0f}".format(game.expansion * 1000))
        innovationLab.config(innovationLab, text = "Innovation: " + "{:,.0f}".format(game.innovation))

    root.after(100, update_labels) # schedule the function to be called again after 1000ms

def calculate_revenues():
    # Calls game to calculate revenue, giving the current active automators as well
    game.calculate_revenue(active_autos)
    
    root.after(100, calculate_revenues)

#Call to continously run update_labels function
root.after(100, update_labels)
root.after(100, check_milestones)
root.after(100, afford_upgrades)
root.after(100, calculate_revenues)

#Main call to run game and load in all frames/buttons/labels etc.
root.mainloop()