class weapon():
    def __init__(self, name, catagory, damage):
        self.name = name
        self.catagory = catagory
        self.damage = damage
    def getdata(self):
        print(f'Name: {self.name} Catagory: {self.catagory} Damage: {self.damage}')

class sword(weapon):
    def __init__(self, name, catagory, damage, damagecatagory):
        super().__init__(name, catagory, damage)
        self.damagecatagory = damagecatagory
    def getdata(self):
        print(f'Name: {self.name}. Catagory: {self.catagory}. Damage: {self.damage}. Damage Category: {self.damagecatagory}. Critical: {self.damage * 5}.')

sword = sword('Blade of Life', 'Katana', 50, 'Slashing')

sword.getdata()