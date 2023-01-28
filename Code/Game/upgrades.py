class Upgrade:
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

class GeneticMutation(Upgrade):
    def __init__(self):
        super().__init__("Genetic Mutation", 10, "Generates passive DNA points for every living organism.")

class Upgrades:
    def __init__(self):
        self.purchased_upgrades = []
        self.upgrades = [GeneticMutation()]
    
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