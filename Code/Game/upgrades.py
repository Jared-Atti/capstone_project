def format_number(number, decimal):
    if number < 1000000000:
        return f"{number:,.{decimal}f}"
    if number < 1000000000000:
        number /= pow(10, 9)
        return f"{number:,.{3}f} Billion"
    if number < 1000000000000000:
        number /= pow(10, 12)
        return f"{number:,.{3}f} Trillion"
    if number < 1000000000000000000:
        number /= pow(10, 15)
        return f"{number:,.{3}f} Quadrillion"
    if number < 1000000000000000000000:
        number /= pow(10, 18)
        return f"{number:,.{3}f} Quintillion"
    if number < 1000000000000000000000000:
        number /= pow(10, 21)
        return f"{number:,.{3}f} Sextillion"
    if number < 100000000000000000000000000:
        number /= pow(10, 24)
        return f"{number:,.{3}f} Septillion"

class Upgrade():
    def __init__(self, name, costs, description):
        self.name = name
        self.costs = costs
        self.description = description
        self.active = 0 # 0 = Not yet unlocked, 1 = Unlocked but not purchased, 2 = Purchased
    
    def showCosts(self):
        coststr = "("
        for i in range(len(self.costs)):
            if i < len(self.costs) - 1:
                coststr += str(format_number(self.costs[i][1], 0)) + " " + str(self.costs[i][0]) + ", "
            else:
                coststr += str(format_number(self.costs[i][1], 0)) + " " + str(self.costs[i][0])
        return coststr + ")"

# Cosmic Upgrades
class GravitationalCompression(Upgrade):
    def __init__(self):
        super().__init__("Gravitational Compression ", [("Energy", 15)], "Siphon energy from space dust collapsing under its own gravity. Unlocks production menu.")
    
    def afford(self, game):
        if game.energy >= 15:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 15
            game.purchasedupgrades += self.name
            self.active = 2

class SubatomicSynthesis(Upgrade):
    def __init__(self):
        super().__init__("Subatomic Synthesis ", [("Energy", 75)], "Smash particles together and convert the energy into quarks.")

    def afford(self, game):
        if game.energy >= 75:
            return True

    def purchase(self, game):
        if self.afford(game):
            game.energy -= 75
            game.purchasedupgrades += self.name
            self.active = 2

class Temporal(Upgrade):
    def __init__(self):
        super().__init__("Temporal Momentum ", [("Energy", 75)], "By harnessing the power of cosmic forces, you have unlocked the ability to manipulate time and expand the fabric of space itself.")
    
    def afford(self, game):
        if game.energy >= 75:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 75
            game.timeFlag = True
            game.purchasedupgrades += self.name
            self.active = 2

class Innovation(Upgrade):
    def __init__(self):
        super().__init__("Innovation ", [("Time", 500)], "Take your progress to the next level with Innovation. Use your full time to generate innovation and advance even faster!")

    def afford(self, game):
        if game.time >= 500:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 500
            game.innovationFlag = True
            game.purchasedupgrades += self.name
            self.active = 2

class Nucleosynthesis(Upgrade):
    def __init__(self):
        super().__init__("Nucleosynthesis ", [("Quarks", 100), ("Innovation", 20)], "Combine quarks and innovation to unlock the ability to create protons and neutrons through the magic of nucleosynthesis!")

    def afford(self, game):
        if game.quarks >= 100 and game.innovation >= 20:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.quarks -= 100
            game.innovation -= 20
            game.purchasedupgrades += self.name
            self.active = 2

class Gravitational_Amplification(Upgrade):
    def __init__(self):
        super().__init__("Gravitational Amplification ", [("Energy", 1000), ("Time", 2000)], "Amplify the gravitational force to increase energy production efficiency.")

    def afford(self, game):
        if game.energy >= 1000 and game.time >= 2000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.energy -= 1000
            game.time -= 2000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 5)
            return autos[0]

