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
        self.potential = 0
        self.potential_lifeforms_req = 1
        self.productivity = 1
        self.expansion = 1
        self.maxpotential = self.potential + self.productivity + self.expansion
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
        
        # Precambrian
        self.microbes = 0
        self.dna = 0
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_energy(self):
        self.energy += 1
        # # Testing
        self.energy += 200000
        self.time += 1000
        # self.potential += 1
        # self.maxpotential += 1
        self.innovation += 10
        self.quarks += 100

    def create_life(self):
        self.microbes += 1
    
    def set_max_potential(self):
        self.maxpotential = self.potential + self.productivity + self.expansion
      
    def buy_upgrade(self, upgrade):
        upgrade.purchase(self)

    def buy_autoupgrade(self, upgrade, *autos):
        return upgrade.purchase(self, autos)

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
                self.innovation += self.productivity * 0.1


        for a in autos:
            if a.toggle == 1:
                afford = False
                # Checking cost
                if (a.tickcost):
                    if a.tickcost[0] == "Energy" and a.calc_cost() <= self.energy:
                        self.energy -= a.calc_cost()
                        afford = True
                    elif a.tickcost[0] == "Quark" and a.calc_cost() <= self.quarks:
                        self.quarks -= a.calc_cost()
                        afford = True
                    elif a.tickcost[0] == "Proton" and a.calc_cost() <= self.protons:
                        self.protons -= a.calc_cost()
                        afford = True
                    elif a.tickcost[0] == "Neutron" and a.calc_cost() <= self.neutrons:
                        self.neutrons -= a.calc_cost()
                        afford = True
                else:
                    afford = True
                
                # Adding revenue
                if afford:
                    if a.revenue[0] == "Energy":
                        self.energy += a.calc_revenue()
                    elif a.revenue[0] == "Quark":
                        self.quarks += a.calc_revenue()
                    elif a.revenue[0] == "Proton":
                        self.protons += a.calc_revenue()
                    elif a.revenue[0] == "Neutron":
                        self.neutrons += a.calc_revenue()

            

_instance = Game()
def Game():
    return _instance
