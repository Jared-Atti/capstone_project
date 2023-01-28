class Game:
    def new(cls):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance

    def init(self):
        self.pop = 0
        self.dna = 0
        self.speciesList = []
        self.popCap = 100
        self.revenue = 0
        self.upgrades = []
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_life(self):
        self.pop += 1

    def buy_upgrade(self,upgrade):
        if self.dna >= upgrade.cost:
            self.dna -= upgrade.cost
            self.upgrades.append(upgrade)
            upgrade.apply()

_instance = Game()
def Game():
    return _instance