class Quark_Fusion(Upgrade):
    def __init__(self):
        super().__init__("Quark Fusion ", [("Time", 1000), ("Energy", 1500)], "Master the art of quark fusion to improve your efficiency and cut your quark costs in half!")

    def afford(self, game):
        if game.time >= 1000 and game.energy >= 1500:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.energy -= 1500
            game.time -= 1000
            game.purchasedupgrades += self.name
            self.active = 2
            newcost = [(autos[0].tickcost[0][0], autos[0].tickcost[0][1] / 2)]
            newrev = (autos[0].revenue[0], autos[0].revenue[1] * 5)
            autos[0].tickcost = newcost
            autos[0].revenue = newrev
            return autos[0]

class Atomic_Fabrication(Upgrade):
    def __init__(self):
        super().__init__("Atomic Fabrication ", [("Quarks", 750), ("Energy", 2000)], "Unleash the Power of Atomic Fabrication to Produce Hydrogen!")

    def afford(self, game):
        if  game.quarks >= 750 and game.energy >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 2000
            game.quarks -= 750
            game.purchasedupgrades += self.name
            self.active = 2

class Discover_Helium(Upgrade):
    def __init__(self):
        super().__init__("Discover Helium ", [("Time", 2000), ("Quarks", 3000), ("Energy", 5000)], "Take your atomic knowledge to new heights with helium!")

    def afford(self, game):
        if game.time >= 2000 and game.quarks >= 3000 and game.energy >= 5000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 5000
            game.time -= 2000
            game.quarks -= 3000
            game.purchasedupgrades += self.name
            self.active = 2

class Cosmic_Burst(Upgrade):
    def __init__(self):
        super().__init__("Cosmic Burst ", [("Innovation", 25)], "+1 Potential")

    def afford(self, game):
        if game.innovation >= 25:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.innovation -= 25
            game.purchasedupgrades += self.name
            game.potential += 1
            game.maxpotential += 1
            self.active = 2

class Starlight_Path(Upgrade):
    def __init__(self):
        super().__init__("Starlight Path ", [("Innovation", 50)], "+1 Potential")

    def afford(self, game):
        if game.innovation >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.innovation -= 50
            game.purchasedupgrades += self.name
            game.potential += 1
            game.maxpotential += 1
            self.active = 2

class Quantum_Leap(Upgrade):
    def __init__(self):
        super().__init__("Quantum Leap ", [("Innovation", 200)], "+5 Potential")

    def afford(self, game):
        if game.innovation >= 200:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.innovation -= 200
            game.purchasedupgrades += self.name
            game.potential += 5
            game.maxpotential += 5
            self.active = 2

class Galatic_Investment(Upgrade):
    def __init__(self):
        super().__init__("Galatic Investment ", [("Innovation", 400)], "+5 Potential")

    def afford(self, game):
        if game.innovation >= 400:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.innovation -= 400
            game.purchasedupgrades += self.name
            game.potential += 5
            game.maxpotential += 5
            self.active = 2

class Nova_Catalyst(Upgrade):
    def __init__(self):
        super().__init__("Nova Catalyst ", [("Innovation", 500)], "+10 Potential")

    def afford(self, game):
        if game.innovation >= 500:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.innovation -= 500
            game.purchasedupgrades += self.name
            game.potential += 10
            game.maxpotential += 10
            self.active = 2

class Gravitational_Flucuations(Upgrade):
    def __init__(self):
        super().__init__("Gravitational Flucuations ", [("Energy", 5000), ("Innovation", 100)], "Amplify the gravitational force to increase energy production efficiency.")

    def afford(self, game):
        if game.innovation >= 100 and game.energy >= 5000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.innovation -= 100
            game.energy -= 5000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 50)
            return autos[0]

class Quark_Acceleration(Upgrade):
    def __init__(self):
        super().__init__("Quark Acceleration ", [("Energy", 20000), ("Quarks", 5000)], "Accelerating the rate of production of quarks greatly while also cutting costs in half.")

    def afford(self, game):
        if game.quarks >= 5000 and game.energy >= 20000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.quarks -= 5000
            game.energy -= 20000
            game.purchasedupgrades += self.name
            self.active = 2
            newcost = [(autos[0].tickcost[0][0], autos[0].tickcost[0][1] / 2)]
            newrev = (autos[0].revenue[0], autos[0].revenue[1] * 50)
            autos[0].tickcost = newcost
            autos[0].revenue = newrev
            return autos[0]


