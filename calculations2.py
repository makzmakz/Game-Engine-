from random import randint

class Ship:
    def __init__(self):
        self.damage = randint(1,10)
        self.health = randint(50,100)

class Player:
    def __init__(self):
        self.ships = self.create_army()
        self.dead_ships = []

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
        self.dead_players = []

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

    def state_of_battle(self, state_battle_counter: bool):
        if state_battle_counter is True:
            print("начальная сводка:")
            print("начальное здоровье: ")
        else:
            print("конечная сводка:")
            print("конечное здоровье: ")
        player_counter = 0
        for player in self.players:
            if player_counter == 0:
                pass
            else:
                print("против ")
            ship_counter = 0
            print("игрок", player_counter + 1)
            for ship in player.ships:
                print("корабль", ship_counter + 1, ship.health)
                ship_counter += 1
            player_counter += 1

    def check_on_is_ship_alive(self):
        # необходимо сделать проверку здоровья для случайной стрельбы
        # уничтоженные корабли сохраняются для статистики
        for player in self.players:
            for ship in player.ships:
                ship_counter = 0
                if ship.health < 1:
                    print("корабль", ship_counter + 1, "уничтожен")
                    player.ships.remove(ship)
                    player.dead_ships.append(ship)
                ship_counter += 1
                print(ship.health) # проверка доступа
            print(len(player.ships)) # проверка доступа

    # TO DO
    # необходимо будет проверить логику цикла на производительность
    def battle_cycle(self):
        is_not_battle_over = True
        while is_not_battle_over:
            # если игрок теряет все корабли он проигрывает
            # если игроков становится меньше 2 игра заканчивается
            # мертвые игроки сохраняются для статистики
            for player in self.players:
                if len(player.ships) < 1:
                    self.players.remove(player)
                    self.dead_players.append(player)
            if len(self.players) < 2:
                is_not_battle_over = False

            # проверка здоровья
            self.check_on_is_ship_alive()

            # TO DO
            # стрельба по случайному кораблю противника для первого игрока
            if (self.players[1].ships[0].health, self.players[1].ships[1].health) >= 0:
                random_aim_on_enemy_by_1_player = randint(0, 1)
            elif self.players[1].ships[0].health >= 0:
                random_aim_on_enemy_by_1_player = 0
            else:
                random_aim_on_enemy_by_1_player = 1

            # TO DO
            # стрельба по случайному кораблю противника для второго игрока
            if (self.players[0].ships[0].health, self.players[0].ships[1].health) >= 0:
                random_aim_on_enemy_by_2_player = randint(0, 1)
            elif self.players[0].ships[0].health >= 0:
                random_aim_on_enemy_by_2_player = 0
            else:
                random_aim_on_enemy_by_2_player = 1

            # TO DO
            # попадание снаряда по цели
            self.players[0].ships[0].health -= self.players[1].ships[0].damage \
                                               + self.players[1].ships[1].damage
            self.players[0].ships[1].health -= self.players[1].ships[0].damage \
                                               + self.players[1].ships[1].damage
            self.players[1].ships[0].health -= self.players[0].ships[0].damage \
                                               + self.players[0].ships[1].damage
            self.players[1].ships[1].health -= self.players[0].ships[0].damage \
                                               + self.players[0].ships[1].damage

            # TO DO
            # проверка кто быстрее погибает по раундам
            # статистика раунда
            print(self.players[0].ships[0].health, self.players[0].ships[1].health,
                  self.players[1].ships[0].health, self.players[1].ships[1].health)


    def calculation(self):
        self.state_of_battle(bool(1))
        # self.battle_cycle()

        # TO DO
        # выясняем победителя
        # статистика игры
        self.state_of_battle(bool(0))


def main():
    calculation = Calculations()
    calculation.calculation()


if __name__ == "__main__":
    main()
