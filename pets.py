""""""

from datetime import datetime
from random import randint


class NoPoopToClean(Exception):
    """"""
    def __init__(self, message="No poop to clean!"):
        super().__init__(message)


class PetAsleep(Exception):
    """"""
    def __init__(self, message="Cannot interact with a sleeping pet!"):
        super().__init__(message)


class UnwantedInteraction(Exception):
    """"""
    def __init__(self, message="Your pet does not want this interaction right now!"):
        super().__init__(message)


class Pet:
    """"""

    def __init__ (self, name, difficulty):

        self.name = name
        self.difficulty = difficulty
        self.poop_level = 0
        self.hunger_level = 0
        self.asleep = {"time": None, "status": False}
        self.sadness_level = 0
        self.tiredness_level = 0


    def interact(self):
        """"""
        check_if_asleep(self)
        if self.sadness_level > 0:
            if self.difficulty == "hard":
                if self.sadness_level > 0.5:
                    self.sadness_level -= 0.5
                else:
                    self.sadness_level = 0
            elif self.difficulty == "challenging":
                if self.sadness_level > 0.75:
                    self.sadness_level -= 0.75
                else:
                    self.sadness_level = 0
            else:
                if self.sadness_level > 1:
                    self.sadness_level -= 1
                else:
                    self.sadness_level = 0
        else:
            raise UnwantedInteraction

    def feed(self):
        """"""
        check_if_asleep(self)
        if self.hunger_level > 0:
            self.hunger_level -= 1
        else:
            raise UnwantedInteraction

    def play(self):
        self.interact()

    def clean(self):
        """"""
        if self.poop_level:
            self.poop_level -= 1
        else:
            raise NoPoopToClean

    def pet(self):
        """"""
        self.interact()

    def sleep(self):
        """"""
        if not self.asleep["status"]:
            self.asleep["status"] = True
            self.asleep["time"] = datetime.now()
        else:
            self.asleep["status"] = False
            self.asleep["time"] = None

    def poop(self):
        """"""
        if level_change(easy=25, challenging=50, hard=90, difficulty=self.difficulty):
            self.poop_level += 1

    def hunger(self):
        """"""
        if level_change(easy=30, challenging=60, hard=100, difficulty=self.difficulty):
            self.hunger_level += 1

    def boredom(self):
        """"""
        if level_change(easy=15, challenging=40, hard=80, difficulty=self.difficulty):
            self.sadness_level += 1

    def tiredness(self):
        """"""
        if level_change(easy=10, challenging=30, hard=60, difficulty=self.difficulty):
            self.tiredness_level += 1


def check_if_asleep(pet: Pet) -> None:
    """"""
    if pet.asleep["status"]:
        raise PetAsleep


def level_change(easy: int, challenging: int, hard: int, difficulty: str) -> bool:
    """"""
    percentage_chance_of_increase = {"easy": easy,
        "challenging": challenging, "hard": hard}
    random_number = randint(0, 100)
    if percentage_chance_of_increase[difficulty] >= random_number:
        return True
    return False


def check_if_alive(pet: Pet) -> bool:
    """"""
    self_levels = [pet.sadness_level,
            pet.poop_level, pet.tiredness_level]
    if pet.difficulty == "hard":
        if any(level == 10 for level in self_levels):
            return False
    if pet.difficulty == "challenging":
        if any(level == 20 for level in self_levels):
            return False
    if pet.hunger_level == 10:
        return False
    return True


if __name__ == "__main__":
    dog = Pet("test", "hard")
    # every hour:
    while (check_if_alive(dog)):
        dog.poop()
        dog.hunger()
        dog.boredom()
        dog.tiredness()