class Proton_Processor(Upgrade):
    def __init__(self):
        super().__init__("Proton Processor ", [("Quarks", 50000), ("Energy", 10000)], "Learn how to automate the production of Protons.")

    def afford(self, game):
        if game.quarks >= 50000 and game.energy >= 10000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.quarks -= 50000
            game.energy -= 10000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 100)
            return autos[0]

class Neutron_Processor(Upgrade):
    def __init__(self):
        super().__init__("Nuetron Processor ", [("Quarks", 75000), ("Energy", 15000)], "Expand your knowledge to automate the production of Neutrons.")

    def afford(self, game):
        if game.quarks >= 75000 and game.energy >= 15000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.quarks -= 75000
            game.energy -= 15000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 100)
            return autos[0]

class Hydrogenic_Catalyst(Upgrade):
    def __init__(self):
        super().__init__("Hydrogenic Catalyst ", [("Protons", 20000), ("Neutrons", 20000)], "With the automation of protons and neutrons, you can now automate Hydrogen.")

    def afford(self, game):
        if game.neutrons >= 20000 and game.protons >= 20000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.protons -= 20000
            game.neutrons -= 20000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 2000)
            return autos[0]

class Helium_Extractor(Upgrade):
    def __init__(self):
        super().__init__("Helium Extractor ", [("Protons", 30000), ("Neutrons", 30000)], "Finally mastering the power to automate the production of Helium")

    def afford(self, game):
        if game.neutrons >= 30000 and game.protons >= 30000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.protons -= 30000
            game.neutrons -= 30000
            game.purchasedupgrades += self.name
            self.active = 2
            autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 2000)
            return autos[0]

class Create_Sun(Upgrade):
    def __init__(self):
        super().__init__("Create the Sun ", [("Time", 3000), ("Hydrogen", 12400000000), ("Helium", 5310000000)], "With all the resources created and utomated, you can now harness the power of the Sun.")

    def afford(self, game):
        if game.time >= 3000 and game.hydrogen >= 12400000000 and game.helium >= 5310000000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 3000
            game.hydrogen -= 12400000000
            game.helium -= 5310000000
            game.purchasedupgrades += self.name
            self.active = 2

class Nuclear_Fusion(Upgrade):
    def __init__(self):
        super().__init__("Nuclear Fusion ", [("Time", 3000), ("Innovation", 100), ("Hydrogen", 2000), ("Helium", 2000)], "TBD")

    def afford(self, game):
        if game.time >= 3000 and game.innovation >= 100 and game.hydrogen >= 2000 and game.helium >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 3000
            game.innovation -= 100
            game.hydrogen -= 2000
            game.helium -= 2000
            game.purchasedupgrades += self.name
            self.active = 2

class Create_Earth(Upgrade):
    def __init__(self):
        super().__init__("Create the Earth ", [("Time", 4000), ("Hydrogen", 560000000), ("Helium", 23400000), ("Innovation", 100)], "Finally with everything you've gathered, you create a life sustaining planet you call Earth and travel to it..")

    def afford(self, game):
        if game.time >= 4000 and game.innovation >= 100 and game.hydrogen >= 560000000 and game.helium >= 23400000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 4000
            game.innovation -= 100
            game.hydrogen -= 560000000
            game.helium -= 23400000
            game.purchasedupgrades += self.name
            self.active = 2

class Nuclear_Fusion_Increase(Upgrade):
    def __init__(self):
        super().__init__("Nuclear Fusion Increase ", None, None)
    
    def purchase(self, game, autos):
        autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 1.20)
        autos[1].revenue = (autos[1].revenue[0], autos[1].revenue[1] * 1.20)
        autos[2].revenue = (autos[2].revenue[0], autos[2].revenue[1] * 1.20)
        autos[3].revenue = (autos[3].revenue[0], autos[3].revenue[1] * 1.20)
        autos[4].revenue = (autos[4].revenue[0], autos[4].revenue[1] * 1.20)
        autos[5].revenue = (autos[5].revenue[0], autos[5].revenue[1] * 1.20)
        return autos

