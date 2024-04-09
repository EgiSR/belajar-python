class hero:
    def __init__(self, inputName, inputHealth, inputpower): #self 
        self.name = inputName
        self.health = inputHealth
        self.power = inputpower


hero1 = hero("egi", 100, 100)

print(hero1.__dict__)