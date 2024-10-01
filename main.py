#"Битва героев" игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health = other.health - self.attack_power
        #атакует другого героя (other), отнимая здоровье в размере своей силы удара

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        #возвращает True, если здоровье героя больше 0, иначе False

class Game:
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        print(f"силы {self.player.name}а: {self.player.health}, силы {self.computer.name}а: {self.computer.health}")
        input("Нажмите Enter для начала игры.")
        while self.player.is_alive and self.computer.is_alive():
            self.computer.attack(self.player)
            print(f"силы {self.player.name}а: {self.player.health}, силы {self.computer.name}а: {self.computer.health}")
            print(self.player.is_alive())
            self.player.attack(self.computer)
            print(f"силы {self.player.name}а: {self.player.health}, силы {self.computer.name}а: {self.computer.health}")
            print(self.computer.is_alive())

#начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.


viktor = Hero("Виктор")
nazgul = Hero("Назгул")

game = Game(viktor, nazgul)
game.start()
