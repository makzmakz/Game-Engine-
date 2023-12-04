from random import randint

class Ship:
    def __init__(self, index_number, min_damage, max_damage, min_hp, max_hp): # TO DO чтобы проверить наверняка движок нужно прогнать неслько разных симуляций
        self.damage = randint(min_damage, max_damage)
        self.health = randint(min_hp, max_hp)
        self.index_number = index_number

class Player:
    def __init__(self, index_number):
        self.ships = self.create_army()
        self.dead_ships = []
        self.total_ships = len(self.ships)
        self.index_number = index_number

    def create_army(self):
        ships = []
        for index_number in range(2):
            min_damage = randint(1,4)
            max_damage = randint(5,10)
            min_hp = randint(5,10)
            max_hp = randint(15,20)
            ship = Ship(index_number, min_damage, max_damage, min_hp, max_hp)
            ships.append(ship)
        return ships

class Calculations:
    def __init__(self):
        self.players = self.create_players()
        self.dead_players = []
        self.information()

    def create_players(self):
        players = []
        for index_number in range(2):
            player = Player(index_number)
            players.append(player)
        return players

    def information(self):
        # это начальная информация об игроках при их создании
        # это статистика раунда (до и после):
        # перед стрельбой в начале каждого раунда
        # и
        # после стрельбы в конце каждого раунда
        # все 3 фичи отображаются по одной функции
        # TO DO
        # в конце раунда подбитые корабли учитываются как неподбитые
        for player in self.players:
            print("информация по игроку", player.index_number + 1, ":")
            # TO DO
            # использую костыль == не знаю как обойти задачу перечисления удаляющихся объектов из списка
            # недееспособные корабли удаляются из списка дееспособных
            ship_index = 0
            for ship in player.ships:
                print("здоровье ", ship.index_number + 1, "корабля ", self.players[player.index_number].ships[ship_index].health)
                ship_index += 1
            print("количество кораблей", player.index_number + 1, "-го игрока =", len(self.players[player.index_number].ships), "шт.")

    # статистика начала и конца игры
    def state_of_battle(self, state_battle_counter: bool):
        if state_battle_counter is True:
            print("начальная сводка:")
            print("начальное здоровье: ")
        else:
            print("конечная сводка:")
            self.is_any_victorier()
        for player in self.players:
            if len(self.players) >= 2:
                print("игрок", player.index_number + 1)
            for ship in player.ships:
                print("корабль", ship.index_number + 1, ship.health)
            if player.index_number < len(self.players)-1:
                print("против ")

    def is_any_victorier(self):
        if len(self.players) == 1: # TO DO костыльное условие
            print("игрок", self.players[0].index_number + 1, "победил")
            print("конечное здоровье:")
        else:
            print("все игроки мертвы == нет победителя")

    def check_on_is_ship_alive(self):
        # проверка здоровья для стрельбы по боеспособной цели противника
        # уничтоженные корабли сохраняются для статистики
        for player in self.players:
            for ship in player.ships:
                if ship.health < 1:
                    print("игрок", player.index_number + 1, "корабль", ship.index_number + 1, "уничтожен")
            # TO DO
            # костыль удаляет несколько кораблей за раунд
            # внутренний цикл удаляет по одному кораблю за раунд
            for i in range(2):
                for ship in player.ships:
                    if ship.health < 1:
                        player.ships.remove(ship)
                        player.dead_ships.append(ship)

    def check_on_is_player_alive(self):
        for player in self.players:
            if len(player.ships) < 1:
                print("игрок", player.index_number + 1, "проиграл")
        # TO DO
        # костыль удаляет нескольких игроков за раунд
        # внутренний цикл удаляет по одному игроку за раунд
        for i in range(2):
            for player in self.players:
                if len(player.ships) < 1:
                    self.players.remove(player)
                    self.dead_players.append(player)

    # стрельба по случайному кораблю противника
    # алгоритм рассчитан на двух игроков
    # 1ый бьет по 2му, 2ой по 1ому, 3ий будет бить по самому себе (3 игрока) или по 4му, 4ый будет бить по 3му
    # TO DO
    # попробовать сделать для любого числа игроков
    def shoot(self):
        player_counter = 0
        for player in self.players:
            for ship in player.ships:
                # TO DO
                # отображение боя внутри раунда (через print) не работает как хотелось бы
                # стоит ли отображать статистику до и после хода каждого корабля?
                print("игрок", player.index_number + 1, "корабль", ship.index_number + 1, "целится")
                self.information()
                self.players[player_counter + 1].ships[randint(0, len(self.players[player_counter + 1].ships))-1].health -= ship.damage
                print("игрок", player.index_number + 1, "корабль", ship.index_number + 1, " выстрелил")
                self.information()
            player_counter -= 1

    # TO DO
    # проверить логику цикла на производительность
    def battle_cycle(self):
        # бой
        is_not_battle_over = True
        game_round = 0
        while is_not_battle_over:
            # если игрок теряет все корабли он проигрывает
            # если игроков становится меньше 2 игра заканчивается
            # мертвые игроки сохраняются для статистики
            print("игровой раунд №:", game_round + 1)
            # проверка 1
            # удаление подбитых кораблей
            self.check_on_is_ship_alive()
            # проверка 2
            # удаление проигравших игроков
            self.check_on_is_player_alive()
            # проверка 3
            # выход из цикла == завершение игры после чего пойдет итоговая статистика
            if len(self.players) < 2:
                break
            # статистика перед стрельбой в начале каждого раунда
            self.information()
            # механика боя
            self.shoot()
            # TO DO
            # статистика после стрельбы в конце каждого раунда
            # работает не корректно (читай описание логики функции)
            self.information()
            game_round += 1

    def calculation(self):
        self.state_of_battle(bool(1))
        self.battle_cycle()
        # TO DO
        # выясняем победителя
        # статистика игры
        self.state_of_battle(bool(0))


def main():
    for simulation in range(10):
        calculation = Calculations() # создаются игроки с армиями и начальная
        calculation.calculation()


if __name__ == "__main__":
    main()
