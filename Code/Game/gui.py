from tkinter import *
import tkinter as tk
from game import Game
import upgrades
import automators
import pickle


#Getting Instance of Game class & Initializing game
game = Game()
game.init()

# Initializing Upgrades
active_upgrades = []
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
u15_GF = upgrades.Gravitational_Flucuations()
u16_QA = upgrades.Quark_Acceleration()
u17_PP = upgrades.Proton_Processor()
u18_NP = upgrades.Neutron_Processor()
u19_HC = upgrades.Hydrogenic_Catalyst()
u20_HE = upgrades.Helium_Extractor()
u21_CS = upgrades.Create_Sun()
u22_NF = upgrades.Nuclear_Fusion()
u23_CE = upgrades.Create_Earth()
u24_CD = upgrades.Cool_Down()
u25_NFI = upgrades.Nuclear_Fusion_Increase()
u26_DNA = upgrades.DNA_Points()
u27_GM = upgrades.GeneticMutation()
u28_MA = upgrades.Metabolic_Adaptation()
u29_AR = upgrades.Asexual_Reproduction()


# Initializing Automators
active_autos = []
a1_GC = automators.Compressor()
a2_QS = automators.Quark_Synthesizer()
a3_PS = automators.Proton_Synthesizer()
a4_NS = automators.Neutron_Synthesizer()
a5_HyF = automators.Hydrogen_Fabricator()
a6_HeF = automators.Helium_Fabricator()
a7_NF = automators.Nuclear_Fusion()












#Variables for Sizes
SPADDING = 5
PADDING = 10
LPADDING = 15

ROOT_HEIGHT = 1
ROOT_WIDTH = 1

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
hydrogenLab = None
heliumLab = None
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
a5_HyF_Name = None
a5_HyF_Desc = None
a5_HyF_Cost = None
a5_HyF_Toggle = None
a6_HeF_Name = None
a6_HeF_Desc = None
a6_HeF_Cost = None
a6_HeF_Toggle = None
a7_NF_Name = None
a7_NF_Desc = None
a7_NF_Cost = None
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
u17_PP_Button = None
u18_NP_Button = None
u19_HC_Button = None
u20_HE_Button = None
u21_CS_Button = None
u22_NF_Button = None
u23_CE_Button = None
u24_CD_Button = None
u26_DNA_Button = None
u27_GM_Button = None
u28_MA_Button = None
u29_AR_Button = None

# Automators
a1_GC_Button = None # Compressor
a2_QS_Button = None # Quark Synthesizer
a3_PS_Button = None # Proton Synthesizer
a4_NS_Button = None # Neutron Synthesizer
a5_HyF_Button = None # Hydrogen Fabricator
a6_HeF_Button = None # Helium Fabricator
a7_NF_Button = None # Nuclear Fusion















def create_energy():
    game.create_energy()

def create_life():
    game.create_life()

def save_state():
    state = vars(game.get())
    # my_globals = globals()
    # for g in my_globals:
    #     if isinstance(my_globals[g], object):
    #         print('b')
    #     else:
    #         state[g] = my_globals[g]
    with open('savefile.dat', 'wb') as f:
        pickle.dump(state, f)

def load_state():
    with open('savefile.dat', 'rb') as f:
        state = pickle.load(f)
    
    for key, value in state.items():
        setattr(game, key, value)
    
    # globals().update(state)

#Main Frame of Game
root = tk.Tk()
root.title = ("Eco-Evolution")
root.geometry("1440x1100")
root.configure(background='black')

root.update_idletasks()
ROOT_HEIGHT = root.winfo_height()
ROOT_WIDTH = root.winfo_width()

# Create a canvas widget
canvas = tk.Canvas(root, height = ROOT_HEIGHT)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# add a scrollbar to the canvas
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Creating the Main Frame
mainframe = tk.Frame(canvas, height = ROOT_HEIGHT)

#CREATING Frames to go on root
timeline = Frame(mainframe, relief = RAISED, bd = 5, bg = "black", height = 90, width = 2000)
lifeForms = Frame(mainframe, relief= RAISED, bd = 5, bg = "white", height = 40, width = 2000)
visuals = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = 450, width = 450)
createLabel = Frame(mainframe, bg = "white", height = 40, width = 100)
# time = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = 40, width = 175)
saveframe = Frame(mainframe, relief = RAISED, bd = 5, bg = "white",  height = 40, width = 130)

mainframe.config(height = ROOT_HEIGHT, width = 1440, background= "black")
mainframe.update_idletasks()

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)
lifeForms.place(x = 20, y = 90)
visuals.place(x = 900, y = TOP_Y)
createLabel.place(x = 20, y = 135)
# time.place(x = 500, y = 135)
saveframe.place(x = ROOT_WIDTH - 150, y = 135)

