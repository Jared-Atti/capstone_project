class Game:
    _instance = None

    def new(cls):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance

    def init(self):
        self.organisms = 0
        self.dna = 0
        self.speciesList = []
        self.popCap = 0
        self.revenue = 0
        self.upgrades = []

    def make_life(self):
        self.organisms += 1

    def buy_upgrade(self,upgrade):
        if self.dna >= upgrade.cost:
            self.dna -= upgrade.cost
            self.upgrades.append(upgrade)
            upgrade.apply()