class Cool_Down(Upgrade):
    def __init__(self):
        super().__init__("Cool Down ", [("Time", 100)], "The Earth is still forming and a very hot molten ball of rock. It needs some time be cool. In the meantime, it can be bombarded with asteroids and collect some interesting materials, maybe even a moon.")

    def afford(self, game):
        if game.time >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 100
            game.purchasedupgrades += self.name
            self.active = 2

# Precambrian Upgrades
class Create_Life(Upgrade):
    def __init__(self):
        super().__init__("Create Life ", [("Time", 10)], "Sacrifice everything you have gathered throughout the Cosmic era to discover a new material called DNA.")

    def afford(self, game):
        if game.time >= 10:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 10
            game.purchasedupgrades += self.name
            self.active = 2

class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation ", [("Time", 1000)], "Generates passive DNA points for every living microbe.")
    
    def afford(self, game):
        if game.time >= 1000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 1000
            game.purchasedupgrades += self.name
            self.active = 2
            game.mutationflag = 1

class Metabolic_Adaptation(Upgrade):
    def __init__(self):
        super().__init__("Metabolic Adaptation ", [("DNA", 200), ("Time", 2000)], "Unlocks the ability to metabolize water as a resource, allowing for greater growth and expansion of your life forms. Unlocks water.")
    
    def afford(self, game):
        if game.dna >= 200 and game.time >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 200
            game.time -= 2000
            game.purchasedupgrades += self.name
            self.active = 2

class Asexual_Reproduction(Upgrade):
    def __init__(self):
        super().__init__("Asexual Reproduction ", [("DNA", 3)], "Microbes begin evolving, learning the ability to reproduce asexually.  Reproducers begin increasing the amount of microbes.")
    
    def afford(self, game):
        if game.dna >= 3:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 3
            game.purchasedupgrades += self.name
            game.repro_microbes = 0.001
            self.active = 2

class Multicellularity(Upgrade):
    def __init__(self):
        super().__init__("Multicellularity ", [("DNA", 100), ("Time", 1000)], "Your organisms will form multicellular structures, allowing for greater specialization and complexity. Unlocks an automator for generating DNA.")
    
    def afford(self, game):
        if game.dna >= 100 and game.time >= 1000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 50
            game.time -= 1000
            game.purchasedupgrades += self.name
            self.active = 2

class Membrane_Proteins(Upgrade):
    def __init__(self):
        super().__init__("Membrane Proteins ", [("DNA", 200), ("Time", 2000)], "Organisms begin using nutrients from the earth to grow and produce offspring more efficiently.")
    
    def afford(self, game):
        if game.dna >= 200 and game.time >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 200
            game.time -= 2000
            game.purchasedupgrades += self.name
            self.active = 2

class Photosynthesis(Upgrade):
    def __init__(self):
        super().__init__("Photosynthesis ", [("DNA", 200), ("Time", 2000)], "Unlocks the ability for your microbes to use sunlight as a source of energy, providing a significant boost to their metabolism and growth rate.")
    
    def afford(self, game):
        if game.dna >= 200 and game.time >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 200
            game.time -= 2000
            game.purchasedupgrades += self.name
            self.active = 2

class Aquaporin_Membranes(Upgrade):
    def __init__(self):
        super().__init__("Aquaporin Membranes ", [("DNA", 500)], "Microbes can produce specialized membranes that allow them to absorb water more efficiently, increasing their ability to survive and reproduce in aquatic environments. Unlocks hydro-synthesis.")
    
    def afford(self, game):
        if game.dna >= 500:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 500
            game.purchasedupgrades += self.name
            self.active = 2

class DNA_Amplifier(Upgrade):
    def __init__(self):
        super().__init__("DNA Amplifier ", [("DNA", 750), ("Nutrients", 100), ("Water", 100)], "Your organisms can evolve eukaryotic cells, which provide increased genetic complexity and the ability to perform specialized functions.")
    
    def afford(self, game):
        if game.dna >= 750 and game.nutrients >= 100 and game.water >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 750
            game.nutrients -= 100
            game.water -= 100
            game.purchasedupgrades += self.name
            self.active = 2

