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
            game.productionFrame = True
            game.purchasedupgrades += self.name
            self.active = 2

class SubatomicSynthesis(Upgrade):
    def __init__(self):
        super().__init__("Subatomic Synthesis", [("Energy", 150)], "Unlocks the production of Quarks.")

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
        super().__init__("Temporal", ("Energy", 100), "Unlocks the production of Time and Innovation.")
    
    def afford(self, game):
        if game.energy >= self.cost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.cost[1]
            self.cost = (self.cost[0], round(self.cost[1] * 1.25))
            self.count += 1


# Precambrian Upgrades
class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation", [("DNA", 10)], "Generates passive DNA points for every living microbe.")