messageCount = 0
timelineLabel = None
def printMessage(message):
    global messageCount
    global timelineLabel
    if messageCount == 0:
        timelineLabel = Label(timeline, text = message + "\n", anchor='w', justify='left', font = ("Terminal", 10), fg = "white", bg = "black")
        timelineLabel.place(y = 14)
        messageCount += 1
    elif messageCount < 5:
        timelineLabel.config(text = timelineLabel.cget("text") + message + '\n', anchor='w')
        messageCount += 1
    else:
        substr = timelineLabel.cget("text").split("\n", 1)[1]
        timelineLabel.config(text = substr + message + '\n')

# mainframe.config(height = ROOT_HEIGHT, width = 1440)
printMessage("Welcome to Eco-Evolution!")
mainframe.update_idletasks()

#Makes all Frames in GUI weighted the same
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

#CREATION of Labels that go onto Frames/Buttons
tlL = Label(timeline, text = "Timeline:", font = ('Terminal', 10), bg = "black", fg = "white")
lifeL = Label(lifeForms, text = "Lifeforms: " + "???", font = ("Terminal", 10), bg = "white")
eraL = Label(visuals, text = "Era: Cosmic", font = ("Terminal", 10), bg = "white")
lifeL.place(x = 0, y = 0)
tlL.place(x = 0, y = 0)
eraL.place(x = 0, y = 0)

#CREATION of Buttons
energyB = tk.Button(createLabel, text ="Energy", command = create_energy, font=('Terminal', 10))
# timeB = tk.Button(time, text = "Advance Time", font=('Terminal', 10), state = DISABLED)
saveB = tk.Button(saveframe, text="Save", command = save_state, font=('Terminal', 10))
loadB = tk.Button(saveframe, text="Load", command = load_state, font=('Terminal', 10))

#PLACEMENT of Buttons in Frames
energyB.place(in_ = createLabel, y = 10, x = 20)
# timeB.place(in_ = time, x = 25, y = 5)
saveB.place(in_ = saveframe, x = 10, y = 5 )
loadB.place(in_ = saveframe, x = 62, y = 5 )

# add the new frame to the canvas
canvas.create_window((0, 0), window = mainframe, anchor = 'nw')

