# import upgrades as upg
import upgrades
import automators

# Initializing Automators
auto_Comp = automators.Compressor()

class Game:
    def new(cls):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance

    def init(self):
        #Frame flags
        self.resourcesFrame = False
        self.upgradesFrame = False
        self.productionFrame = False
        self.temporalFrame = False

        # General
        self.speciesList = []
        self.purchasedupgrades = []
        self.timeFlag = False
        self.time = 0
        self.innovationFlag = False
        self.innovation = 0
        self.maxpotential = 1
        self.potential = 0
        self.potentialincrease = 1
        self.productivity = 1
        self.expansion = 1
        self.currentEra = 0 # 0 = Cosmic, 1 = Precambrian
        
        ## Cosmic
        self.quarks = 0
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

        # Automators
        self.compression_count = 0
        self.compression_cost = 10
        self.compression_rev = 0
        
        # Precambrian
        self.microbes = 0
        self.dna = 0
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_energy(self):
        self.energy += 200

    def create_life(self):
        self.microbes += 1
        

    def buy_upgrade(self, upgrade):
        upgrade.purchase(self)

    def increase_automator(self, automator):
        automator.increase(self)

    def calculate_revenue(self, autos):
        # Every era
        # Time and innovation
        if (self.temporalFrame == True):
            if (self.time + self.productivity > self.expansion * 1000):
                self.time = self.expansion * 1000
            elif (self.time < self.expansion * 1000):
                self.time += self.productivity * 0.99
            
            if (self.innovationFlag and self.time >= self.expansion * 1000):
                self.innovation += self.productivity * 0.025


        for a in autos:
            # Adding revenue
            if a.revenue[0] == "Energy":
                self.energy += a.calc_revenue()
            elif a.revenue[0] == "Quarks":
                self.quarks += a.calc_revenue()

            # Applying cost
            if a.cost[0] == "Energy":
                self.energy -= a.calc_cost()
            elif a.cost[0] == "Quarks":
                self.quarks -= a.calc_cost()

_instance = Game()
def Game():
    return _instance
