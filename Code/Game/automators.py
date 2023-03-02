class Automator():
    def __init__(self, name, upcost, revenue, tickcost):
        self.name = name
        self.upcost = upcost
        self.revenue = revenue
        self.tickcost = tickcost
        self.count = 0
        self.active = 0 # 0 = Not yet unlocked, 1 = Unlocked but not purchased, 2 = Purchased
    
    def showCost(self):
        return "Cost: " + "{:,.0f}".format(self.upcost[1]) + " " + self.upcost[0]

    def calc_revenue(self):
        return (self.revenue[1] * self.count) / 10
    
    def calc_cost(self):
        return (self.tickcost[1] * self.count) / 10
    
    def desc(self):
        if (self.tickcost):
            return "Each " + self.name + " produces " + "{:,.0f}".format(self.revenue[1]) + " " + self.revenue[0] + " and costs " + "{:,.0f}".format(self.tickcost[1]) + " " + self.tickcost[0] + " per tick"
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
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.25))
            self.count += 1

class Quark_Synthesizer(Automator):
    def __init__(self):
        super().__init__("Quark Synthesiser", ("Energy", 100), ("Quark", 1), ("Energy", 1))
    
    def afford(self, game):
        if game.energy >= self.upcost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.upcost[1]
            self.upcost = (self.upcost[0], round(self.upcost[1] * 1.25))
            self.count += 1