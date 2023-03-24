class Automator():
    def __init__(self, name, upcost, revenue, tickcost):
        self.name = name
        self.upcost = upcost
        self.revenue = revenue
        self.tickcost = tickcost
        self.count = 0
        self.toggle = 1
        self.active = 0 # 0 = Not yet unlocked, 1 = Unlocked but not purchased, 2 = Purchased
    
    def showCost(self):
        return "Cost: " + "{:,.0f}".format(self.upcost[1]) + " " + self.upcost[0]

    def calc_revenue(self):
        return (self.revenue[1] * self.count) / 10
    
    def calc_cost(self, index):
        return (self.tickcost[index][1] * self.count) / 10
    
    def desc(self):
        if (self.tickcost):
            text = "Each " + self.name + " produces " + "{:,.0f}".format(self.revenue[1]) + " " + self.revenue[0] + " and costs "
            for i in range(len(self.tickcost)):
                text += "({:,.0f}".format(self.tickcost[i][1]) + " " + self.tickcost[i][0] + ") "

            return text + "per tick"
        else:
             return "Each " + self.name + " produces " + "{:,.0f}".format(self.revenue[1]) + " " + self.revenue[0] + " per tick"

class Compressor(Automator):
    def __init__(self):
        super().__init__("Compressor", ("Energy", 10), ("Energy", 1), None)
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.1))
            self.count += 1

class Quark_Synthesizer(Automator):
    def __init__(self):
        super().__init__("Quark Synthesiser", ("Energy", 50), ("Quarks", 1), [("Energy", 8)])
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.05))
            self.count += 1

class Proton_Synthesizer(Automator):
    def __init__(self):
        super().__init__("Proton Synthesiser", ("Energy", 100), ("Proton", 1), [("Quarks", 3)])
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.05))
            self.count += 1

class Neutron_Synthesizer(Automator):
    def __init__(self):
        super().__init__("Neutron Synthesiser", ("Energy", 100), ("Neutron", 1), [("Quarks", 3)])
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.05))
            self.count += 1


class Hydrogen_Fabricator(Automator):
    def __init__(self):
        super().__init__("Hydogen Fabricator", ("Energy", 200), ("Hydrogen", 1), [("Proton", 1)])
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.05))
            self.count += 1

class Helium_Fabricator(Automator):
    def __init__(self):
        super().__init__("Helium Fabricator", ("Energy", 200), ("Helium", 1), [("Proton", 2),("Neutron", 2)])
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.05))
            self.count += 1

class Nuclear_Fusion(Automator):
    def __init__(self):
        super().__init__("Nuclear Fusion", [("Hydrogen", 10000),("Helium", 7500)], None, None)
        self.toggle = 0
    
    def desc(self):
         return "Improves all other automators by 10% every purchase."
    
    def showCost(self):
        return "Cost: " + "{:,.0f}".format(self.upcost[0][1]) + " " + self.upcost[0][0] + " and " + "{:,.0f}".format(self.upcost[1][1]) + " " + self.upcost[1][0]

    def afford(self, game):
        if game.hydrogen >= self.upcost[0][1] and game.helium >= self.upcost[1][1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.hydrogen -= self.upcost[0][1]
            self.upcost = [(self.upcost[0][0], round(self.upcost[0][1] * 1.9)), (self.upcost[1][0], round(self.upcost[1][1] * 1.9))]
            self.count += 1