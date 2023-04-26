from tkinter import *
import tkinter as tk
from game import Game
import upgrades
import automators
import pickle
import os
from PIL import Image, ImageTk
import time


#Getting Instance of Game class & Initializing game
game = Game()
game.init()

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
backgrounds = os.path.abspath(os.path.join(root, "Assets/BackGround"))

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
u26_DNA = upgrades.Create_Life()
u27_GM = upgrades.GeneticMutation()
u28_MA = upgrades.Metabolic_Adaptation()
u29_AR = upgrades.Asexual_Reproduction()
u30_MC = upgrades.Multicellularity()
u31_MP = upgrades.Membrane_Proteins()
u32_PS = upgrades.Photosynthesis()
u33_AM = upgrades.Aquaporin_Membranes()
u34_DA = upgrades.DNA_Amplifier()
u35_FL = upgrades.Flagella()
u36_CP = upgrades.Chloroplasts()
u37_MC = upgrades.Mitochondria()
u38_BP = upgrades.Biofilm_Production()
u39_CS = upgrades.Chemosynthesis()
u40_OX = upgrades.Oxygenation()
u41_DF = upgrades.Differentiation()
u42_SY = upgrades.Symbiosis()
u43_DT = upgrades.Diatoms()
u44_AB = upgrades.Algal_Blooms()
u45_MT = upgrades.Mixotrophy()
u46_OL = upgrades.Ozone_Layer()
u47_ES = upgrades.Ecosystems()
u48_NS = upgrades.Nervous_System()
u49_ES = upgrades.Endoskeleton()
u50_SB = upgrades.Swim_Bladder()
u51_EX = upgrades.Exoskeleton()
u52_MM = upgrades.Metamorphosis()
u53_IW = upgrades.Insectoid_Wings()
u54_OP = upgrades.Oviparity()
u55_LL = upgrades.Lungs_and_Limbs()
u56_IF = upgrades.Internal_Fertilization()
u57_TP = upgrades.Tetrapods()
u58_ET = upgrades.Ectothermy()
u59_RS = upgrades.Reptilian_Scales()
u60_EC = upgrades.Ecdysis()
u61_DH = upgrades.Double_Helix_Master()
u62_MG = upgrades.Mammary_Glands()
u63_FUR = upgrades.Fur()
u64_NC = upgrades.Neucortex()
u65_FF = upgrades.Flight_Feathers()
u66_BT = upgrades.Beaks_and_Talons()
u67_VC = upgrades.Vocalization_and_Coloration()
u68_AD = upgrades.Adaptability()
u69_DI = upgrades.Dinosaurs()
u70_IMM = upgrades.Increased_Muscle_Mass()
u71_CD = upgrades.Competition_and_Cooperation()
u72_CD = upgrades.Continental_Drift()
u73_CS = upgrades.Climate_Stabilization()
u74_SD = upgrades.Sacrifice_The_Dinosaurs()
u75_ER = upgrades.Evolutionary_Radiation()
u76_OT = upgrades.Opposable_Thumbs()
u77_IBS = upgrades.Increased_Brain_Size()
u78_SC = upgrades.Social_Complexity()
u79_TU = upgrades.Tool_Use()
u80_HS = upgrades.Homo_Sapiens()

# Initializing Automators
active_autos = []
a1_GC = automators.Compressor()
a2_QS = automators.Quark_Synthesizer()
a3_PS = automators.Proton_Synthesizer()
a4_NS = automators.Neutron_Synthesizer()
a5_HyF = automators.Hydrogen_Fabricator()
a6_HeF = automators.Helium_Fabricator()
a7_NF = automators.Nuclear_Fusion()
a8_NS = automators.Nutrient_Synthesis()
a9_HS = automators.Hydro_Synthesis()
a10_DNA = automators.DNA_Manufacturer()











#Variables for Sizes
SPADDING = 5
PADDING = 10
LPADDING = 15

ROOT_HEIGHT = 1
ROOT_WIDTH = 1

LEFT_COLUMN_WIDTH = 300
MIDDLE_COLUMN_WIDTH = 350
RIGHT_COLUMN_WIDTH = 350
VISUAL_COLUMN_WIDTH = 300

RESOURCE_FRAME_HEIGHT = 30
RESOURCE_LABEL_NEXTY = 25
SPECIES_FRAME_HEIGHT = 30
SPECIES_LABEL_NEXTY = 25

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
MIDDLE_COLUMN_X = LEFT_COLUMN_X + LEFT_COLUMN_WIDTH + PADDING
RIGHT_COLUMN_X = MIDDLE_COLUMN_X + MIDDLE_COLUMN_WIDTH + PADDING
VISUAL_COLUMN_X = RIGHT_COLUMN_X + RIGHT_COLUMN_WIDTH + PADDING

PRODUCTION_FRAME_TOP = RESOURCE_FRAME_HEIGHT + TOP_Y + PADDING

# GLOBAL LISTS
# Global Frames
resourcesF = None
upgradesF = None
productionF = None
temporalF = None
speciesF = None

# Global Titles
resourcesTitleLabel = None
upgradeTitleLabel = None
productionTitleLabel = None
temporalTitleLabel = None
speciesTitleLabel = None

# Global Labels
# Resources
energyLab = None
microbeLab = None
quarkLab = None
protonLab = None
neutronLab = None
hydrogenLab = None
heliumLab = None
dnaLab = None
nutrientLab = None
waterLab = None
VisualLab = None
spaceBG = None

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
a8_NS_Name = None
a8_NS_Desc = None
a8_NS_Cost = None
a8_NS_Toggle = None
a9_HS_Name = None
a9_HS_Desc = None
a9_HS_Cost = None
a9_HS_Toggle = None
a10_DNA_Name = None
a10_DNA_Desc = None
a10_DNA_Cost = None

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

# Species
microbesLab = None
algaeLab = None
fishLab = None
insectLab = None
amphibianLab = None
reptileLab = None
birdLab = None
mammalLab = None
dinosaurLab = None
primateLab = None

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
u30_MC_Button = None
u31_MP_Button = None
u32_PS_Button = None
u33_AM_Button = None
u34_DA_Button = None
u35_FL_Button = None
u36_CP_Button = None
u37_MC_Button = None
u38_BP_Button = None
u39_CS_Button = None
u40_OX_Button = None
u41_DF_Button = None
u42_SY_Button = None
u43_DT_Button = None
u44_AB_Button = None
u45_MT_Button = None
u46_OL_Button = None
u47_ES_Button = None
u48_NS_Button = None
u49_ES_Button = None
u50_SB_Button = None
u51_EX_Button = None
u52_MM_Button = None
u53_IW_Button = None
u54_OP_Button = None
u55_LL_Button = None
u56_IF_Button = None
u57_TP_Button = None
u58_ET_Button = None
u59_RS_Button = None
u60_EC_Button = None
u61_DH_Button = None
u62_MG_Button = None
u63_FUR_Button = None
u64_NC_Button = None
u65_FF_Button = None
u66_BT_Button = None
u67_VC_Button = None
u68_AD_Button = None
u69_DI_Button = None
u70_IMM_Button = None
u71_CD_Button = None
u72_CD_Button = None
u73_CS_Button = None
u74_SD_Button = None
u75_ER_Button = None
u76_OT_Button = None
u77_IBS_Button = None
u78_SC_Button = None
u79_TU_Button = None
u80_HS_Button = None

