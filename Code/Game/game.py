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
        self.cheat = 10
        
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
        self.repro_microbes = 0.001
        self.plants = 0
        self.repro_plants = 0.001
        self.fish = 0
        self.repro_fish = 0.001
        self.insects = 0
        self.repro_insects = 0.001
        self.amphibians = 0
        self.repro_amphibians = 0.001
        self.reptiles = 0
        self.repro_reptiles = 0.001
        self.birds = 0
        self.repro_birds = 0.001
        self.mammals = 0
        self.repro_mammals = 0.001
        self.dinosaurs = 0
        self.repro_dinosaurs = 0.001
        self.primates = 0
        self.repro_primates = 0.001
        self.dna = 0
        self.nutrients = 0
        self.water = 0
        self.mutationflag = 0
        self.waterflag = 0
        self.nutrientsflag = 0
    
    def get(self):
        if self is None:
            return self.init()
        return self

    def create_energy(self):
        self.energy += 1
        # Testing cheats
        # self.energy += 100000000000
        # self.maxpotential += 100
        # self.time += 100000000000
        # self.expansion += 50
        # self.productivity += 50
        # self.innovation += 10000
        # self.protons += 100000000000
        # self.neutrons += 100000000000
        # self.quarks += 100000000000
        # self.hydrogen += 100000000000
        # self.helium += 100000000000

    def create_life(self):
        self.microbes += 1 + self.repro_microbes * 1000 * self.cheat
        if self.plants > 0:
            self.plants += 1 + self.repro_plants * 1000 * self.cheat
        if self.fish > 0:
            self.fish += 1 + self.repro_fish * 1000 * self.cheat
        if self.insects > 0:
            self.insects += 1 + self.repro_insects * 1000 * self.cheat
        if self.amphibians > 0:
            self.amphibians += 1 + self.repro_amphibians * 1000 * self.cheat
        if self.reptiles > 0:
            self.reptiles += 1 + self.repro_reptiles * 1000 * self.cheat
        if self.birds > 0:
            self.birds += 1 + self.repro_birds * 1000 * self.cheat
        if self.mammals > 0:
            self.mammals += 1 + self.repro_mammals * 1000 * self.cheat
        if self.dinosaurs > 0:
            self.dinosaurs += 1 + self.repro_dinosaurs * 1000 * self.cheat
        if self.primates > 0:
            self.primates += 1 + self.repro_primates * 1000 * self.cheat
        # Testing cheats
        # self.microbes += 1000
        # self.water += 1000
        # self.nutrients += 1000
        # self.dna += 1000
    
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

        # Time and innovation
        if (self.temporalFrame == True):
            if (self.time + self.productivity > self.expansion * 1000):
                self.time = self.expansion * 1000
            elif (self.time < self.expansion * 1000):
                self.time += self.productivity * 5 * self.cheat
            
            if (self.innovationFlag and self.time >= self.expansion * 1000):
                self.innovation += self.productivity * 0.5 * self.cheat
            elif (self.innovationFlag):
                self.innovation += self.productivity * 0.025 * self.cheat

        #DNA Mutation
        if (self.mutationflag):
            self.dna += (self.microbes * 0.002) * self.cheat
        if (self.waterflag):
            self.water += (self.microbes * 0.0005) * self.cheat
        if (self.nutrientsflag):
            self.nutrients += (self.microbes * 0.0005) * self.cheat
        
        #Reproductions
        if (self.repro_microbes >= 0):
            self.microbes += self.microbes * self.repro_microbes * self.cheat
            self.lifeforms += self.microbes * self.repro_microbes * self.cheat
        if (self.repro_plants >= 0):
            self.plants += self.plants * self.repro_plants * self.cheat
            self.lifeforms += self.plants * self.repro_plants * self.cheat
        if (self.repro_fish >= 0):
            self.fish += self.fish * self.repro_fish * self.cheat
            self.lifeforms += self.fish * self.repro_fish * self.cheat
        if (self.repro_insects >= 0):
            self.insects += self.insects * self.repro_insects * self.cheat
            self.lifeforms += self.insects * self.repro_insects * self.cheat
        if (self.repro_amphibians >= 0):
            self.amphibians += self.amphibians * self.repro_amphibians * self.cheat
            self.lifeforms += self.amphibians * self.repro_amphibians * self.cheat
        if (self.repro_reptiles >= 0):
            self.reptiles += self.reptiles * self.repro_reptiles * self.cheat
            self.lifeforms += self.reptiles * self.repro_reptiles * self.cheat
        if (self.repro_birds >= 0):
            self.birds += self.birds * self.repro_birds * self.cheat
            self.lifeforms += self.birds * self.repro_birds * self.cheat
        if (self.repro_mammals >= 0):
            self.mammals += self.mammals * self.repro_mammals * self.cheat
            self.lifeforms += self.mammals * self.repro_mammals * self.cheat
        if (self.repro_dinosaurs != 0):
            self.dinosaurs += self.dinosaurs * self.repro_dinosaurs * self.cheat
            self.lifeforms += self.dinosaurs * self.repro_dinosaurs * self.cheat
            if (self.dinosaurs < 1):
                self.dinosaurs = 0
                self.repro_dinosaurs = 0
        if (self.repro_primates >= 0):
            self.primates += self.primates * self.repro_primates * self.cheat
            self.lifeforms += self.primates * self.repro_primates * self.cheat

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
                        elif a.tickcost[i][0] == "Water" and a.calc_cost(i) <= self.water:
                            self.water -= a.calc_cost(i)
                            afford = True
                        elif a.tickcost[i][0] == "Nutrients" and a.calc_cost(i) <= self.nutrients:
                            self.nutrients -= a.calc_cost(i)
                            afford = True
                else:
                    afford = True
                
                # Adding revenue
                if afford:
                    if a.revenue[0] == "Energy":
                        self.energy += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Quarks":
                        self.quarks += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Protons":
                        self.protons += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Neutrons":
                        self.neutrons += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Hydrogen":
                        self.hydrogen += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Helium":
                        self.helium += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "DNA":
                        self.dna += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Nutrients":
                        self.nutrients += a.calc_revenue() * self.cheat
                    elif a.revenue[0] == "Water":
                        self.water += a.calc_revenue() * self.cheat

            

_instance = Game()
def Game():
    return _instance
