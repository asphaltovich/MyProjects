import random

# Базовый класс персонажа
class BaseCharacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        pass

# Класс игрока
class Player(BaseCharacter):
    def __init__(self, name):
        super().__init__(name, 100)
        self.inventory = []

    def attack(self):
        return random.randint(10, 20)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def has_item(self, item_name):
        return item_name in self.inventory

    def show_inventory(self):
        if self.inventory:
            print("Инвентарь:", ', '.join(self.inventory))
        else:
            print("Инвентарь пуст.")

# Класс врагов
class Enemy(BaseCharacter):
    def __init__(self, name, health, damage_range):
        super().__init__(name, health)
        self.damage_range = damage_range

    def attack(self):
        return random.randint(*self.damage_range)

# Гоблин — слабый враг
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Гоблин", 30, (5, 10))
    def attack(self):
        damage = super().attack()
        print(f"{self.name} атакует и наносит {damage} урона.")
        return damage

# Орк — сильный враг
class Orc(Enemy):
    def __init__(self):
        super().__init__("Орк", 50, (15, 25))
    def attack(self):
        damage = self.damage_range[1]
        print(f"{self.name} мощно атакует и наносит {damage} урона.")
        return damage

# Локация
class Location:
    def __init__(self, name, description, enemies=None, items=None, exits=None):
        self.name = name
        self.description = description
        self.enemies = enemies if enemies else []
        self.items = items if items else []
        self.exits = exits if exits else {}

    def describe(self):
        print(f"\n--- {self.name} ---")
        print(self.description)
        if self.items:
            print("Здесь есть предметы:", ', '.join(self.items))
        if self.enemies:
            print("Враги здесь:", ', '.join([enemy.name for enemy in self.enemies]))
        if self.exits:
            print("Доступные направления:", ', '.join(self.exits.keys()))

# Обработка команд
def handle_go(current_location, input_command):
    parts = input_command.split(" ", 1)
    if len(parts) < 2:
        print("Укажите направление для перемещения.")
        return current_location
    direction = parts[1]
    if direction in current_location.exits:
        return current_location.exits[direction]
    else:
        print("Невозможно идти в это направление.")
        return current_location

def handle_take(player, current_location, input_command):
    parts = input_command.split(" ", 1)
    if len(parts) < 2:
        print("Укажите предмет для взятия.")
        return
    item_name = parts[1]
    if item_name in current_location.items:
        player.add_item(item_name)
        current_location.items.remove(item_name)
        print(f"Вы взяли {item_name}.")
    else:
        print(f"Здесь нет предмета {item_name}.")

def handle_drop(player, current_location, input_command):
    parts = input_command.split(" ", 1)
    if len(parts) < 2:
        print("Укажите предмет для сброса.")
        return
    item_name = parts[1]
    if player.has_item(item_name):
        player.remove_item(item_name)
        current_location.items.append(item_name)
        print(f"Вы положили {item_name} в локацию.")
    else:
        print(f"У вас нет предмета {item_name}.")

def handle_fight(player, current_location):
    if not current_location.enemies:
        print("Здесь нет врагов для боя.")
        return False
    enemy = current_location.enemies[0]
    print(f"Начинается бой с {enemy.name}!")
    while enemy.health > 0 and player.health > 0:
        damage = player.attack()
        enemy.health -= damage
        print(f"Вы наносите {damage} урона {enemy.name}. Осталось здоровья: {enemy.health}")
        if enemy.health <= 0:
            print(f"{enemy.name} побежден!")
            current_location.enemies.remove(enemy)
            return True
        damage = enemy.attack()
        player.health -= damage
        print(f"{enemy.name} наносит вам {damage} урона. Ваше здоровье: {player.health}")
        if player.health <= 0:
            print("Вы проиграли...")
            return False
    return True

def handle_info(player, current_location):
    print(f"Здоровье: {player.health}")
    player.show_inventory()
    current_location.describe()

# Создаем локации и связываем их по названиям
start = Location(
    "Стартовая комната",
    "Вы в небольшой комнате. Перед вами дверь.",
    items=["старый ключ"]
)
forest = Location(
    "Лес",
    "Темный лес с деревьями вокруг. Тут тихо, но есть враги.",
    enemies=[Goblin()],
    items=["магический амулет"]
)
cave = Location(
    "Пещера",
    "Тёмная пещера. Внутри слышен шорох.",
    enemies=[Orc()],
    items=["золотой медальон"]
)
treasure_room = Location(
    "Комната сокровищ",
    "Здесь лежит главный предмет — драгоценный артефакт.",
    items=["магический артефакт"]
)

# Связь локаций по названиям
start.exits = {"лес": forest}
forest.exits = {"назад": start, "пещера": cave}
cave.exits = {"назад": forest, "комната сокровищ": treasure_room}
treasure_room.exits = {"назад": cave}

# Игра
player_name = input("Введите ваше имя: ")
player = Player(player_name)
current_location = start
game_over = False
won = False

while not game_over:
    command = input("Введите команду (можно несколько сразу): ").lower()

    # Разделяем команду на части по пробелам
    parts = command.split()
    i = 0
    while i < len(parts):
        word = parts[i]
        # Обработка команды "иди"
        if word == "иди" and i + 1 < len(parts):
            direction = ' '.join(parts[i + 1:])
            current_location = handle_go(current_location, "иди " + direction)
            break  # после перемещения дальше не идем
        # Обработка "бери"
        elif word == "бери" and i + 1 < len(parts):
            item = ' '.join(parts[i + 1:])
            handle_take(player, current_location, "бери " + item)
            break
        # Обработка "клади"
        elif word == "клади" and i + 1 < len(parts):
            item = ' '.join(parts[i + 1:])
            handle_drop(player, current_location, "клади " + item)
            break
        # Обработка "биться"
        elif word == "биться":
            success = handle_fight(player, current_location)
            if not success:
                print("Игра окончена.")
                game_over = True
            break
        # Обработка "инфо"
        elif word == "инфо":
            handle_info(player, current_location)
            break
        # Обработка "выход"
        elif word == "выход":
            print("Вы вышли из игры.")
            game_over = True
            break
        else:
            # Если команда не распознана, пропускаем
            pass
        i += 1

    # Проверка победы
    if ("магический артефакт" in player.inventory and current_location == treasure_room and not current_location.enemies):
        print("Поздравляем! Вы нашли главный артефакт и завершили игру победой!")
        won = True
        break

if won:
    print("Поздравляем! Вы выиграли игру.")
elif not game_over:
    print("Игра завершена.")