# Automators
a1_GC_Button = None # Compressor
a2_QS_Button = None # Quark Synthesizer
a3_PS_Button = None # Proton Synthesizer
a4_NS_Button = None # Neutron Synthesizer
a5_HyF_Button = None # Hydrogen Fabricator
a6_HeF_Button = None # Helium Fabricator
a7_NF_Button = None # Nuclear Fusion
a8_NS_Button = None
a9_HS_Button = None
a10_DNA_Button = None

#Images
space = Image.open(backgrounds + "\\background.png")
space = space.resize((260, 260), Image.LANCZOS)
i1 = Image.open(backgrounds + "\\cosmic1.png")
i1 = i1.resize((260, 260), Image.LANCZOS)
i2 = Image.open(backgrounds + "\\cosmic2.png")
i2 = i2.resize((260, 260), Image.LANCZOS)
i3 = Image.open(backgrounds + "\\cosmic3.png")
i3 = i3.resize((260, 260), Image.LANCZOS)
i4 = Image.open(backgrounds + "\\cosmic4.png")
i4 = i4.resize((260, 260), Image.LANCZOS)
i5 = Image.open(backgrounds + "\\cosmic5.png")
i5 = i5.resize((260, 260), Image.LANCZOS)
i6 = Image.open(backgrounds + "\\cosmic6.png")
i6 = i6.resize((260, 260), Image.LANCZOS)
i7 = Image.open(backgrounds + "\\cosmic7.png")
i7 = i7.resize((260, 260), Image.LANCZOS)
i8 = Image.open(backgrounds + "\\cosmic8.png")
i8 = i2.resize((260, 260), Image.LANCZOS)
i9 = Image.open(backgrounds + "\\cosmic9.png")
i9 = i9.resize((260, 260), Image.LANCZOS)
i10 = Image.open(backgrounds + "\\cosmic10.png")
i10 = i10.resize((260, 260), Image.LANCZOS)
i11 = Image.open(backgrounds + "\\cosmic11.png")
i11 = i11.resize((260, 260), Image.LANCZOS)
i12 = Image.open(backgrounds + "\\cosmic12.png")
i12 = i12.resize((260, 260), Image.LANCZOS)
i13 = Image.open(backgrounds + "\\cosmic13.png")
i13 = i13.resize((260, 260), Image.LANCZOS)
i14 = Image.open(backgrounds + "\\cosmic14.png")
i14 = i14.resize((260, 260), Image.LANCZOS)


def format_number(number, decimal):
    if number < 1000000000:
        return f"{number:,.{decimal}f}"
    if decimal == 0:
        decimal = 3
    else:
        decimal = 1
    if number < 1000000000000:
        number /= pow(10, 9)
        return f"{number:,.{decimal}f} Billion"
    if number < 1000000000000000:
        number /= pow(10, 12)
        return f"{number:,.{decimal}f} Trillion"
    if number < 1000000000000000000:
        number /= pow(10, 15)
        return f"{number:,.{decimal}f} Quadrillion"
    if number < 1000000000000000000000:
        number /= pow(10, 18)
        return f"{number:,.{decimal}f} Quintillion"
    if number < 1000000000000000000000000:
        number /= pow(10, 21)
        return f"{number:,.{decimal}f} Sextillion"
    if number < 1000000000000000000000000000:
        number /= pow(10, 24)
        return f"{number:,.{decimal}f} Septillion"
    if number < 1000000000000000000000000000000:
        number /= pow(10, 27)
        return f"{number:,.{decimal}f} Octillion"
    if number < 1000000000000000000000000000000000:
        number /= pow(10, 30)
        return f"{number:,.{decimal}f} Nonillion"
    if number < 1000000000000000000000000000000000000:
        number /= pow(10, 33)
        return f"{number:,.{decimal}f} Decillion"
    if number < 1000000000000000000000000000000000000000:
        number /= pow(10, 36)
        return f"{number:,.{decimal}f} Undecillion"
    if number < 1000000000000000000000000000000000000000000:
        number /= pow(10, 39)
        return f"{number:,.{decimal}f} Duodecillion"
    if number < 1000000000000000000000000000000000000000000000:
        number /= pow(10, 42)
        return f"{number:,.{decimal}f} Tredecillion"
    if number < 1000000000000000000000000000000000000000000000000:
        number /= pow(10, 45)
        return f"{number:,.{decimal}f} Quattuordecillion"
    if number < 1000000000000000000000000000000000000000000000000000:
        number /= pow(10, 48)
        return f"{number:,.{decimal}f} Quindecillion"
    if number < 1000000000000000000000000000000000000000000000000000000:
        number /= pow(10, 51)
        return f"{number:,.{decimal}f} Sexdecillion"
    if number < 1000000000000000000000000000000000000000000000000000000000:
        number /= pow(10, 54)
        return f"{number:,.{decimal}f} Septendecillion"
    if number < 1000000000000000000000000000000000000000000000000000000000000:
        number /= pow(10, 57)
        return f"{number:,.{decimal}f} Octodecillion"
    if number < 1000000000000000000000000000000000000000000000000000000000000000:
        number /= pow(10, 60)
        return f"{number:,.{decimal}f} Novemdecillion"
    if number < 1000000000000000000000000000000000000000000000000000000000000000000:
        number /= pow(10, 63)
        return f"{number:,.{decimal}f} Vigintillion"
    power = 66
    number /= pow(10, 66)
    while number > 1000:
        number /= 1000
        power += 3
    return f"{number:,.{decimal}f} * 10^" + str(power)











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
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d" % (screen_width, screen_height))
# root.geometry("1440x1100")
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
visuals = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = 300, width = 300)
createLabel = Frame(mainframe, bg = "white", height = 40, width = 100)
# time = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = 40, width = 175)
saveframe = Frame(mainframe, relief = RAISED, bd = 5, bg = "white",  height = 40, width = 130)

spaceBG = ImageTk.PhotoImage(space)
BGLab = Label(mainframe, image = spaceBG)
BGLab.image = spaceBG

mainframe.config(height = ROOT_HEIGHT, width = 1440, background= "black")
mainframe.update_idletasks()

