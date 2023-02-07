class Game:
    def new(cls):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance

    def init(self):
        # General
        self.speciesList = []
        self.upgrades = []
        
        # Cosmic
        self.protons = 0
        self.neutrons = 0
        self.energy = 0
        self.hydrogen = 0
        self.helium = 0
        self.oxygen = 0
        self.silicon = 0
        self.aluminum = 0
        self.iron = 0
        self.suppelements = 0 # supplementary
        
        # Precambrian
        self.microbes = 0
        self.dna = 0
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_energy(self):
        self.energy += 1

    def create_life(self):
        self.microbes += 1

    def buy_upgrade(self,upgrade):
        if self.dna >= upgrade.cost:
            self.dna -= upgrade.cost
            self.upgrades.append(upgrade)
            upgrade.apply()

_instance = Game()
def Game():
    return _instance
