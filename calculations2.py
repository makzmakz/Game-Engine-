from random import randint

class Ship:
    def __init__(self):
        self.damage = randint(1,10)
        self.health = randint(50,100)

class Player:
    def __init__(self):
        self.ships = self.create_army()

    def create_army(self):
        ships = []
        for i in range(2):
            ship = Ship()
            ships.append(ship)
            print("здоровье ", i+1, "корабля ",  ships[i].health) #проверка доступа к объекту
        print("количество кораблей", len(ships)) #проверка количества элементов списка
        return ships

class Calculations:
    def __init__(self):
        self.players = self.create_players()

    def create_players(self):
        players = []
        for i in range(2):
            player = Player()
            players.append(player)
            print("информация по игроку", i + 1, ":")
            for j in range(2):
                print("здоровье ", j + 1, "корабля ", players[i].ships[j].health)  # проверка доступа к объекту
            print("количество кораблей", i+1, "-го игрока =", len(players[i].ships), "шт.")  # проверка количества элементов списка
        return players

    def calculation(self):
        print("начальная сводка:")
        print("начальное здоровье: ", self.players[0].ships[0].health, self.players[0].ships[1].health,
              "против ", self.players[1].ships[0].health, self.players[1].ships[1].health)

        """while (self.players[0].ships[0].health or self.players[0].ships[1].health) >= 0 \
                and (self.players[1].ships[0].health or self.players[1].ships[1].health) >= 0:

            # стрельба по случайному кораблю противника для первого игрока
            if (self.players[1].ships[0].health, self.players[1].ships[1].health) >= 0:
                random_enemy_damage_to_2 = randint(0,1)
            elif self.players[1].ships[0].health >= 0:
                random_enemy_damage_to_2 = 0
            else:
                random_enemy_damage_to_2 = 1

            # стрельба по случайному кораблю противника для второго игрока
            if (self.players[0].ships[0].health, self.players[0].ships[1].health) >= 0:
                random_enemy_damage_to_1 = randint(0, 1)
            elif self.players[0].ships[0].health >= 0:
                random_enemy_damage_to_1 = 0
            else:
                random_enemy_damage_to_1 = 1

            self.players[0].ships[random_enemy_damage_to_1] -= self.players[1].ships[0].damage - self.players[1].ships[1].damage
            self.ship2.health -= self.ship1.damage
            print(self.ship1.health, self.ship2.health) # проверка кто быстрее погибает по раундам """

        print("конечная сводка:")
        print("конечное здоровье: ", self.players[0].ships[0].health, self.players[0].ships[1].health,
              "против ", self.players[1].ships[0].health, self.players[1].ships[1].health) # выясняем победителя"""

def main():

    calculation = Calculations()
    calculation.calculation()



if __name__ == "__main__":
    main()
