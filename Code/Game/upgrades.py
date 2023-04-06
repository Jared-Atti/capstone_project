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
                coststr += str("{:,.0f}".format(self.costs[i][1])) + " " + str(self.costs[i][0]) + ", "
            else:
                coststr += str("{:,.0f}".format(self.costs[i][1])) + " " + str(self.costs[i][0])
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
        super().__init__("Cool Down ", ("Time", 100), "The Earth is still forming and a very hot molten ball of rock. It needs some time be cool. In the meantime, it can be bombarded with asteroids and collect some interesting materials, maybe even a moon.")

    def afford(self, game):
        if game.time >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 100
            game.purchasedupgrades += self.name
            self.active = 2

# Precambrian Upgrades
class DNA_Points(Upgrade):
    def __init__(self):
        super().__init__("DNA Points ", ("Time", 10), "Sacrifice everything you have gathered throughout the Cosmic era to discover a new material called DNA.")

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
        super().__init__("Genetic Mutation ", [("DNA", 25)], "Generates passive DNA points for every living microbe.")
    
    def afford(self, game):
        if game.dna >= 25:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 25
            game.purchasedupgrades += self.name
            self.active = 2

class Metabolic_Adaptation(Upgrade):
    def __init__(self):
        super().__init__("Metabolic Adaptation ", [("DNA", 50)], "Unlocks the ability to metabolize water and nutrients as resources, allowing for greater growth and expansion of your life forms.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 50
            game.purchasedupgrades += self.name
            self.active = 2

class Asexual_Reproduction(Upgrade):
    def __init__(self):
        super().__init__("Asexual Reproduction ", [("DNA", 50)], "Microbes begin evolving, learning the ability to reproduce asexually.  Reproducers begin increasing the amount of microbes.")
    
    def afford(self, game):
        if game.dna >= 50:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.dna -= 50
            game.purchasedupgrades += self.name
            self.active = 2
