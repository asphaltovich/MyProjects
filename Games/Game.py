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
    direction = input_command.strip().lower()
    if direction in current_location.exits:
        return current_location.exits[direction]
    else:
        print("Невозможно идти в это направление.")
        return current_location

def handle_take(player, current_location, input_command):
    item_name = input_command.strip().lower()
    for item in current_location.items:
        if item.lower() == item_name:
            player.add_item(item)
            current_location.items.remove(item)
            print(f"Вы взяли {item}.")
            return
    print(f"Здесь нет предмета {item_name}.")

def handle_drop(player, current_location, input_command):
    item_name = input_command.strip().lower()
    for item in player.inventory:
        if item.lower() == item_name:
            player.remove_item(item)
            current_location.items.append(item)
            print(f"Вы положили {item} в локацию.")
            return
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

# Новая функция для перемещения в любую локацию по названию
def handle_move_to_location(current_location, all_locations, input_command):
    location_name = input_command.strip().lower()
    for loc in all_locations:
        if loc.name.lower() == location_name:
            return loc
    print(f"Локация '{input_command}' не найдена.")
    return current_location

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

# Все локации для поиска
all_locations = [start, forest, cave, treasure_room]

# Игра
player_name = input("Введите ваше имя: ")
player = Player(player_name)
current_location = start
game_over = False
won = False

while not game_over:
    command = input("Введите команду (можно несколько сразу): ").lower()
    parts = command.split()

    # Обработка команды "перейти [название]"
    if parts and parts[0] == "перейти" and len(parts) > 1:
        target_name = ' '.join(parts[1:])
        current_location = handle_move_to_location(current_location, all_locations, target_name)
        continue

    i = 0
    comando_обнаружено = False
    while i < len(parts):
        word = parts[i]
        # Обработка "иди"
        if word == "иди" and i + 1 < len(parts):
            direction = ' '.join(parts[i + 1:])
            current_location = handle_go(current_location, direction)
            comando_обнаружено = True
            break
        # Обработка "бери"
        elif word == "бери" and i + 1 < len(parts):
            item = ' '.join(parts[i + 1:])
            handle_take(player, current_location, item)
            comando_обнаружено = True
            break
        # Обработка "клади"
        elif word == "клади" and i + 1 < len(parts):
            item = ' '.join(parts[i + 1:])
            handle_drop(player, current_location, item)
            comando_обнаружено = True
            break
        # Обработка "биться"
        elif word == "биться":
            success = handle_fight(player, current_location)
            if not success:
                print("Игра окончена.")
                game_over = True
            comando_обнаружено = True
            break
        # Обработка "инфо"
        elif word == "инфо":
            handle_info(player, current_location)
            comando_обнаружено = True
            break
        # Обработка "выход"
        elif word == "выход":
            print("Вы вышли из игры.")
            game_over = True
            comando_обнаружено = True
            break
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
