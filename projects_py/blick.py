class Blick:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def shoot(self):
        while self.ammo > 0:
            input()
            self.ammo -= 1
            print(f'{self.name} ammo: {self.ammo}')

revolver = Blick("Revolver", 6)
glock = Blick("G17", 17)
        
glock.shoot()