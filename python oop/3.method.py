class Hero:
    #static variable, yang akan menempel diclassnya
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputpower):
        #instance variable 
        self.name = inputName
        self.health = inputHealth
        self.power = inputpower
        Hero.jumlah_hero += 1
    
    #void function/ method tanpa return
    def siapa(self):
        print("namaku adalah "+ self.name)
    
    #method dengan argument
    def healthUp(self, up):
        self.health += up
    
    #method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("sniper", 100, 100)
hero2 = Hero("fighter", 200, 100)

hero1.siapa()
hero1.healthUp(40)
print(hero1.__dict__)