#PLACEMENT of Frames on root
timeline.place(x = 20, y = 0)
lifeForms.place(x = 20, y = 90)
visuals.place(x = VISUAL_COLUMN_X, y = TOP_Y)
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
lifeL = Label(lifeForms, text = "Lifeforms: ???", font = ("Terminal", 10), bg = "white")
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
    global VisualLab
    u1_GC.active = 2
    root.after(100)
    printMessage("You purchased Gravitational Compression! Passive energy coming soon!")
    cosmic1 = ImageTk.PhotoImage(i1)
    VisualLab = Label(visuals, image = cosmic1)
    VisualLab.image = cosmic1
    VisualLab.place(relx=0.5, rely=0.52, anchor="center")
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
    # active_autos.append(a2_QS)
    quarkLab = createResourceLabel(quarkLab, game.quarks, "Quarks")
    cosmic2 = ImageTk.PhotoImage(i2)
    VisualLab.config(image = cosmic2)
    VisualLab.image = cosmic2
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
    cosmic3 = ImageTk.PhotoImage(i3)
    VisualLab.config(image = cosmic3)
    VisualLab.image = cosmic3
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
    # active_autos.append(a3_PS)
    results = createProducer(a4_NS_Name, "Neutron Synthesizers", a4_NS_Button, increase_a4_NS, a4_NS_Cost, a4_NS_Desc, True, a4_NS_Toggle, toggle_a4_NS, a4_NS)
    a4_NS_Name = results[0]
    a4_NS_Button = results[1]
    a4_NS_Cost = results[2]
    a4_NS_Desc = results[3]
    a4_NS_Toggle = results[4]
    # active_autos.append(a4_NS)
    protonLab = createResourceLabel(protonLab, game.protons, "Protons")
    neutronLab = createResourceLabel(neutronLab, game.neutrons, "Neutron")
    cosmic4 = ImageTk.PhotoImage(i4)
    VisualLab.config(image = cosmic4)
    VisualLab.image = cosmic4

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
    cosmic5 = ImageTk.PhotoImage(i5)
    VisualLab.config(image = cosmic5)
    VisualLab.image = cosmic5

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
    cosmic6 = ImageTk.PhotoImage(i6)
    VisualLab.config(image = cosmic6)
    VisualLab.image = cosmic6

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
    # active_autos.append(a5_HyF)
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
    # active_autos.append(a6_HeF)
    global heliumLab
    heliumLab = createResourceLabel(hydrogenLab, game.helium, "Helium")
    cosmic7 = ImageTk.PhotoImage(i7)
    VisualLab.config(image = cosmic7)
    VisualLab.image = cosmic7

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
    cosmic8 = ImageTk.PhotoImage(i8)
    VisualLab.config(image = cosmic8)
    VisualLab.image = cosmic8

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
    cosmic9 = ImageTk.PhotoImage(i9)
    VisualLab.config(image = cosmic9)
    VisualLab.image = cosmic9

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
    cosmic10 = ImageTk.PhotoImage(i10)
    VisualLab.config(image = cosmic10)
    VisualLab.image = cosmic10
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
    # active_autos.append(a7_NF)

def buy_CE():
    game.buy_upgrade(u23_CE)
    global u23_CE_Button
    u23_CE.active = 2
    root.after(100)
    printMessage("Woah! What's that big red ball? Looks pretty hot, we should let it cool down for a bit...")
    cosmic11 = ImageTk.PhotoImage(i11)
    VisualLab.config(image = cosmic11)
    VisualLab.image = cosmic11
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
    cosmic12 = ImageTk.PhotoImage(i12)
    VisualLab.config(image = cosmic12)
    VisualLab.image = cosmic12
    global u26_DNA_Button
    u26_DNA_Button = createUpgradeButton(u26_DNA_Button, u26_DNA, buy_DNA)
    

def buy_DNA():
    game.buy_upgrade(u26_DNA)
    global u26_DNA_Button
    u26_DNA.active = 2
    root.after(100)
    global energyLab
    global quarkLab
    global protonLab
    global neutronLab
    global heliumLab
    global hydrogenLab
    energyLab = destroyResourceLabel(energyLab)
    quarkLab = destroyResourceLabel(quarkLab)
    protonLab = destroyResourceLabel(protonLab)
    neutronLab = destroyResourceLabel(neutronLab)
    heliumLab = destroyResourceLabel(heliumLab)
    hydrogenLab = destroyResourceLabel(hydrogenLab)
    energyB.destroy()
    destroyProducer(a1_GC_Name, a1_GC_Cost, a1_GC_Desc, a1_GC_Button, None, a1_GC)
    destroyProducer(a2_QS_Name, a2_QS_Cost, a2_QS_Desc, a2_QS_Button, a2_QS_Toggle, a2_QS)
    destroyProducer(a3_PS_Name, a3_PS_Cost, a3_PS_Desc, a3_PS_Button, a3_PS_Toggle, a3_PS)
    destroyProducer(a4_NS_Name, a4_NS_Cost, a4_NS_Desc, a4_NS_Button, a4_NS_Toggle, a4_NS)
    destroyProducer(a5_HyF_Name, a5_HyF_Cost, a5_HyF_Desc, a5_HyF_Button, a5_HyF_Toggle, a5_HyF)
    destroyProducer(a6_HeF_Name, a6_HeF_Cost, a6_HeF_Desc, a6_HeF_Button, a6_HeF_Toggle, a6_HeF)
    destroyProducer(a7_NF_Name, a7_NF_Cost, a7_NF_Desc, a7_NF_Button, None, a7_NF)
    global active_autos
    active_autos = []
    printMessage("Welcome to the Pre-Cambrian Era!")
    printMessage("Don't freak out, you won't be needing any of that stuff anymore...")
    printMessage("Check out your new button! I wonder what it makes now?")
    cosmic13 = ImageTk.PhotoImage(i13)
    VisualLab.config(image = cosmic13)
    VisualLab.image = cosmic13
    root.config(background='darkblue')
    destroyUpgradeButton(u26_DNA_Button, u26_DNA)
    global lifeB
    global lifeL
    lifeB = tk.Button(createLabel, text ="Create Life", command = create_life, font=('Terminal', 10))
    createLabel.config(width = 140)
    lifeB.place(in_ = createLabel, y = 10, x = 20)
    game.lifeforms = 1
    lifeL.config(text = "Lifeforms: " + str(game.lifeforms))
    global speciesF
    global speciesTitleLabel
    speciesF = Frame(mainframe, relief = RAISED, bd = 5, bg = "white", height = RESOURCE_FRAME_HEIGHT, width = RIGHT_COLUMN_WIDTH)
    speciesF.place(x = RIGHT_COLUMN_X, y = TOP_Y)
    root.after(100)
    speciesTitleLabel = Label(speciesF, text = "Species", font = ("Terminal", 10), bg = "white")
    speciesTitleLabel.place(relx = 0.5, y = 10, anchor="center")
    root.after(100)
    

        



def buy_27_GM():
    game.buy_upgrade(u27_GM)
    global u27_GM_Button
    u27_GM.active = 2
    root.after(100)
    destroyUpgradeButton(u27_GM_Button, u27_GM)
    global dnaLab
    dnaLab = createResourceLabel(dnaLab, game.dna, "DNA")
    global u34_DA_Button
    u34_DA_Button = createUpgradeButton(u34_DA_Button, u34_DA, buy_34_DA)


