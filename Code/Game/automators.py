class Automator():
    def __init__(self, name, cost, revenue):
        self.name = name
        self.cost = cost
        self.revenue = revenue
        self.count = 0
        self.active = 0 # 0 = Not yet unlocked, 1 = Unlocked but not purchased, 2 = Purchased
    
    def showCost(self):
        return "Cost: " + "{:,.0f}".format(self.cost[1]) + " " + self.cost[0]

    def calc_revenue(self):
        return (self.revenue[1] * self.count) / 10
    
    def desc(self):
        return "Each " + self.name + " produces " + "{:,.0f}".format(self.revenue[1]) + " " + self.revenue[0] + " per tick"

class Compressor(Automator):
    def __init__(self):
        super().__init__("Compressor", ("Energy", 10), ("Energy", 1))
    
    def afford(self, game):
        if game.energy >= self.cost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.cost[1]
            self.cost = (self.cost[0], round(self.cost[1] * 1.25))
            self.count += 1

class Siphoner(Automator):
    def __init__(self):
        super().__init__("Siphoner", ("Energy", 100), ("Energy", 1))
    
    def afford(self, game):
        if game.energy >= self.cost[1]:
            return True
    
    def increase(self, game):
        if self.afford(game):
            game.energy -= self.cost[1]
            self.cost = (self.cost[0], round(self.cost[1] * 1.25))
            self.count += 1