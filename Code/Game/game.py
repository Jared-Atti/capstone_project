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
        self.lifeforms = 0
        
        ## Cosmic
        self.quarks = 0
        self.protons = 0
        self.neutrons = 0
        self.energy = 0
        self.hydrogen = 0
        self.helium = 0
        self.nuclears = 0
        
        # Precambrian
        self.microbes = 0
        self.repro_microbes = 0
        self.dna = 0
        self.nutrients = 0
        self.water = 0
        self.mutationflag = 0
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_energy(self):
        self.energy += 1
        # Testing
        self.energy += 100000000000
        self.maxpotential += 100
        self.time += 100000000000
        self.expansion += 50
        self.productivity += 50
        self.innovation += 10000
        self.protons += 100000000000
        self.neutrons += 100000000000
        self.quarks += 100000000000
        self.hydrogen += 100000000000
        self.helium += 100000000000

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
        # Lifeforms
        self.lifeforms = self.microbes

        # Time and innovation
        if (self.temporalFrame == True):
            if (self.time + self.productivity > self.expansion * 1000):
                self.time = self.expansion * 1000
            elif (self.time < self.expansion * 1000):
                self.time += self.productivity * 5
            
            if (self.innovationFlag and self.time >= self.expansion * 1000):
                self.innovation += self.productivity * 0.5
            elif (self.innovationFlag):
                self.innovation += self.productivity * 0.025

        #DNA Mutation
        if (self.mutationflag):
            self.dna += (self.microbes * 0.001)
        
        #Reproductions
        if (self.repro_microbes >= 0):
            self.microbes += self.microbes * self.repro_microbes

        # Automators
        for a in autos:
            if a.toggle == 1:
                afford = False
                # Checking cost
                if (a.tickcost):
                    for i in range(len(a.tickcost)):
                        if a.tickcost[i][0] == "Energy" and a.calc_cost(i) <= self.energy:
                            self.energy -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Quarks" and a.calc_cost(i) <= self.quarks:
                            self.quarks -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Protons" and a.calc_cost(i) <= self.protons:
                            self.protons -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Neutrons" and a.calc_cost(i) <= self.neutrons:
                            self.neutrons -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Hydrogen" and a.calc_cost(i) <= self.hydrogen:
                            self.hydrogen -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Helium" and a.calc_cost(i) <= self.helium:
                            self.helium -= a.calc_cost(i)
                            afford = True
                else:
                    afford = True
                
                # Adding revenue
                if afford:
                    if a.revenue[0] == "Energy":
                        self.energy += a.calc_revenue()
                    elif a.revenue[0] == "Quarks":
                        self.quarks += a.calc_revenue()
                    elif a.revenue[0] == "Protons":
                        self.protons += a.calc_revenue()
                    elif a.revenue[0] == "Neutrons":
                        self.neutrons += a.calc_revenue()
                    elif a.revenue[0] == "Hydrogen":
                        self.hydrogen += a.calc_revenue()
                    elif a.revenue[0] == "Helium":
                        self.helium += a.calc_revenue()

            

_instance = Game()
def Game():
    return _instance