def buy_28_MA():
    game.buy_upgrade(u28_MA)
    global u28_MA_Button
    u28_MA.active = 2
    root.after(100)
    destroyUpgradeButton(u28_MA_Button, u28_MA)
    global waterLab
    global u33_AM_Button
    waterLab = createResourceLabel(waterLab, game.water, "Water")
    u33_AM_Button = createUpgradeButton(u33_AM_Button, u33_AM, buy_33_AM)

def buy_29_AR():
    game.buy_upgrade(u29_AR)
    global u29_AR_Button
    u29_AR.active = 2
    root.after(100)
    destroyUpgradeButton(u29_AR_Button, u29_AR)
    global u35_FL_Button
    u35_FL_Button = createUpgradeButton(u35_FL_Button, u35_FL, buy_35_FL)


def buy_30_MC():
    game.buy_upgrade(u30_MC)
    global u30_MC_Button
    u30_MC.active = 2
    root.after(100)
    destroyUpgradeButton(u30_MC_Button, u30_MC)
    global a10_DNA_Button
    global a10_DNA_Name
    global a10_DNA_Cost
    global a10_DNA_Desc
    results = createProducer(a10_DNA_Name, "DNA Manufacturer", a10_DNA_Button, increase_a10_DNA, a10_DNA_Cost, a10_DNA_Desc, False, None, None, a10_DNA)
    a10_DNA_Name = results[0]
    a10_DNA_Button = results[1]
    a10_DNA_Cost = results[2]
    a10_DNA_Desc = results[3]
    # active_autos.append(a10_DNA)


def buy_31_MP():
    game.buy_upgrade(u31_MP)
    global u31_MP_Button
    u31_MP.active = 2
    root.after(100)
    destroyUpgradeButton(u31_MP_Button, u31_MP)
    global nutrientLab
    global u32_PS_Button
    nutrientLab = createResourceLabel(nutrientLab, game.nutrients, "Nutrients")
    u32_PS_Button = createUpgradeButton(u32_PS_Button, u32_PS, buy_32_PS)

def buy_32_PS():
    game.buy_upgrade(u32_PS)
    global u32_PS_Button
    u32_PS.active = 2
    root.after(100)
    destroyUpgradeButton(u32_PS_Button, u32_PS)
    global a8_NS_Button
    global a8_NS_Name
    global a8_NS_Cost
    global a8_NS_Desc
    global a8_NS_Toggle
    results = createProducer(a8_NS_Name, "Nutrient Synthesizer", a8_NS_Button, increase_a8_NS, a8_NS_Cost, a8_NS_Desc, True, a8_NS_Toggle, toggle_a8_NS, a8_NS)
    a8_NS_Name = results[0]
    a8_NS_Button = results[1]
    a8_NS_Cost = results[2]
    a8_NS_Desc = results[3]
    a8_NS_Toggle = results[4]
    # active_autos.append(a8_NS)

def buy_33_AM():
    game.buy_upgrade(u33_AM)
    global u33_AM_Button
    u33_AM.active = 2
    root.after(100)
    destroyUpgradeButton(u33_AM_Button, u33_AM)
    global a9_HS_Button
    global a9_HS_Name
    global a9_HS_Cost
    global a9_HS_Desc
    global a9_HS_Toggle
    results = createProducer(a9_HS_Name, "Hydro Synthesizer", a9_HS_Button, increase_a9_HS, a9_HS_Cost, a9_HS_Desc, True, a9_HS_Toggle, toggle_a9_HS, a9_HS)
    a9_HS_Name = results[0]
    a9_HS_Button = results[1]
    a9_HS_Cost = results[2]
    a9_HS_Desc = results[3]
    a9_HS_Toggle = results[4]
    # active_autos.append(a9_HS)

def buy_34_DA():
    global a10_DNA
    a10_DNA = game.buy_autoupgrade(u34_DA, a10_DNA)
    global u34_DA_Button
    u34_DA.active = 2
    root.after(100)
    printMessage("u34_DA")
    destroyUpgradeButton(u34_DA_Button, u34_DA)
    global a10_DNA_Desc
    a10_DNA_Desc.config(a10_DNA_Desc, text = a10_DNA.desc())

def buy_35_FL():
    game.buy_upgrade(u35_FL)
    global u35_FL_Button
    u35_FL.active = 2
    root.after(100)
    printMessage("u35_FL")
    destroyUpgradeButton(u35_FL_Button, u35_FL)
    global u38_BP_Button
    u38_BP_Button = createUpgradeButton(u38_BP_Button, u38_BP, buy_38_BP)

def buy_36_CP():
    global a8_NS
    a8_NS = game.buy_autoupgrade(u36_CP, a8_NS)
    global u36_CP_Button
    u36_CP.active = 2
    root.after(100)
    printMessage("u36_CP")
    destroyUpgradeButton(u36_CP_Button, u36_CP)
    global a8_NS_Desc
    a8_NS_Desc.config(a8_NS_Desc, text = a8_NS.desc())
    global u39_CS_Button
    u39_CS_Button = createUpgradeButton(u39_CS_Button, u39_CS, buy_39_CS)

def buy_37_MC():
    global a9_HS
    a9_HS = game.buy_autoupgrade(u37_MC, a9_HS)
    global u37_MC_Button
    u37_MC.active = 2
    root.after(100)
    printMessage("u37_MC")
    destroyUpgradeButton(u37_MC_Button, u37_MC)
    global a9_HS_Desc
    a9_HS_Desc.config(a9_HS_Desc, text = a9_HS.desc())
    global u40_OX_Button
    u40_OX_Button = createUpgradeButton(u40_OX_Button, u40_OX, buy_40_OX)

def buy_38_BP():
    game.buy_upgrade(u38_BP)

def buy_39_CS():
    game.buy_upgrade(u39_CS)

def buy_40_OX():
    game.buy_upgrade(u40_OX)

def buy_41_DF():
    game.buy_upgrade(u41_DF)
    global u41_DF_Button
    u41_DF.active = 2
    root.after(100)
    destroyUpgradeButton(u41_DF_Button, u41_DF)
    u43_DT_Button = createUpgradeButton(u43_DT_Button, u43_DT, buy_43_DT)

def buy_42_SY():
    game.buy_upgrade(u42_SY)

def buy_43_DT():
    game.buy_upgrade(u43_DT)

def buy_44_AB():
    game.buy_upgrade(u44_AB)

def buy_45_MT():
    game.buy_upgrade(u45_MT)

def buy_46_OL():
    game.buy_upgrade(u46_OL)

def buy_47_ES():
    game.buy_upgrade(u47_ES)

def buy_48_NS():
    game.buy_upgrade(u48_NS)