class Flagella(Upgrade):
    def __init__(self):
        super().__init__("Flagella ", [("DNA", 300), ("Nutrients", 50), ("Water", 100)], "Your organisms can produce flagella, providing increased mobility and the ability to explore new environments, allowing for greater reproduction rates.")
    
    def afford(self, game):
        if game.dna >= 300 and game.nutrients >= 50 and game.water >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 300
            game.nutrients -= 50
            game.water -= 100
            game.purchasedupgrades += self.name
            self.active = 2

class Chloroplasts(Upgrade):
    def __init__(self):
        super().__init__("Chloroplasts ", [("DNA", 400), ("Nutrients", 120), ("Water", 75)], "Your organisms can produce Chloroplasts, providing more efficient usage of nutrients to make the resource last longer.")
    
    def afford(self, game):
        if game.dna >= 400 and game.nutrients >= 120 and game.water >= 75:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 400
            game.nutrients -= 120
            game.water -= 75
            game.purchasedupgrades += self.name
            self.active = 2

class Mitochondria(Upgrade):
    def __init__(self):
        super().__init__("Mitochondria ", [("DNA", 500), ("Nutrients", 130), ("Water", 100)], "The powerhouse of the cell, your organisms will be able to preserve more water and use it more efficiently.")
    
    def afford(self, game):
        if game.dna >= 500 and game.nutrients >= 130 and game.water >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 500
            game.nutrients -= 130
            game.water -= 100
            game.purchasedupgrades += self.name
            self.active = 2

class Biofilm_Production(Upgrade):
    def __init__(self):
        super().__init__("Biofilm Production ", [("DNA", 600), ("Nutrients", 150), ("Water", 170)], "Unlocks the ability for microbes to produce a sticky biofilm, which can protect them from environmental stressors and allow for cooperative behavior, improving microbial reproduction.")
    
    def afford(self, game):
        if game.dna >= 600 and game.nutrients >= 150 and game.water >= 170:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 600
            game.nutrients -= 150
            game.water -= 170
            game.purchasedupgrades += self.name
            self.active = 2

class Chemosynthesis(Upgrade):
    def __init__(self):
        super().__init__("Chemosynthesis ", [("DNA", 700), ("Nutrients", 300), ("Water", 150)], "Unlocks the ability for microbes to use chemical energy to produce organic matter, which can support more complex ecosystems.")
    
    def afford(self, game):
        if game.dna >= 700 and game.nutrients >= 300 and game.water >= 150:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 700
            game.dna -= 300
            game.dna -= 150
            game.purchasedupgrades += self.name
            self.active = 2

class Oxygenation(Upgrade):
    def __init__(self):
        super().__init__("Oxygenation ", [("DNA", 700), ("Nutrients", 150), ("Water", 300)], "Increases the amount of oxygen in the environment, allowing for the evolution of more complex life forms.")
    
    def afford(self, game):
        if game.dna >= 700 and game.nutrients >= 150 and game.water >= 300:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 50
            game.purchasedupgrades += self.name
            self.active = 2

class Differentiation(Upgrade):
    def __init__(self):
        super().__init__("Differentiation ", [("DNA", 3000), ("Nutrients", 1000), ("Water", 1000), ("Time", 5000)], "With cells abot to specialize and perform different functions within a colony, unlocks Ediacaran organisms.")
    
    def afford(self, game):
        if game.dna >= 3000 and game.nutrients >= 1000 and game.water >= 1000 and game.time >= 5000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 3000
            game.dna -= 1000
            game.dna -= 1000
            game.dna -= 5000
            game.purchasedupgrades += self.name
            self.active = 2

