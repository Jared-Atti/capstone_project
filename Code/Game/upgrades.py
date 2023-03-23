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
        super().__init__("Innovation ", [("Time", 1000)], "Take your progress to the next level with Innovation. Use your full time to generate innovation and advance even faster!")

    def afford(self, game):
        if game.time >= 1000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 1000
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
        super().__init__("Quark Fusion ", [("Innovation", 30), ("Energy", 1500)], "Master the art of quark fusion to improve your efficiency and cut your quark costs in half!")

    def afford(self, game):
        if game.innovation >= 30 and game.energy >= 1500:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.energy -= 1500
            game.innovation -= 30
            game.purchasedupgrades += self.name
            self.active = 2
            newcost = [(autos[0].tickcost[0][0], autos[0].tickcost[0][1] / 2)]
            newrev = (autos[0].revenue[0], autos[0].revenue[1] * 5)
            autos[0].tickcost = newcost
            autos[0].revenue = newrev
            return autos[0]

class Atomic_Fabrication(Upgrade):
    def __init__(self):
        super().__init__("Atomic Fabrication ", [("Innovation", 100), ("Quarks", 200), ("Energy", 1000)], "Unleash the Power of Atomic Fabrication to Produce Hydrogen!")

    def afford(self, game):
        if game.innovation >= 100 and game.quarks >= 200 and game.energy >= 1000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 1000
            game.innovation -= 100
            game.quarks -= 200
            game.purchasedupgrades += self.name
            self.active = 2

class Discover_Helium(Upgrade):
    def __init__(self):
        super().__init__("Discover Helium ", [("Innovation", 150), ("Quarks", 300), ("Energy", 1000)], "Take your atomic knowledge to new heights with helium!")

    def afford(self, game):
        if game.innovation >= 150 and game.quarks >= 300 and game.energy >= 1000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 1000
            game.innovation -= 150
            game.quarks -= 300
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
        super().__init__("Gravitational Flucuations ", [("Energy", 5000), ("Innovation", 100)], "TBD")

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
        super().__init__("Quark Acceleration ", [("Energy", 20000), ("Innovation", 200)], "TBD")

    def afford(self, game):
        if game.innovation >= 200 and game.energy >= 20000:
            return True
    
    def purchase(self, game, autos):
        if self.afford(game):
            game.innovation -= 200
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
        super().__init__("Proton Processor ", [("Quarks", 50000), ("Energy", 10000)], "TBD")

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
        super().__init__("Nuetron Processor ", [("Quarks", 75000), ("Energy", 15000)], "TBD")

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
        super().__init__("Hydrogenic Catalyst ", [("Protons", 20000), ("Neutrons", 20000)], "TBD")

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
        super().__init__("Helium Extractor ", [("Protons", 30000), ("Neutrons", 30000)], "TBD")

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
        super().__init__("Create the Sun ", [("Time", 10000), ("Hydrogen", 12400000000), ("Helium", 5310000000)], "TBD")

    def afford(self, game):
        if game.time >= 10000 and game.hydrogen >= 12400000000 and game.helium >= 5310000000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 10000
            game.hydrogen -= 12400000000
            game.helium -= 5310000000
            game.purchasedupgrades += self.name
            self.active = 2

class Nuclear_Fusion(Upgrade):
    def __init__(self):
        super().__init__("Nuclear Fusion ", [("Time", 3000), ("Innovation", 75)], "TBD")

    def afford(self, game):
        if game.time >= 3000 and game.innovation >= 75:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 3000
            game.innovation -= 75
            game.purchasedupgrades += self.name
            self.active = 2

class Create_Earth(Upgrade):
    def __init__(self):
        super().__init__("Create the Earth ", [("Time", 5000), ("Innovation", 100)], "TBD")

    def afford(self, game):
        if game.time >= 5000 and game.innovation >= 100:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 5000
            game.innovation -= 100
            game.purchasedupgrades += self.name
            self.active = 2

class Travel_Earth(Upgrade):
    def __init__(self):
        super().__init__("Travel to Earth ", [("Time", 10000)], "TBD")

    def afford(self, game):
        if game.time >= 10000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.time -= 10000
            game.purchasedupgrades += self.name
            self.active = 2

class Nuclear_Fusion_Increase(Upgrade):
    def __init__(self):
        super().__init__("Nuclear Fusion Increase ", None, None)
    
    def purchase(self, game, autos):
        autos[0].revenue = (autos[0].revenue[0], autos[0].revenue[1] * 1.10)
        autos[1].revenue = (autos[1].revenue[0], autos[1].revenue[1] * 1.10)
        autos[2].revenue = (autos[2].revenue[0], autos[2].revenue[1] * 1.10)
        autos[3].revenue = (autos[3].revenue[0], autos[3].revenue[1] * 1.10)
        autos[4].revenue = (autos[4].revenue[0], autos[4].revenue[1] * 1.10)
        autos[5].revenue = (autos[5].revenue[0], autos[5].revenue[1] * 1.10)
        return autos


# Precambrian Upgrades
class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation ", [("DNA", 10)], "Generates passive DNA points for every living microbe.")
