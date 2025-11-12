rom abc import ABC, abstractmethod


class Character(ABC): # Абстрактный класс Character
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

# Дочерний класс Воин
class Warrior(Character): 
    def __init__(self, strength_level):
        self.strength_level = strength_level

    def attack(self):
        print(f"Воин атакует с силой {self.strength_level}!")

    def defend(self):
        print("Воин защищается щитом!")

# Дочерний класс Маг
class Mage(Character):
    def __init__(self, mana_level):
        self.mana_level = mana_level

    def attack(self):
        print(f"Маг вызывает магическую атаку с уровнем маны {self.mana_level}!")

    def defend(self):
        print("Маг использует магическую защиту!")

# Дочерний класс Лучник
class Archer(Character):
    def __init__(self, accuracy):
        self.accuracy = accuracy

    def attack(self):
        print(f"Лучник стреляет с точностью {self.accuracy}!")

    def defend(self):
        print("Лучник уклоняется от атаки!")


warrior = Warrior(strength_level=10)
mage = Mage(mana_level=100)
archer = Archer(accuracy=85)


warrior.attack()
warrior.defend()

mage.attack()
mage.defend()

archer.attack()
archer.defend()