def update_scrollregion(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(canvas.find_withtag("mainframe"), width=event.width if event else 0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

mainframe.bind("<Configure>", update_scrollregion)
mainframe.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

def scroll(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", scroll)






































#FUNCTIONS connected to Game class for in-game Buttons
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
    printMessage("You purchased Gravitational Compression! Passive energy coming soon!")
    destroyUpgradeButton(u1_GC_Button, u1_GC)

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
    printMessage("You bought Subatomic Synthesis! A new resource has emerged!")
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
    printMessage("You bought Temporal Momentum! Now we get to see your true potential...")
    destroyUpgradeButton(u3_TM_Button, u3_TM)

def buy_IN():
    game.buy_upgrade(u4_IN)
    global u4_IN_Button
    u4_IN.active = 2
    root.after(100)
    printMessage("You bought Innovation! Now you'll generate even more from Time being at a maximum!")
    destroyUpgradeButton(u4_IN_Button, u4_IN)

    global u10_P1_Button
    u10_P1_Button = createUpgradeButton(u10_P1_Button, u10_P1, buy_P1)

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
    printMessage("You bought Nucleosynthesis! More new resources! Yay!")
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

    global u8_AF_Button
    u8_AF_Button = createUpgradeButton(u8_AF_Button, u8_AF, buy_AF)
    global u17_PP_Button
    u17_PP_Button = createUpgradeButton(u17_PP_Button, u17_PP, buy_PP)
    global u18_NP_Button
    u18_NP_Button = createUpgradeButton(u18_NP_Button, u18_NP, buy_NP)

def buy_GA():
    global a1_GC
    a1_GC = game.buy_autoupgrade(u6_GA, a1_GC)
    global u6_GA_Button
    u6_GA.active = 2
    root.after(100)
    printMessage("You bought Gravitational Amplification! Your Energy is about to sky rocket!")
    destroyUpgradeButton(u6_GA_Button, u6_GA)
    global a1_GC_Desc
    a1_GC_Desc.config(a1_GC_Desc, text = a1_GC.desc())

    global u15_GF_Button
    u15_GF_Button = createUpgradeButton(u15_GF_Button, u15_GF, buy_GF)

def buy_QF():
    global a2_QS
    a2_QS = game.buy_autoupgrade(u7_QF, a2_QS)
    global u7_QF_Button
    u7_QF.active = 2
    root.after(100)
    printMessage("You bought Quark Fusion! Give me all of the Quarks!!")
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
    printMessage("You bought Atomic Fabrication! How many more resources are there?!?")
    destroyUpgradeButton(u8_AF_Button, u8_AF)

    global a5_HyF_Button
    global a5_HyF_Name
    global a5_HyF_Cost
    global a5_HyF_Desc
    global a5_HyF_Toggle
    results = createProducer(a5_HyF_Name, "Hydrogen Fabricator", a5_HyF_Button, increase_a5_HyF, a5_HyF_Cost, a5_HyF_Desc, True, a5_HyF_Toggle, toggle_a5_HyF, a5_HyF)
    a5_HyF_Name = results[0]
    a5_HyF_Button = results[1]
    a5_HyF_Cost = results[2]
    a5_HyF_Desc = results[3]
    a5_HyF_Toggle = results[4]
    active_autos.append(a5_HyF)
    global hydrogenLab
    hydrogenLab = createResourceLabel(hydrogenLab, game.hydrogen, "Hydrogen")

    global u9_DH_Button
    u9_DH_Button = createUpgradeButton(u9_DH_Button, u9_DH, buy_DH)
    global u19_HC_Button
    u19_HC_Button = createUpgradeButton(u19_HC_Button, u19_HC, buy_HC)

def buy_DH():
    game.buy_upgrade(u9_DH)
    global u9_DH_Button
    u9_DH.active = 2
    root.after(100)
    printMessage("You bought Discover Helium! Guess what? Another Resource!!!")
    destroyUpgradeButton(u9_DH_Button, u9_DH)

    global a6_HeF_Button
    global a6_HeF_Name
    global a6_HeF_Cost
    global a6_HeF_Desc
    global a6_HeF_Toggle
    results = createProducer(a6_HeF_Name, "Helium Fabricator", a6_HeF_Button, increase_a6_HeF, a6_HeF_Cost, a6_HeF_Desc, True, a6_HeF_Toggle, toggle_a6_HeF, a6_HeF)
    a6_HeF_Name = results[0]
    a6_HeF_Button = results[1]
    a6_HeF_Cost = results[2]
    a6_HeF_Desc = results[3]
    a6_HeF_Toggle = results[4]
    active_autos.append(a6_HeF)
    global heliumLab
    heliumLab = createResourceLabel(hydrogenLab, game.helium, "Helium")

    global u21_CS_Button
    u21_CS_Button = createUpgradeButton(u21_CS_Button, u21_CS, buy_CS)
    global u20_HE_Button
    u20_HE_Button = createUpgradeButton(u20_HE_Button, u20_HE, buy_HE)
    global u22_NF_Button
    u22_NF_Button = createUpgradeButton(u22_NF_Button, u22_NF, buy_NF)

def buy_P1():
    game.buy_upgrade(u10_P1)
    global u10_P1_Button
    u10_P1.active = 2
    root.after(100)
    printMessage("You bought Cosmic Burst! Look! More Potential!")
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
    printMessage("You bought Starlight Path! Even more Potential!")
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
    printMessage("You bought Quantum Leap! Gimmie all the Potential!")
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
    printMessage("You bought Galactic Investment! This was definitely worth it.")
    destroyUpgradeButton(u13_P4_Button, u13_P4)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

    global u14_P5_Button
    u14_P5_Button = createUpgradeButton(u14_P5_Button, u14_P5, buy_P5)

def buy_P5():
    game.buy_upgrade(u14_P5)
    global u14_P5_Button
    u14_P5.active = 2
    root.after(100)
    printMessage("You bought Nova Catalyst! May not know how it works, but we'll always take more potential!")
    destroyUpgradeButton(u14_P5_Button, u14_P5)
    game.set_max_potential()
    productivityBut.config(productivityBut, state = ACTIVE)
    expansionBut.config(expansionBut, state = ACTIVE)

def buy_GF():
    global a1_GC
    a1_GC = game.buy_autoupgrade(u15_GF, a1_GC)
    global u15_GF_Button
    u15_GF.active = 2
    root.after(100)
    printMessage("You bought Gravitational Fluctuations! You won't even know what to do with all this energy!")
    destroyUpgradeButton(u15_GF_Button, u15_GF)
    global a1_GC_Desc
    a1_GC_Desc.config(a1_GC_Desc, text = a1_GC.desc())


def buy_QA():
    global a2_QS
    a2_QS = game.buy_autoupgrade(u16_QA, a2_QS)
    global u16_QA_Button
    u16_QA.active = 2
    root.after(100)
    printMessage("You bought Quark Acceleration! You better not waste these!")
    destroyUpgradeButton(u16_QA_Button, u16_QA)
    global a2_QS_Desc
    a2_QS_Desc.config(a2_QS_Desc, text = a2_QS.desc())

def buy_PP():
    global a3_PS
    a3_PS = game.buy_autoupgrade(u17_PP, a3_PS)
    global u17_PP_Button
    u17_PP.active = 2
    root.after(100)
    printMessage("You bought Proton Processor! Now we're cooking with gas!")
    destroyUpgradeButton(u17_PP_Button, u17_PP)
    global a3_PS_Desc
    a3_PS_Desc.config(a3_PS_Desc, text = a3_PS.desc())

def buy_NP():
    global a4_NS
    a4_NS = game.buy_autoupgrade(u18_NP, a4_NS)
    global u18_NP_Button
    u18_NP.active = 2
    root.after(100)
    printMessage("You bought Neutron Processor! Did we just give those upgrades the same name basically? maybe...")
    destroyUpgradeButton(u18_NP_Button, u18_NP)
    global a4_NS_Desc
    a4_NS_Desc.config(a4_NS_Desc, text = a4_NS.desc())

def buy_HC():
    global a5_HyF
    a5_HyF = game.buy_autoupgrade(u19_HC, a5_HyF)
    global u19_HC_Button
    u19_HC.active = 2
    root.after(100)
    printMessage("You bought Hydrogenic Catalyst! Sounds expensive!")
    destroyUpgradeButton(u19_HC_Button, u19_HC)
    global a5_HyF_Desc
    a5_HyF_Desc.config(a5_HyF_Desc, text = a5_HyF.desc())

def buy_HE():
    global a6_HeF
    a6_HeF = game.buy_autoupgrade(u20_HE, a6_HeF)
    global u20_HE_Button
    u20_HE.active = 2
    root.after(100)
    printMessage("You bought Helium Extractor! Why is everyones voices getting so high?")
    destroyUpgradeButton(u20_HE_Button, u20_HE)
    global a6_HeF_Desc
    a6_HeF_Desc.config(a6_HeF_Desc, text = a6_HeF.desc())

def buy_CS():
    game.buy_upgrade(u21_CS)
    global u21_CS_Button
    u21_CS.active = 2
    root.after(100)
    printMessage("You just created the Sun! That thing is really really bright!!")
    destroyUpgradeButton(u21_CS_Button, u21_CS)

    global u23_CE_Button
    u23_CE_Button = createUpgradeButton(u23_CE_Button, u23_CE, buy_CE)

def buy_NF():
    game.buy_upgrade(u22_NF)
    global u22_NF_Button
    u22_NF.active = 2
    root.after(100)
    printMessage("You bought Nuclear Fusion! Your automators are basically automated!")
    destroyUpgradeButton(u22_NF_Button, u22_NF)

    global a7_NF_Button
    global a7_NF_Name
    global a7_NF_Cost
    global a7_NF_Desc
    results = createProducer(a7_NF_Name, "Nuclear Fusion", a7_NF_Button, increase_a7_NF, a7_NF_Cost, a7_NF_Desc, False, None, None, a7_NF)
    a7_NF_Name = results[0]
    a7_NF_Button = results[1]
    a7_NF_Cost = results[2]
    a7_NF_Desc = results[3]
    active_autos.append(a7_NF)

def buy_CE():
    game.buy_upgrade(u23_CE)
    global u23_CE_Button
    u23_CE.active = 2
    root.after(100)
    printMessage("Woah! What's that big red ball? Looks pretty hot, we should let it cool down for a bit...")
    destroyUpgradeButton(u23_CE_Button,u23_CE)
    
    global u24_CD_Button
    u24_CD_Button = createUpgradeButton(u24_CD_Button, u24_CD, buy_CD)

def buy_CD():
    game.buy_upgrade(u24_CD)
    global u24_CD_Button
    u24_CD.active = 2
    root.after(100)
    printMessage("That's better, looks like theres some cool things down there, we should go check it out!")
    destroyUpgradeButton(u24_CD_Button,u24_CD)
    global u26_DNA_Button
    u26_DNA_Button = createUpgradeButton(u26_DNA_Button, u26_DNA, buy_DNA)
    

def buy_DNA():
    game.buy_upgrade(u26_DNA)
    global u26_DNA_Button
    u26_DNA.active = 2
    root.after(100)
    destroyResourceLabel(energyLab)
    destroyResourceLabel(quarkLab)
    destroyResourceLabel(protonLab)
    destroyResourceLabel(neutronLab)
    destroyResourceLabel(heliumLab)
    destroyResourceLabel(hydrogenLab)
    energyB.destroy()
    destroyProducer(a1_GC_Name, a1_GC_Cost, a1_GC_Desc, a1_GC_Button, None, a1_GC)
    destroyProducer(a2_QS_Name, a2_QS_Cost, a2_QS_Desc, a2_QS_Button, a2_QS_Toggle, a2_QS)
    destroyProducer(a3_PS_Name, a3_PS_Cost, a3_PS_Desc, a3_PS_Button, a3_PS_Toggle, a3_PS)
    destroyProducer(a4_NS_Name, a4_NS_Cost, a4_NS_Desc, a4_NS_Button, a4_NS_Toggle, a4_NS)
    destroyProducer(a5_HyF_Name, a5_HyF_Cost, a5_HyF_Desc, a5_HyF_Button, a5_HyF_Toggle, a5_HyF)
    destroyProducer(a6_HeF_Name, a6_HeF_Cost, a6_HeF_Desc, a6_HeF_Button, a6_HeF_Toggle, a6_HeF)
    destroyProducer(a7_NF_Name, a7_NF_Cost, a7_NF_Desc, a7_NF_Button, None, a7_NF)
    printMessage("Welcome to the Pre-Cambrian Era!")
    printMessage("Don't freak out, you won't be needing any of that stuff anymore...")
    printMessage("Check out your new button! I wonder what it makes now?")
    root.config(background='darkblue')
    destroyUpgradeButton(u26_DNA_Button, u26_DNA)
    global lifeB
    lifeB = tk.Button(createLabel, text ="Create Life", command = create_life, font=('Terminal', 10))
    createLabel.config(width = 140)
    lifeB.place(in_ = createLabel, y = 10, x = 20)
    lifeL.destroy()
    lifeL = Label(lifeForms, text = "Lifeforms: " + game.microbes, font = ("Terminal", 10), bg = "white")
    global productionFy
    productionFy = productionF.winfo_y()
    productionF.config(y = productionFy + 25)
    root.after(100)
    

def buy_GM():
    game.buy_upgrade(u27_GM)
    global u27_GM_Button
    u27_GM.active = 2
    root.after(100)
    destroyUpgradeButton(u27_GM)

def buy_MA():
    game.buy_upgrade(u28_MA)
    global u28_MA_Button
    u28_MA.active = 2
    root.after(100)
    destroyUpgradeButton(u28_MA)

def buy_AR():
    game.buy_upgrade(u29_AR)
    global u29_AR_Button
    u29_AR.active = 2
    root.after(100)
    destroyUpgradeButton(u29_AR)
























# Increasing Automators
def increase_a1_GC():
    temp = 0
    while a1_GC.afford(game) and temp < 5:
        a1_GC.increase(game)
        global a1_GC_Name
        global compressor_costs
        a1_GC_Name.config(a1_GC_Name, text = "Compressors: " + "{:,.0f}".format(a1_GC.count))
        a1_GC_Cost.config(a1_GC_Cost, text = a1_GC.showCost())
        productionF.update_idletasks()
        a1_GC_Button.place(x = (a1_GC_Name.winfo_width() + LPADDING))
        temp += 1

def increase_a2_QS():
    temp = 0
    while a2_QS.afford(game) and temp < 5:
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
        temp += 1
        
def increase_a3_PS():
    temp = 0
    while a3_PS.afford(game) and temp < 5:
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
        temp += 1

def increase_a4_NS():
    temp = 0
    while a4_NS.afford(game) and temp < 5:
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
        temp += 1

def increase_a5_HyF():
    temp = 0
    while a5_HyF.afford(game) and temp < 5:
        a5_HyF.increase(game)
        global a5_HyF_Name
        global a5_HyF_Cost
        global a5_HyF_Button
        global a5_HyF_Toggle
        a5_HyF_Name.config(a5_HyF_Name, text = "Hydrogen Fabricator: " + "{:,.0f}".format(a5_HyF.count))
        a5_HyF_Cost.config(a5_HyF_Cost, text = a5_HyF.showCost())
        productionF.update_idletasks()
        a5_HyF_Button.place(x = (a5_HyF_Name.winfo_width() + LPADDING))
        a5_HyF_Toggle.place(x = (a5_HyF_Name.winfo_width() + a5_HyF_Button.winfo_width() + LPADDING + SPADDING))
        temp += 1

def increase_a6_HeF():
    temp = 0
    while a6_HeF.afford(game) and temp < 5:
        a6_HeF.increase(game)
        global a6_HeF_Name
        global a6_HeF_Cost
        global a6_HeF_Button
        global a6_HeF_Toggle
        a6_HeF_Name.config(a6_HeF_Name, text = "Helium Fabricator: " + "{:,.0f}".format(a6_HeF.count))
        a6_HeF_Cost.config(a6_HeF_Cost, text = a6_HeF.showCost())
        productionF.update_idletasks()
        a6_HeF_Button.place(x = (a6_HeF_Name.winfo_width() + LPADDING))
        a6_HeF_Toggle.place(x = (a6_HeF_Name.winfo_width() + a6_HeF_Button.winfo_width() + LPADDING + SPADDING))
        temp += 1

def increase_a7_NF():
    temp = 0
    while game.hydrogen >= a7_NF.upcost[0][1] and game.helium >= a7_NF.upcost[1][1] and temp < 5:
        a7_NF.increase(game)
        global a7_NF_Name
        global a7_NF_Cost
        global a7_NF_Button
        a7_NF_Name.config(a7_NF_Name, text = "Nuclear Fusion: " + "{:,.0f}".format(a7_NF.count))
        a7_NF_Cost.config(a7_NF_Cost, text = a7_NF.showCost())
        productionF.update_idletasks()
        a7_NF_Button.place(x = (a7_NF_Name.winfo_width() + LPADDING))

        global a1_GC
        global a2_QS
        global a3_PS
        global a4_NS
        global a5_HyF
        global a6_HeF
        autos = game.buy_autoupgrade(u25_NFI, a1_GC, a2_QS, a3_PS, a4_NS, a5_HyF, a6_HeF, a7_NF)
        a1_GC = autos[0]
        a2_QS = autos[1]
        a3_PS = autos[2]
        a4_NS = autos[3]
        a5_HyF = autos[4]
        a6_HeF = autos[5]

        global a1_GC_Desc
        a1_GC_Desc.config(a1_GC_Desc, text = a1_GC.desc())
        global a2_QS_Desc
        a2_QS_Desc.config(a2_QS_Desc, text = a2_QS.desc())
        global a3_PS_Desc
        a3_PS_Desc.config(a3_PS_Desc, text = a3_PS.desc())
        global a4_NS_Desc
        a4_NS_Desc.config(a4_NS_Desc, text = a4_NS.desc())
        global a5_HyF_Desc
        a5_HyF_Desc.config(a5_HyF_Desc, text = a5_HyF.desc())
        global a6_HeF_Desc
        a6_HeF_Desc.config(a6_HeF_Desc, text = a6_HeF.desc())
        temp += 1














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

def toggle_a5_HyF():
    global a5_HyF_Toggle
    if (a5_HyF.toggle == 1):
        a5_HyF.toggle = 0
        a5_HyF_Toggle.config(a5_HyF_Toggle, text = "OFF")
    else:
        a5_HyF.toggle = 1
        a5_HyF_Toggle.config(a5_HyF_Toggle, text = "ON")

def toggle_a6_HeF():
    global a6_HeF_Toggle
    if (a6_HeF.toggle == 1):
        a6_HeF.toggle = 0
        a6_HeF_Toggle.config(a6_HeF_Toggle, text = "OFF")
    else:
        a6_HeF.toggle = 1
        a6_HeF_Toggle.config(a6_HeF_Toggle, text = "ON")








































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
        resourcesF = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = RESOURCE_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        resourcesF.place(x = LEFT_COLUMN_X, y = TOP_Y)
        # Creating and placing frame title
        resourcesTitleLabel = Label(resourcesF, text = "Resources", font = ("Terminal", 10), bg = "white")
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
        upgradesF = Frame (mainframe, relief = RAISED, bd = 5, bg = "white", height = UPGRADE_FRAME_HEIGHT, width = MIDDLE_COLUMN_WIDTH)
        upgradesF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)
        # Creating and placing frame title
        upgradesL = Label(upgradesF, text = "Upgrades", font = ("Terminal", 10), bg = "white")
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
        productionF = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = PRODUCTION_FRAME_HEIGHT, width = LEFT_COLUMN_WIDTH)
        productionF.place(x = LEFT_COLUMN_X, y = TOP_Y + RESOURCE_FRAME_HEIGHT + 5)
        # Creating and placing frame title
        productionTitleLabel = Label(productionF, text = "Production", font = ("Terminal", 10), bg = "white")
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
        temporalF = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = TEMPORAL_FRAME_HEIGHT, width = MIDDLE_COLUMN_WIDTH)
        temporalF.place(x = MIDDLE_COLUMN_X, y = TOP_Y)

        temporalTitleLabel = Label(temporalF, text = "Temporal Momentum", font = ("Terminal", 10), bg = "white")
        temporalTitleLabel.place(relx = 0.5, y = 10, anchor="center")
        temporalF.update_idletasks()
        label_height = temporalTitleLabel.winfo_height()

        potentialLab = Label(temporalF, text = "Potential: " + "{:,.0f}".format(game.maxpotential), font = ("Terminal", 10), bg = "white")
        potentialLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialLab.winfo_height()

        potentialDescLab = Label(temporalF, text = "+1 Potential at " + "{:,.0f}".format(game.potential_lifeforms_req) + " lifeforms", font = ("Terminal", 8), bg = "white")
        potentialDescLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialDescLab.winfo_height() + LPADDING

        productivityBut = tk.Button(temporalF, text = "Productivity", font = ("Terminal", 9), width = 13, command = buy_Productivity, state = DISABLED)
        productivityBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        productivityLab = Label(temporalF, text = "{:,.0f}".format(game.productivity), font = ("Terminal", 9), bg = "white")
        productivityLab.place(x = productivityBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + productivityBut.winfo_height() + SPADDING

        temporalF.update_idletasks()
        expansionBut = tk.Button(temporalF, text = "Expansion", font = ("Terminal", 9), width = 13, command = buy_Expansion, state = DISABLED)
        expansionBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        expansionLab = Label(temporalF, text = "{:,.0f}".format(game.expansion), font = ("Terminal", 9), bg = "white")
        expansionLab.place(x = expansionBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + expansionBut.winfo_height() + LPADDING

        respecBut = tk.Button(temporalF, text = "Respec", font = ("Terminal", 8), width = 8, command = respec_temporal, state = DISABLED)
        respecBut.place(x = PADDING, y = label_height + SPADDING)
        label_height = label_height + respecBut.winfo_height() + LPADDING

        timeLab = Label(temporalF, text = "Time: " + "{:,.0f}".format(game.time) + " / " + "{:,.0f}".format(game.expansion * 1000), font = ("Terminal", 10), bg = "white")
        timeLab.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        label_height = label_height + timeLab.winfo_height() + SPADDING

        innovationLab = Label(temporalF, text = "Innovation: " + "{:,.0f}".format(game.innovation), font = ("Terminal", 10), bg = "white")
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

    if (game.microbes > 0 and u26_DNA.active == 2): 
            microbeLab = createResourceLabel(microbeLab, game.microbe, "Microbes: ")
    

    root.after(100, check_milestones)








































# Function for adding a new resource to resources frame
def createResourceLabel(label, resource, name):
    global RESOURCE_FRAME_HEIGHT
    global RESOURCE_LABEL_NEXTY
    global PRODUCTION_FRAME_TOP
    label = Label(resourcesF, text = name + ": " + "{:,.0f}".format(resource), font = ('Terminal', 10), bg = "white")
    label.place(x = PADDING, y = RESOURCE_LABEL_NEXTY)
    resourcesF.update_idletasks()
    label_height = label.winfo_height()
    RESOURCE_FRAME_HEIGHT = RESOURCE_FRAME_HEIGHT + label_height + PADDING
    RESOURCE_LABEL_NEXTY = RESOURCE_LABEL_NEXTY + label_height + PADDING
    PRODUCTION_FRAME_TOP = PRODUCTION_FRAME_TOP + label_height + PADDING
    resourcesF.config(height=RESOURCE_FRAME_HEIGHT)
    if (productionF != None):
        productionF.place(y = PRODUCTION_FRAME_TOP)

    # global ROOT_HEIGHT
    # ROOT_HEIGHT += (label_height + PADDING) * 0.9
    # mainframe.config(height = ROOT_HEIGHT)
    # mainframe.update_idletasks()
    # update_scrollregion()

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

    # global ROOT_HEIGHT
    # ROOT_HEIGHT -= (label_height + PADDING) * 0.9
    # mainframe.config(height = ROOT_HEIGHT)
    # mainframe.update_idletasks()
    # update_scrollregion()


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
    button.place(in_ = upgradesF, relx = 0.5, y = UPGRADE_BUTTON_NEXTY, anchor=('nw'))
    button.place_configure(anchor='n')
    upgradesF.update_idletasks()
    button_height = button.winfo_height()
    button.place(in_ = upgradesF, relx = 0.5, y = UPGRADE_BUTTON_NEXTY, anchor=('nw'))
    button.place_configure(anchor='n')
    
    # Updating frame height values
    UPGRADE_FRAME_HEIGHT = UPGRADE_FRAME_HEIGHT + button_height + PADDING
    UPGRADE_BUTTON_NEXTY = UPGRADE_BUTTON_NEXTY + button_height + PADDING
    upgradesF.config(height=UPGRADE_FRAME_HEIGHT)
    # Setting active status of upgrade
    upgrade.active = 1

    global ROOT_HEIGHT
    ROOT_HEIGHT += (button_height + PADDING) * 0.9
    mainframe.config(height = ROOT_HEIGHT)
    mainframe.update_idletasks()
    update_scrollregion()

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
        if current_y >= button_y:
            widget.place(y=current_y - button_height - LPADDING)

    # Updating variables
    UPGRADE_BUTTON_NEXTY = UPGRADE_BUTTON_NEXTY - button_height - PADDING
    UPGRADE_FRAME_HEIGHT = UPGRADE_FRAME_HEIGHT - button_height - PADDING
    upgradesF.config(height=UPGRADE_FRAME_HEIGHT)
    # Updating upgrade status
    upgrade.active = 2

    global ROOT_HEIGHT
    ROOT_HEIGHT -= (button_height + PADDING) * 0.9
    mainframe.config(height = ROOT_HEIGHT)
    mainframe.update_idletasks()
    update_scrollregion()

# Function for adding a new producer to productions
def createProducer(namelabel, name, button, cmd, costlabel, desclabel, toggleflag, togglebut, togglecommand, automator):
    global PRODUCTION_LABEL_NEXTY
    global PRODUCTION_FRAME_HEIGHT
    global productionF

    namelabel = Label(productionF, text = name + ": " + "{:,.0f}".format(automator.count), font = ('Terminal', 10), bg = "white")
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
    costlabel = Label(productionF, text = automator.showCost(), font = ('Terminal', 9), wraplength=LEFT_COLUMN_WIDTH - (PADDING * 2), bg = "white")
    costlabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + PADDING / 2 + namelabel.winfo_height())

    productionF.update_idletasks()
    desclabel = Label(productionF, text = automator.desc(), font = ('Terminal', 8), wraplength=LEFT_COLUMN_WIDTH - (PADDING * 2), bg = "white")
    desclabel.place(x = PADDING, y = PRODUCTION_LABEL_NEXTY + 2 * PADDING / 2 + namelabel.winfo_height() + costlabel.winfo_height())
    
    productionF.update_idletasks()
    
    totalheight = namelabel.winfo_height() + costlabel.winfo_height() + desclabel.winfo_height()

    PRODUCTION_LABEL_NEXTY = PRODUCTION_LABEL_NEXTY + totalheight + PADDING * 2
    PRODUCTION_FRAME_HEIGHT = PRODUCTION_FRAME_HEIGHT + totalheight + PADDING * 2
    productionF.config(height=PRODUCTION_FRAME_HEIGHT)

    # Adds automator to the list of active autos
    active_autos.append(automator)

    global ROOT_HEIGHT
    ROOT_HEIGHT += (totalheight + PADDING * 2) * 0.9
    mainframe.config(height = ROOT_HEIGHT)
    mainframe.update_idletasks()
    update_scrollregion()

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
            # Moving up 20 + 5 + button_height/2
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

    global ROOT_HEIGHT
    ROOT_HEIGHT -= (totalheight + PADDING * 2) * 0.9
    mainframe.config(height = ROOT_HEIGHT)
    mainframe.update_idletasks()
    update_scrollregion()


































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

    if u14_P5.active == 1:
        if u14_P5.afford(game):
            u14_P5_Button.config(u14_P5_Button, state = ACTIVE)
        else:
            u14_P5_Button.config(u14_P5_Button, state = DISABLED)
    
    if u15_GF.active == 1:
        if u15_GF.afford(game):
            u15_GF_Button.config(u15_GF_Button, state = ACTIVE)
        else:
            u15_GF_Button.config(u15_GF_Button, state = DISABLED)

    if u16_QA.active == 1:
        if u16_QA.afford(game):
            u16_QA_Button.config(u16_QA_Button, state = ACTIVE)
        else:
            u16_QA_Button.config(u16_QA_Button, state = DISABLED)

    if u17_PP.active == 1:
        if u17_PP.afford(game):
            u17_PP_Button.config(u17_PP_Button, state = ACTIVE)
        else:
            u17_PP_Button.config(u17_PP_Button, state = DISABLED)
    
    if u18_NP.active == 1:
        if u18_NP.afford(game):
            u18_NP_Button.config(u18_NP_Button, state = ACTIVE)
        else:
            u18_NP_Button.config(u18_NP_Button, state = DISABLED)

    if u19_HC.active == 1:
        if u19_HC.afford(game):
            u19_HC_Button.config(u19_HC_Button, state = ACTIVE)
        else:
            u19_HC_Button.config(u19_HC_Button, state = DISABLED)
    
    if u20_HE.active == 1:
        if u20_HE.afford(game):
            u20_HE_Button.config(u20_HE_Button, state = ACTIVE)
        else:
            u20_HE_Button.config(u20_HE_Button, state = DISABLED)

    if u21_CS.active == 1:
        if u21_CS.afford(game):
            u21_CS_Button.config(u21_CS_Button, state = ACTIVE)
        else:
            u21_CS_Button.config(u21_CS_Button, state = DISABLED)

    if u22_NF.active == 1:
        if u22_NF.afford(game):
            u22_NF_Button.config(u22_NF_Button, state = ACTIVE)
        else:
            u22_NF_Button.config(u22_NF_Button, state = DISABLED)

    if u23_CE.active == 1:
        if u23_CE.afford(game):
            u23_CE_Button.config(u23_CE_Button, state = ACTIVE)
        else:
            u23_CE_Button.config(u23_CE_Button, state = DISABLED)
    
    if u24_CD.active == 1:
        if u24_CD.afford(game):
            u24_CD_Button.config(u24_CD_Button, state = ACTIVE)
        else:
            u24_CD_Button.config(u24_CD_Button, state = DISABLED)

    if u26_DNA.active == 1:
        if u26_DNA.afford(game):
            u26_DNA_Button.config(u26_DNA_Button, state = ACTIVE)
        else:
            u26_DNA_Button.config(u26_DNA_Button, state = DISABLED)

    if u27_GM.active == 1:
        if u27_GM.afford(game):
            u27_GM_Button.config(u27_GM_Button, state = ACTIVE)
        else:
            u27_GM_Button.config(u27_GM_Button, state = DISABLED)

    if u28_MA.active == 1:
        if u28_MA.afford(game):
            u28_MA_Button.config(u28_MA_Button, state = ACTIVE)
        else:
            u28_MA_Button.config(u28_MA_Button, state = DISABLED)

    if u29_AR.active == 1:
        if u29_AR.afford(game):
            u29_AR_Button.config(u29_AR_Button, state = ACTIVE)
        else:
            u29_AR_Button.config(u29_AR_Button, state = DISABLED)
    
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
        if (hydrogenLab):
            hydrogenLab.config(hydrogenLab, text = "Hydrogen: " + "{:,.0f}".format(game.hydrogen))
        if (heliumLab):
            heliumLab.config(heliumLab, text = "Helium: " + "{:,.0f}".format(game.helium))

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