class Symbiosis(Upgrade):
    def __init__(self):
        super().__init__("Symbiosis ", [("", 0)], "Unlocks the ability for different organisms to form mutually beneficial relationships.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Diatoms(Upgrade):
    def __init__(self):
        super().__init__("Diatoms ", [("", 0)], "Unlocks the ability to produce silica shells, allowing for the creation of diatoms, a type of algae that are key primary producers in aquatic environments.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Algal_Blooms(Upgrade):
    def __init__(self):
        super().__init__("Algal Blooms ", [("", 0)], "Algae create massive populations of algae, known as algal blooms, which can provide food for higher trophic levels and help to sequester carbon dioxide from the atmosphere.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Mixotrophy(Upgrade):
    def __init__(self):
        super().__init__("Mixotrophy ", [("", 0)], "Unlocks the ability to combine photosynthesis with phagocytosis, allowing algae to take in organic matter as a supplementary energy source when light levels are low.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Ozone_Layer(Upgrade):
    def __init__(self):
        super().__init__("Ozone Layer ", [("", 0)], "Unlocks the ability to live outside of water once evolved enough")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Ecosystems(Upgrade):
    def __init__(self):
        super().__init__("Ecosystems ", [("", 0)], "Ecosystems begin forming across the Earth, manage environmental quality and species diversity for improvements to growth rates and DNA generation.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Nervous_System(Upgrade):
    def __init__(self):
        super().__init__("Nervous System ", [("", 0)], "Unlocks the ability to develop a nervous system, allowing for more complex behaviors and movement, allowing for the evolution of simple invertebrates such as fish.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Endoskeleton(Upgrade):
    def __init__(self):
        super().__init__("Endoskeleton ", [("", 0)], "Unlocks the ability to develop an internal skeleton, providing even greater protection and support to fish.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Swim_Bladder(Upgrade):
    def __init__(self):
        super().__init__("Swim Bladder ", [("", 0)], "Unlocks the ability for fish to control their buoyancy in the water column, conserving energy and allowing for more efficient movement and hunting.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Exoskeleton(Upgrade):
    def __init__(self):
        super().__init__("Exoskeleton ", [("", 0)], "Unlocks the ability to develop an external skeleton, providing protection and support, leading to the evolution of arthropods such as insects.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Metamorphosis(Upgrade):
    def __init__(self):
        super().__init__("Metamorphosis ", [("", 0)], "Unlocks the ability to undergo metamorphosis, which allows insects to transition from a larval form to an adult form.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Insectoid_Wings(Upgrade):
    def __init__(self):
        super().__init__("Insectoid Wings ", [("", 0)], "Unlocks the insect's ability to develop wings, which allows insects to fly and access new habitats and resources.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Oviparity(Upgrade):
    def __init__(self):
        super().__init__("Oviparity ", [("", 0)], "Unlocks the ability for organisms to lay eggs, allowing for the evolution of amphibians who start their life in water but eventually live on land.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Lungs_and_Limbs(Upgrade):
    def __init__(self):
        super().__init__("Lungs and Limbs ", [("", 0)], "Unlocks the ability for amphibians to breathe air and to crawl and climb on land.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Internal_Fertilization(Upgrade):
    def __init__(self):
        super().__init__("Internal Fertilization ", [("", 0)], "Unlocks the ability for amphibians to reproduce on land and increase their reproductive success.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Tetrapods(Upgrade):
    def __init__(self):
        super().__init__("Tetrapods ", [("", 0)], "Evolve from amphibians tor other classes of tetrapods, such as reptiles, birds, and mammals.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Ectothermy(Upgrade):
    def __init__(self):
        super().__init__("Ectothermy ", [("", 0)], "Some animals evolve to have the ability to regulate body temperature through basking in the sun and other external heat sources. Unlocks reptiles.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Reptilian_Scales(Upgrade):
    def __init__(self):
        super().__init__("Reptilian Scales ", [("", 0)], "Reptiles gain the ability to grow scales, providing protection against predators and harsh environments.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Ecdysis(Upgrade):
    def __init__(self):
        super().__init__("Ecdysis ", [("", 0)], "Reptiles gain the ability to shed their skin to facilitate growth and remove parasites, improving health and survival rates.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Double_Helix_Master(Upgrade):
    def __init__(self):
        super().__init__("Double Helix Master ", [("", 0)], "DNA automators kick into a higher gear and begin processing faster and more efficiently.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2


class Mammary_Glands(Upgrade):
    def __init__(self):
        super().__init__("Mammary Glands ", [("", 0)], "Some animals develop the ability to produce milk to feed offspring. Unlocks mammals.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Fur(Upgrade):
    def __init__(self):
        super().__init__("Fur ", [("", 0)], "Mammals start growing fur, providing insulation and protection from the environemnt, improving their survival rates.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Neucortex(Upgrade):
    def __init__(self):
        super().__init__("Neucortex ", [("", 0)], "Mammals begin showing early signs of unlocking higher cognitive functions, such as problem-solving, decision-making, and social interaction.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Flight_Feathers(Upgrade):
    def __init__(self):
        super().__init__("Flight Feathers ", [("", 0)], "Some animals evolve to grow feathered wings permitting them to fly. Unlocks birds.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Beaks_and_Talons(Upgrade):
    def __init__(self):
        super().__init__("Beaks and Talons ", [("", 0)], "Birds evolve to have varying shaped beaks and talons, allowing for easier collection of food and self-defense.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Vocalization_and_Coloration(Upgrade):
    def __init__(self):
        super().__init__("Vocalization and Coloration ", [("", 0)], "Birds develop unique colorations and adopt vocal communication to attract mates and warn of danger.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Adaptability(Upgrade):
    def __init__(self):
        super().__init__("Adaptability ", [("", 0)], "Increases in adaptability of all species allows animals to thrive in different environments and social dynamics. Effects of symbiosis is amplified as a result.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Dinosaurs(Upgrade):
    def __init__(self):
        super().__init__("Dinosaurs ", [("", 0)], "Early signs of the dinosaurs begin to arise as animals develop bipedalism and exhibit rapid muscle growth, becoming immense in size in a short period of time.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Increased_Muscle_Mass(Upgrade):
    def __init__(self):
        super().__init__("Increased Muscle Mass ", [("", 0)], "Dinosaurs further build more muscle mass. Massive lifeforms begin roaming the Earth.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Competition_and_Cooperation(Upgrade):
    def __init__(self):
        super().__init__("Competition and Cooperation ", [("", 0)], "Herbivores and carnivore dinosaurs form social dynamics to improve their chances of survival.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Continental_Drift(Upgrade):
    def __init__(self):
        super().__init__("Continental Drift ", [("", 0)], "Over time, continents drift more closer and farther apart, landmasses are seperated and new environments are created. Animal diversity is boosted.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Climate_Stabilization(Upgrade):
    def __init__(self):
        super().__init__("Climate Stabilization ", [("", 0)], "Climate change on Earth begin to stabilize over several million years of drastic cycles in preperation for a new form of life to come.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Sacrifice_The_Dinosaurs(Upgrade):
    def __init__(self):
        super().__init__("Sacrifice the Dinosaurs. ", [("", 0)], "A large asteroid is soon to collide with the Earth, causing massive devastation and leading to the extinction of the dinosaurs. This tragedy is unnavoidable, and may just be the necessary to achieving a higher intelligence.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Evolutionary_Radiation(Upgrade):
    def __init__(self):
        super().__init__("Evolutionary Radiation ", [("", 0)], "The asteroid has struck the Earth. What remains of the dinosaurs has been burried deep in the ground. But this sudden disappearance of dominant competitors will lead to rapid diversification of new species. A new era of possibility will soon follow.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Opposable_Thumbs(Upgrade):
    def __init__(self):
        super().__init__("Opposable Thumbs ", [("", 0)], "Species of animals are develop thumbs, allowing for grasping onto branches and manipulating objects. Primates are born.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Increased_Brain_Size(Upgrade):
    def __init__(self):
        super().__init__("Increased Brain Size ", [("", 0)], "Primates experience brain development and are able to learn and adapt to new environments. This is important for primates that need to navigate complex arboreal environments and communicate with other members of their social group.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Social_Complexity(Upgrade):
    def __init__(self):
        super().__init__("Social Complexity ", [("", 0)], "Primates begin introducing more complex social structures. Primates that are able to coordinate their actions and work together to achieve common goals.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Tool_Use(Upgrade):
    def __init__(self):
        super().__init__("Tool Use ", [("", 0)], "Primates begin to manipulate their environment, using sticks, stones, or other objects to access food, build shelter, or defend against predators.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2

class Homo_Sapiens(Upgrade):
    def __init__(self):
        super().__init__("Homo Sapiens ", [("", 0)], "Congratulations! This is as far as the game has been implemented so far!")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.purchasedupgrades += self.name
            self.active = 2