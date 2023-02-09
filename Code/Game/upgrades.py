class Cost:
     def __init__(self, resource, value):
        self.resource = resource
        self.value = value

class Upgrade:
    def __init__(self, name, costs, description):
        self.name = name
        self.cost = Cost(costs)
        self.description = description

class Upgrades:
    def __init__(self):
        self.purchased_upgrades = []
        # example: self.upgrades = [GeneticMutation()]
        self.upgrades = []
    
    def purchase_upgrade(self, upgrade_name, game_stats):
        for upgrade in self.upgrades:
            if upgrade.name == upgrade_name:
                if game_stats.dna >= upgrade.cost:
                    game_stats.dna -= upgrade.cost
                    self.purchased_upgrades.append(upgrade)
                    return True
                else:
                    return False
        return False

# Cosmic Upgrades
class SiphonRadiation(Upgrade):
    def __init__(self):
        super().__init__("Siphon Radiation", [("Energy", 10)], "Being siphoning radiation for 1 energy per second.")

# Precambrian Upgrades
class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation", [("DNA", 10)], "Generates passive DNA points for every living microbe.")
