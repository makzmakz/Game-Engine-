from random import randint

class Ship:
    def __init__(self):
        self.damage = randint(1,10)
        self.health = randint(50,100)

class Player:
    def __init__(self):
        self.ships = self.create_army()
        self.dead_ships = []
        self.total_ships = len(self.ships)

    def create_army(self):
        ships = []
        for i in range(2):
            ship = Ship()
            ships.append(ship)
            # print("здоровье ", i+1, "корабля ",  ships[i].health) #проверка доступа к объекту
        # print("количество кораблей", len(ships)) #проверка количества элементов списка
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
        # проверка здоровья для стрельбы по боеспособной цели противника
        # уничтоженные корабли сохраняются для статистики
        for player in self.players:
            for ship in player.ships:
                ship_counter = 0
                if ship.health < 1:
                    print("корабль", ship_counter + 1, "уничтожен")
                    player.ships.remove(ship)
                    player.dead_ships.append(ship)
                ship_counter += 1
                # print(ship.health) # проверка доступа
            # print(len(player.ships)) # проверка доступа

    # стрельба по случайному кораблю противника
    # алгоритм рассчитан на двух игроков
    # TO DO
    # попробовать сделать для любого числа игроков
    def shoot(self):
        # здоровье перед стрельбой
        for player in self.players:
            for ship in player.ships:
                print(ship.health)
        # стрельба
        player_counter = 0
        for player in self.players:
            print("статус игрока", player_counter + 2)
            #ship_counter = 0
            for ship in player.ships:
                # TO DO
                # отображение боя внутри раунда (через print) не работает как хотелось бы
                #print(self.players[player_counter + 1].ships[ship_counter].health, "hp корабля", ship_counter + 1, "в начале раунда")
                #print(self.players[player_counter + 1].ships[ship_counter + 1].health, "hp корабля", ship_counter + 2, "в начале раунда")
                self.players[player_counter + 1].ships[randint(0, len(self.players[player_counter + 1].ships))-1].health -= ship.damage
                #print(self.players[player_counter + 1].ships[ship_counter].health, "hp корабля", ship_counter+1, "в конце раунда")
                #print(self.players[player_counter + 1].ships[ship_counter+1].health, "hp корабля", ship_counter + 2, "в конце раунда")
            player_counter -= 1
        # здоровье после стрельбы
        for player in self.players:
            for ship in player.ships:
                print(ship.health)

    # TO DO
    # необходимо будет проверить логику цикла на производительность
    # нужно добавить индефикацию Игрока чтобы понять кто победил из исходного множества игроков
    def battle_cycle(self):
        # бой
        is_not_battle_over = True
        game_round = 0
        while is_not_battle_over:
            # если игрок теряет все корабли он проигрывает
            # если игроков становится меньше 2 игра заканчивается
            # мертвые игроки сохраняются для статистики
            print("игровой раунд №:", game_round + 1)
            # удаление подбитых кораблей
            self.check_on_is_ship_alive()
            # удаление проигравших
            for player in self.players:
                if len(player.ships) < 1:
                    self.players.remove(player)
                    self.dead_players.append(player)
            if len(self.players) < 2:
                # завершение игры после чего пойдет статистика
                break
            self.shoot()
            game_round += 1

            '''
            # TO DO
            # проверка кто быстрее погибает по раундам
            # статистика раунда
            print(self.players[0].ships[0].health, self.players[0].ships[1].health,
                  self.players[1].ships[0].health, self.players[1].ships[1].health)
            '''


    def calculation(self):
        self.state_of_battle(bool(1))
        self.battle_cycle()

        # TO DO
        # выясняем победителя (нужна индексация Player)
        # статистика игры
        self.state_of_battle(bool(0))


def main():
    calculation = Calculations()
    calculation.calculation()


if __name__ == "__main__":
    main()