def buy_49_ES():
    game.buy_upgrade(u49_ES)

def buy_50_SB():
    game.buy_upgrade(u50_SB)

def buy_51_EX():
    game.buy_upgrade(u51_EX)

def buy_52_MM():
    game.buy_upgrade(u52_MM)

def buy_53_IW():
    game.buy_upgrade(u53_IW)

def buy_54_OP():
    game.buy_upgrade(u54_OP)

def buy_55_LL():
    game.buy_upgrade(u55_LL)

def buy_56_IF():
    game.buy_upgrade(u56_IF)

def buy_57_TP():
    game.buy_upgrade(u57_TP)

def buy_58_ET():
    game.buy_upgrade(u58_ET)

def buy_59_RS():
    game.buy_upgrade(u59_RS)

def buy_60_EC():
    game.buy_upgrade(u60_EC)

def buy_61_DH():
    game.buy_upgrade(u61_DH)

def buy_62_MG():
    game.buy_upgrade(u62_MG)

def buy_63_FUR():
    game.buy_upgrade(u63_FUR)

def buy_64_NC():
    game.buy_upgrade(u64_NC)

def buy_65_FF():
    game.buy_upgrade(u65_FF)

def buy_66_BT():
    game.buy_upgrade(u66_BT)

def buy_67_VC():
    game.buy_upgrade(u67_VC)

def buy_68_AD():
    game.buy_upgrade(u68_AD)

def buy_69_DI():
    game.buy_upgrade(u69_DI)

def buy_70_IMM():
    game.buy_upgrade(u70_IMM)

def buy_71_CD():
    game.buy_upgrade(u71_CD)

def buy_72_CD():
    game.buy_upgrade(u72_CD)

def buy_73_CS():
    game.buy_upgrade(u73_CS)

def buy_74_SD():
    game.buy_upgrade(u74_SD)

def buy_75_ER():
    game.buy_upgrade(u75_ER)

def buy_76_OT():
    game.buy_upgrade(u76_OT)

def buy_77_IBS():
    game.buy_upgrade(u77_IBS)

def buy_78_SC():
    game.buy_upgrade(u78_SC)

def buy_79_TU():
    game.buy_upgrade(u79_TU)

def buy_80_HS():
    game.buy_upgrade(u80_HS)























# Increasing Automators
def increase_a1_GC():
    temp = 0
    while a1_GC.afford(game) and temp < 5:
        a1_GC.increase(game)
        global a1_GC_Name
        global compressor_costs
        a1_GC_Name.config(a1_GC_Name, text = "Compressors: " + format_number(a1_GC.count, 0))
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
        a2_QS_Name.config(a2_QS_Name, text = "Quark Synthesizers: " + format_number(a2_QS.count, 0))
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
        a3_PS_Name.config(a3_PS_Name, text = "Proton Synthesizers: " + format_number(a3_PS.count, 0))
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
        a4_NS_Name.config(a4_NS_Name, text = "Neutron Synthesizers: " + format_number(a4_NS.count, 0))
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
        a5_HyF_Name.config(a5_HyF_Name, text = "Hydrogen Fabricator: " + format_number(a5_HyF.count, 0))
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
        a6_HeF_Name.config(a6_HeF_Name, text = "Helium Fabricator: " + format_number(a6_HeF.count, 0))
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
        a7_NF_Name.config(a7_NF_Name, text = "Nuclear Fusion: " + format_number(a7_NF.count, 0))
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

def increase_a8_NS():
    temp = 0
    while a8_NS.afford(game) and temp < 5:
        a8_NS.increase(game)
        global a8_NS_Name
        global a8_NS_Cost
        global a8_NS_Button
        global a8_NS_Toggle
        a8_NS_Name.config(a8_NS_Name, text = "Nutrient Synthesis: " + format_number(a8_NS.count, 0))
        a8_NS_Cost.config(a8_NS_Cost, text = a8_NS.showCost())
        productionF.update_idletasks()
        a8_NS_Button.place(x = (a8_NS_Name.winfo_width() + LPADDING))
        a8_NS_Toggle.place(x = (a8_NS_Name.winfo_width() + a8_NS_Button.winfo_width() + LPADDING + SPADDING))
        temp += 1

def increase_a9_HS():
    temp = 0
    while a9_HS.afford(game) and temp < 5:
        a9_HS.increase(game)
        global a9_HS_Name
        global a9_HS_Cost
        global a9_HS_Button
        global a9_HS_Toggle
        a9_HS_Name.config(a9_HS_Name, text = "Hydro Synthesis: " + format_number(a9_HS.count, 0))
        a9_HS_Cost.config(a9_HS_Cost, text = a9_HS.showCost())
        productionF.update_idletasks()
        a9_HS_Button.place(x = (a9_HS_Name.winfo_width() + LPADDING))
        a9_HS_Toggle.place(x = (a9_HS_Name.winfo_width() + a9_HS_Button.winfo_width() + LPADDING + SPADDING))
        temp += 1

def increase_a10_DNA():
    temp = 0
    while a10_DNA.afford(game) and temp < 5:
        a10_DNA.increase(game)
        global a10_DNA_Name
        global compressor_costs
        a10_DNA_Name.config(a10_DNA_Name, text = "DNA Manufacturers: " + format_number(a10_DNA.count, 0))
        a10_DNA_Cost.config(a10_DNA_Cost, text = a10_DNA.showCost())
        productionF.update_idletasks()
        a10_DNA_Button.place(x = (a10_DNA_Name.winfo_width() + LPADDING))
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

def toggle_a8_NS():
    global a8_NS_Toggle
    if (a8_NS.toggle == 1):
        a8_NS.toggle = 0
        a8_NS_Toggle.config(a8_NS_Toggle, text = "OFF")
    else:
        a8_NS.toggle = 1
        a8_NS_Toggle.config(a8_NS_Toggle, text = "ON")

