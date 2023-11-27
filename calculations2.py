from random import randint

class Ship:
    def __init__(self):
        self.damage = randint(1,10)
        self.health = randint(50,100)

class Player:
    pass

class Calculations:
    def __init__(self, ship1: Ship, ship2: Ship):
        self.ship1 = ship1
        self.ship2 = ship2

    def calculation(self):
        print("начальное здоровье: ", self.ship1.health, "против ", self.ship2.health)
        while self.ship1.health >= 0 and self.ship2.health >= 0:
            self.ship1.health -= self.ship2.damage
            self.ship2.health -= self.ship1.damage
            print(self.ship1.health, self.ship2.health) # проверка кто быстрее погибает по раундам

        print("конечное здоровье: ", self.ship1.health, "против ", self.ship2.health) # выясняем победителя

def main():
    ship1 = Ship()
    ship2 = Ship()
    calculation = Calculations(ship1, ship2)
    calculation.calculation()



if __name__ == "__main__":
    main()
