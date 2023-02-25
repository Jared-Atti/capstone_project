# class Upgrades:
#     def new(cls):
#         if cls._instance is None:
#             cls._instance = super().new(cls)
#         return cls._instance

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
                coststr += str(self.costs[i][1]) + " " + str(self.costs[i][0]) + ", "
            else:
                coststr += str(self.costs[i][1]) + " " + str(self.costs[i][0])
        return coststr + ")"

# Cosmic Upgrades
class GravitationalCompression(Upgrade):
    def __init__(self):
        super().__init__("Gravitational Compression", [("Energy", 20)], "Siphon energy from space dust collapsing under its own gravity. Unlocks production menu.")
    
    def afford(self, game):
        if game.energy >= 20:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 20
            # game.energyRev += 0.1
            game.purchasedupgrades += self.name
            self.active = 2

class SubatomicSynthesis(Upgrade):
    def __init__(self):
        super().__init__("Subatomic Synthesis", [("Energy", 150)], "Smash particles together and convert the energy into quarks.")

    def afford(self, game):
        if game.energy >= 150:
            return True

    def purchase(self, game):
        if self.afford(game):
            game.energy -= 150
            game.purchasedupgrades += self.name
            self.active = 2

class Temporal(Upgrade):
    def __init__(self):
        super().__init__("Temporal", [("Energy", 200)], "By harnessing the power of cosmic forces, you have unlocked the ability to manipulate time and expand the fabric of space itself.")
    
    def afford(self, game):
        if game.energy >= 200:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 200
            game.timeFlag = True
            game.purchasedupgrades += self.name
            self.active = 2

class Innovation(Upgrade):
    def __init__(self):
        super().__init__("Innovation", [("Time", 1000)], "Unlocks the production of Innovation.")

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
        super().__init__("Nucleosynthesis", [("Quarks", 100), ("Innovation", 20)], "Unlocks proton & neutron automator & resource.")

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
        super().__init__("Gravitational Amplification", [("Energy", 1000), ("Time", 2000)], "Improves comrpessor automator.")

    def afford(self, game):
        if game.energy >= 1000 and game.time >= 2000:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 1000
            game.time -= 2000
            game.purchasedupgrades += self.name
            self.active = 2

class Quark_Fusion(Upgrade):
    def __init__(self):
        super().__init__("Quark Fusion", [("Innovation", 30), ("Energy", 1500)], "Halves the cost of quarks, doubles the production.")

    def afford(self, game):
        if game.innovation >= 30 and game.energy >= 1500:
            return True
    
    def purchase(self, game):
        if self.afford(game):
            game.energy -= 1500
            game.innovation -= 30
            game.purchasedupgrades += self.name
            self.active = 2

class Atomic_Fabrication(Upgrade):
    def __init__(self):
        super().__init__("Atomic Fabrication", [("Innovation", 100), ("Quarks", 200), ("Energy", 1000)], "Unlocks Hydrogen production.")

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
        super().__init__("Discover Helium", [("Innovation", 150), ("Quarks", 300), ("Energy", 1000)], "Unlocks Helium production.")

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

# Precambrian Upgrades
class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation", [("DNA", 10)], "Generates passive DNA points for every living microbe.")