def toggle_a9_HS():
    global a9_HS_Toggle
    if (a9_HS.toggle == 1):
        a9_HS.toggle = 0
        a9_HS_Toggle.config(a9_HS_Toggle, text = "OFF")
    else:
        a9_HS.toggle = 1
        a9_HS_Toggle.config(a9_HS_Toggle, text = "ON")





































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
        # active_autos.append(a1_GC)

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

        potentialLab = Label(temporalF, text = "Potential: " + format_number(game.maxpotential, 0), font = ("Terminal", 10), bg = "white")
        potentialLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialLab.winfo_height()

        potentialDescLab = Label(temporalF, text = "+1 Potential at " + format_number(game.potential_lifeforms_req, 0) + " lifeforms", font = ("Terminal", 8), bg = "white")
        potentialDescLab.place(x = PADDING, y = label_height + PADDING)
        temporalF.update_idletasks()
        label_height = label_height + potentialDescLab.winfo_height() + LPADDING

        productivityBut = tk.Button(temporalF, text = "Productivity", font = ("Terminal", 9), width = 13, command = buy_Productivity, state = DISABLED)
        productivityBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        productivityLab = Label(temporalF, text = format_number(game.productivity, 0), font = ("Terminal", 9), bg = "white")
        productivityLab.place(x = productivityBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + productivityBut.winfo_height() + SPADDING

        temporalF.update_idletasks()
        expansionBut = tk.Button(temporalF, text = "Expansion", font = ("Terminal", 9), width = 13, command = buy_Expansion, state = DISABLED)
        expansionBut.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        
        expansionLab = Label(temporalF, text = format_number(game.expansion, 0), font = ("Terminal", 9), bg = "white")
        expansionLab.place(x = expansionBut.winfo_width() + LPADDING, y = label_height + LPADDING)
        label_height = label_height + expansionBut.winfo_height() + LPADDING

        respecBut = tk.Button(temporalF, text = "Respec", font = ("Terminal", 8), width = 8, command = respec_temporal, state = DISABLED)
        respecBut.place(x = PADDING, y = label_height + SPADDING)
        label_height = label_height + respecBut.winfo_height() + LPADDING

        timeLab = Label(temporalF, text = "Time: " + format_number(game.time, 0) + " / " + format_number(game.expansion * 1000, 0), font = ("Terminal", 10), bg = "white")
        timeLab.place(x = PADDING, y = label_height + LPADDING)
        temporalF.update_idletasks()
        label_height = label_height + timeLab.winfo_height() + SPADDING

        innovationLab = Label(temporalF, text = "Innovation: " + format_number(game.innovation, 0), font = ("Terminal", 10), bg = "white")
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

    global microbeLab
    if (game.microbes > 0 and u26_DNA.active == 2 and microbeLab == None): 
        microbeLab = createSpeciesLabel(microbeLab, game.microbes, "Microbes")
    
    # Potential upgrade from milestones
    if (game.lifeforms >= game.potential_lifeforms_req):
        game.potential_lifeforms_req *= 10
        game.potential += 1
        game.set_max_potential()
        productivityBut.config(productivityBut, state = ACTIVE)
        expansionBut.config(expansionBut, state = ACTIVE)
    
    # Unlocking upgrades after getting mcirobes
    if (game.microbes >= 10 and u41_DF.active == 0):
        global u41_DF_Button
        global u27_GM_Button
        global u28_MA_Button
        global u29_AR_Button
        global u30_MC_Button
        global u31_MP_Button
        u27_GM_Button = createUpgradeButton(u27_GM_Button, u27_GM, buy_27_GM)
        u29_AR_Button = createUpgradeButton(u29_AR_Button, u29_AR, buy_29_AR)
        u30_MC_Button = createUpgradeButton(u30_MC_Button, u30_MC, buy_30_MC)
        u28_MA_Button = createUpgradeButton(u28_MA_Button, u28_MA, buy_28_MA)
        u31_MP_Button = createUpgradeButton(u31_MP_Button, u31_MP, buy_31_MP)
        u41_DF_Button = createUpgradeButton(u41_DF_Button, u41_DF, buy_41_DF)

    root.after(100, check_milestones)

































































# Function for adding a new resource to resources frame
def createResourceLabel(label, resource, name):
    global RESOURCE_FRAME_HEIGHT
    global RESOURCE_LABEL_NEXTY
    global PRODUCTION_FRAME_TOP
    label = Label(resourcesF, text = name + ": " + format_number(resource, 0), font = ('Terminal', 10), bg = "white")
    label.place(x = PADDING, y = RESOURCE_LABEL_NEXTY, anchor=('nw'))
    # label.place_configure(anchor='n')
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
    label_y = label.winfo_y()
    label_height = label.winfo_height()
    label.destroy()

    for widget in resourcesF.winfo_children():
        current_y = widget.winfo_y()
        if current_y >= label_y:
            widget.place(y=current_y - label_height - LPADDING)
    
    RESOURCE_FRAME_HEIGHT = RESOURCE_FRAME_HEIGHT - label_height - PADDING
    RESOURCE_LABEL_NEXTY = RESOURCE_LABEL_NEXTY - label_height - PADDING
    PRODUCTION_FRAME_TOP = PRODUCTION_FRAME_TOP - label_height - PADDING
    resourcesF.config(height=RESOURCE_FRAME_HEIGHT)

    if (productionF != None):
        productionF.place(y = PRODUCTION_FRAME_TOP)
    
    return None

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

    namelabel = Label(productionF, text = name + ": " + format_number(automator.count, 0), font = ('Terminal', 10), bg = "white")
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


# Function for adding a new resource to resources frame
def createSpeciesLabel(label, lifeform, name):
    global SPECIES_FRAME_HEIGHT
    global SPECIES_LABEL_NEXTY
    label = Label(speciesF, text = name + ": " + format_number(lifeform, 0) + "\n + " + format_number(lifeform, 2), font = ('Terminal', 10), bg = "white")
    label.place(x = PADDING, y = SPECIES_LABEL_NEXTY, anchor=('nw'))
    # label.place_configure(anchor='n')
    speciesF.update_idletasks()
    label_height = label.winfo_height()
    SPECIES_FRAME_HEIGHT = SPECIES_FRAME_HEIGHT + label_height + PADDING
    SPECIES_LABEL_NEXTY = SPECIES_LABEL_NEXTY + label_height + PADDING
    speciesF.config(height=SPECIES_FRAME_HEIGHT)

    return label

# Function for destroying a button within upgrades frame
def destroySpeciesLabel(label):
    global SPECIES_FRAME_HEIGHT
    global SPECIES_LABEL_NEXTY
    label_y = label.winfo_y()
    label_height = label.winfo_height()
    label.destroy()

    for widget in speciesF.winfo_children():
        current_y = widget.winfo_y()
        if current_y >= label_y:
            widget.place(y=current_y - label_height - LPADDING)
    
    SPECIES_FRAME_HEIGHT = SPECIES_FRAME_HEIGHT - label_height - PADDING
    SPECIES_LABEL_NEXTY = SPECIES_LABEL_NEXTY - label_height - PADDING
    speciesF.config(height=SPECIES_FRAME_HEIGHT)
    
    return None
































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

    if u30_MC.active == 1:
        if u30_MC.afford(game):
            u30_MC_Button.config(u30_MC_Button, state = ACTIVE)
        else:
            u30_MC_Button.config(u30_MC_Button, state = DISABLED)

    if u31_MP.active == 1:
        if u31_MP.afford(game):
            u31_MP_Button.config(u31_MP_Button, state = ACTIVE)
        else:
            u31_MP_Button.config(u31_MP_Button, state = DISABLED)

    if u32_PS.active == 1:
        if u32_PS.afford(game):
            u32_PS_Button.config(u32_PS_Button, state = ACTIVE)
        else:
            u32_PS_Button.config(u32_PS_Button, state = DISABLED)

    if u33_AM.active == 1:
        if u33_AM.afford(game):
            u33_AM_Button.config(u33_AM_Button, state = ACTIVE)
        else:
            u33_AM_Button.config(u33_AM_Button, state = DISABLED)

    if u34_DA.active == 1:
        if u34_DA.afford(game):
            u34_DA_Button.config(u34_DA_Button, state = ACTIVE)
        else:
            u34_DA_Button.config(u34_DA_Button, state = DISABLED)

    if u35_FL.active == 1:
        if u35_FL.afford(game):
            u35_FL_Button.config(u35_FL_Button, state = ACTIVE)
        else:
            u35_FL_Button.config(u35_FL_Button, state = DISABLED)

    if u36_CP.active == 1:
        if u36_CP.afford(game):
            u36_CP_Button.config(u36_CP_Button, state = ACTIVE)
        else:
            u36_CP_Button.config(u36_CP_Button, state = DISABLED)

    if u37_MC.active == 1:
        if u37_MC.afford(game):
            u37_MC_Button.config(u37_MC_Button, state = ACTIVE)
        else:
            u37_MC_Button.config(u37_MC_Button, state = DISABLED)

    if u38_BP.active == 1:
        if u38_BP.afford(game):
            u38_BP_Button.config(u38_BP_Button, state = ACTIVE)
        else:
            u38_BP_Button.config(u38_BP_Button, state = DISABLED)

    if u39_CS.active == 1:
        if u39_CS.afford(game):
            u39_CS_Button.config(u39_CS_Button, state = ACTIVE)
        else:
            u39_CS_Button.config(u39_CS_Button, state = DISABLED)

    if u40_OX.active == 1:
        if u40_OX.afford(game):
            u40_OX_Button.config(u40_OX_Button, state = ACTIVE)
        else:
            u40_OX_Button.config(u40_OX_Button, state = DISABLED)

    if u41_DF.active == 1:
        if u41_DF.afford(game):
            u41_DF_Button.config(u41_DF_Button, state = ACTIVE)
        else:
            u41_DF_Button.config(u41_DF_Button, state = DISABLED)

    if u42_SY.active == 1:
        if u42_SY.afford(game):
            u42_SY_Button.config(u42_SY_Button, state = ACTIVE)
        else:
            u42_SY_Button.config(u42_SY_Button, state = DISABLED)

    if u43_DT.active == 1:
        if u43_DT.afford(game):
            u43_DT_Button.config(u43_DT_Button, state = ACTIVE)
        else:
            u43_DT_Button.config(u43_DT_Button, state = DISABLED)

    if u44_AB.active == 1:
        if u44_AB.afford(game):
            u44_AB_Button.config(u44_AB_Button, state = ACTIVE)
        else:
            u44_AB_Button.config(u44_AB_Button, state = DISABLED)

    if u45_MT.active == 1:
        if u45_MT.afford(game):
            u45_MT_Button.config(u45_MT_Button, state = ACTIVE)
        else:
            u45_MT_Button.config(u45_MT_Button, state = DISABLED)

    if u46_OL.active == 1:
        if u46_OL.afford(game):
            u46_OL_Button.config(u46_OL_Button, state = ACTIVE)
        else:
            u46_OL_Button.config(u46_OL_Button, state = DISABLED)

    if u47_ES.active == 1:
        if u47_ES.afford(game):
            u47_ES_Button.config(u47_ES_Button, state = ACTIVE)
        else:
            u47_ES_Button.config(u47_ES_Button, state = DISABLED)

    if u48_NS.active == 1:
        if u48_NS.afford(game):
            u48_NS_Button.config(u48_NS_Button, state = ACTIVE)
        else:
            u48_NS_Button.config(u48_NS_Button, state = DISABLED)

    if u49_ES.active == 1:
        if u49_ES.afford(game):
            u49_ES_Button.config(u49_ES_Button, state = ACTIVE)
        else:
            u49_ES_Button.config(u49_ES_Button, state = DISABLED)

    if u50_SB.active == 1:
        if u50_SB.afford(game):
            u50_SB_Button.config(u50_SB_Button, state = ACTIVE)
        else:
            u50_SB_Button.config(u50_SB_Button, state = DISABLED)

    if u51_EX.active == 1:
        if u51_EX.afford(game):
            u51_EX_Button.config(u51_EX_Button, state = ACTIVE)
        else:
            u51_EX_Button.config(u51_EX_Button, state = DISABLED)

    if u52_MM.active == 1:
        if u52_MM.afford(game):
            u52_MM_Button.config(u52_MM_Button, state = ACTIVE)
        else:
            u52_MM_Button.config(u52_MM_Button, state = DISABLED)

    if u53_IW.active == 1:
        if u53_IW.afford(game):
            u53_IW_Button.config(u53_IW_Button, state = ACTIVE)
        else:
            u53_IW_Button.config(u53_IW_Button, state = DISABLED)

    if u54_OP.active == 1:
        if u54_OP.afford(game):
            u54_OP_Button.config(u54_OP_Button, state = ACTIVE)
        else:
            u54_OP_Button.config(u54_OP_Button, state = DISABLED)

    if u55_LL.active == 1:
        if u55_LL.afford(game):
            u55_LL_Button.config(u55_LL_Button, state = ACTIVE)
        else:
            u55_LL_Button.config(u55_LL_Button, state = DISABLED)

    if u56_IF.active == 1:
        if u56_IF.afford(game):
            u56_IF_Button.config(u56_IF_Button, state = ACTIVE)
        else:
            u56_IF_Button.config(u56_IF_Button, state = DISABLED)

    if u57_TP.active == 1:
        if u57_TP.afford(game):
            u57_TP_Button.config(u57_TP_Button, state = ACTIVE)
        else:
            u57_TP_Button.config(u57_TP_Button, state = DISABLED)

    if u58_ET.active == 1:
        if u58_ET.afford(game):
            u58_ET_Button.config(u58_ET_Button, state = ACTIVE)
        else:
            u58_ET_Button.config(u58_ET_Button, state = DISABLED)

    if u59_RS.active == 1:
        if u59_RS.afford(game):
            u59_RS_Button.config(u59_RS_Button, state = ACTIVE)
        else:
            u59_RS_Button.config(u59_RS_Button, state = DISABLED)

    if u60_EC.active == 1:
        if u60_EC.afford(game):
            u60_EC_Button.config(u60_EC_Button, state = ACTIVE)
        else:
            u60_EC_Button.config(u60_EC_Button, state = DISABLED)

    if u61_DH.active == 1:
        if u61_DH.afford(game):
            u61_DH_Button.config(u61_DH_Button, state = ACTIVE)
        else:
            u61_DH_Button.config(u61_DH_Button, state = DISABLED)

    if u62_MG.active == 1:
        if u62_MG.afford(game):
            u62_MG_Button.config(u62_MG_Button, state = ACTIVE)
        else:
            u62_MG_Button.config(u62_MG_Button, state = DISABLED)

    if u63_FUR.active == 1:
        if u63_FUR.afford(game):
            u63_FUR_Button.config(u63_FUR_Button, state = ACTIVE)
        else:
            u63_FUR_Button.config(u63_FUR_Button, state = DISABLED)
    
    if u64_NC.active == 1:
        if u64_NC.afford(game):
            u64_NC_Button.config(u64_NC_Button, state = ACTIVE)
        else:
            u64_NC_Button.config(u64_NC_Button, state = DISABLED)

    if u65_FF.active == 1:
        if u65_FF.afford(game):
            u65_FF_Button.config(u65_FF_Button, state = ACTIVE)
        else:
            u65_FF_Button.config(u65_FF_Button, state = DISABLED)

    if u66_BT.active == 1:
        if u66_BT.afford(game):
            u66_BT_Button.config(u66_BT_Button, state = ACTIVE)
        else:
            u66_BT_Button.config(u66_BT_Button, state = DISABLED)

    if u67_VC.active == 1:
        if u67_VC.afford(game):
            u67_VC_Button.config(u67_VC_Button, state = ACTIVE)
        else:
            u67_VC_Button.config(u67_VC_Button, state = DISABLED)

    if u68_AD.active == 1:
        if u68_AD.afford(game):
            u68_AD_Button.config(u68_AD_Button, state = ACTIVE)
        else:
            u68_AD_Button.config(u68_AD_Button, state = DISABLED)

    if u69_DI.active == 1:
        if u69_DI.afford(game):
            u69_DI_Button.config(u69_DI_Button, state = ACTIVE)
        else:
            u69_DI_Button.config(u69_DI_Button, state = DISABLED)

    if u70_IMM.active == 1:
        if u70_IMM.afford(game):
            u70_IMM_Button.config(u70_IMM_Button, state = ACTIVE)
        else:
            u70_IMM_Button.config(u70_IMM_Button, state = DISABLED)

    if u71_CD.active == 1:
        if u71_CD.afford(game):
            u71_CD_Button.config(u71_CD_Button, state = ACTIVE)
        else:
            u71_CD_Button.config(u71_CD_Button, state = DISABLED)

    if u72_CD.active == 1:
        if u72_CD.afford(game):
            u72_CD_Button.config(u72_CD_Button, state = ACTIVE)
        else:
            u72_CD_Button.config(u72_CD_Button, state = DISABLED)

    if u73_CS.active == 1:
        if u73_CS.afford(game):
            u73_CS_Button.config(u73_CS_Button, state = ACTIVE)
        else:
            u73_CS_Button.config(u73_CS_Button, state = DISABLED)

    if u74_SD.active == 1:
        if u74_SD.afford(game):
            u74_SD_Button.config(u74_SD_Button, state = ACTIVE)
        else:
            u74_SD_Button.config(u74_SD_Button, state = DISABLED)

    if u75_ER.active == 1:
        if u75_ER.afford(game):
            u75_ER_Button.config(u75_ER_Button, state = ACTIVE)
        else:
            u75_ER_Button.config(u75_ER_Button, state = DISABLED)

    if u76_OT.active == 1:
        if u76_OT.afford(game):
            u76_OT_Button.config(u76_OT_Button, state = ACTIVE)
        else:
            u76_OT_Button.config(u76_OT_Button, state = DISABLED)

    if u77_IBS.active == 1:
        if u77_IBS.afford(game):
            u77_IBS_Button.config(u77_IBS_Button, state = ACTIVE)
        else:
            u77_IBS_Button.config(u77_IBS_Button, state = DISABLED)

    if u78_SC.active == 1:
        if u78_SC.afford(game):
            u78_SC_Button.config(u78_SC_Button, state = ACTIVE)
        else:
            u78_SC_Button.config(u78_SC_Button, state = DISABLED)

    if u79_TU.active == 1:
        if u79_TU.afford(game):
            u79_TU_Button.config(u79_TU_Button, state = ACTIVE)
        else:
            u79_TU_Button.config(u79_TU_Button, state = DISABLED)

    if u80_HS.active == 1:
        if u80_HS.afford(game):
            u80_HS_Button.config(u80_HS_Button, state = ACTIVE)
        else:
            u80_HS_Button.config(u80_HS_Button, state = DISABLED)


    root.after(100, afford_upgrades)

#Function that constantly updates game Labels
def update_labels():
    game = Game() # get the instance of the game class
    if game.resourcesFrame == True:
        global energyLab
        global quarkLab
        global protonLab
        global neutronLab
        global hydrogenLab
        global heliumLab
        global dnaLab
        global waterLab
        global nutrientsLab
        global microbeLab
        global lifeL
        try:
            if (energyLab):
                energyLab.config(energyLab, text = "Energy: " + format_number(game.energy, 0))
                # energyLab.config(energyLab, text = "Energy: " + format_number(game.energy))
            if (quarkLab):
                quarkLab.config(quarkLab, text = "Quarks: " + format_number(game.quarks, 0))
            if (protonLab):
                protonLab.config(protonLab, text = "Protons: " + format_number(game.protons, 0))
            if (neutronLab):
                neutronLab.config(neutronLab, text = "Neutrons: " + format_number(game.neutrons, 0))
            if (hydrogenLab):
                hydrogenLab.config(hydrogenLab, text = "Hydrogen: " + format_number(game.hydrogen, 0))
            if (heliumLab):
                heliumLab.config(heliumLab, text = "Helium: " + format_number(game.helium, 0))
            if (dnaLab):
                dnaLab.config(dnaLab, text = "DNA: " + format_number(game.dna, 0))
            if (nutrientLab):
                nutrientLab.config(nutrientLab, text = "Nutrients: " + format_number(game.nutrients, 0))
            if (waterLab):
                waterLab.config(waterLab, text = "Water: " + format_number(game.water, 0))
            if (microbeLab):
                microbeLab.config(microbeLab, text = "Microbes: " + format_number(game.microbes, 0) + "\n+ " + format_number(game.microbes * game.repro_microbes, 2) + " per tick")
            if (algaeLab):
                algaeLab.config(algaeLab, text = "Algae: " + format_number(game.algae, 0) + "\n+ " + format_number(game.algae * game.repro_algae, 2) + " per tick")
            if (game.lifeforms > 0):
                lifeL.config(lifeL, text = "Lifeforms: " + "{:,.0f}".format(game.lifeforms))
        except:
            None
    if game.temporalFrame == True:
        global timeLab
        global innovationLab
        potentialLab.config(potentialLab, text = "Potential: " + format_number(game.maxpotential, 0))
        potentialDescLab.config(potentialDescLab, text = "+1 Potential at " + format_number(game.potential_lifeforms_req, 0) + " lifeforms")
        timeLab.config(timeLab, text = "Time: " + format_number(game.time, 0) + " / " + format_number(game.expansion * 1000, 0))
        innovationLab.config(innovationLab, text = "Innovation: " + format_number(game.innovation, 0))

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