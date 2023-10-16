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


class Pet:
    """"""

    def __init__ (self, name, difficulty):

        self.name = name
        self.lifespan_left = 10
        self.difficulty = difficulty
        self.poop_level = 0
        self.hunger_level = 0
        self.asleep = {"time": None, "status": False}
        self.sadness_level = 0
        self.tiredness_level = 0


    def check_if_asleep(self):
        """"""
        if self.asleep["status"]:
            raise PetAsleep

    def reset_lifespan(self, time_added: int):
        """"""
        self.lifespan_left = 10

    def feed(self):
        """"""
        self.reset_lifespan()

    def play(self):
        """"""
        self.check_if_asleep()
        if self.difficulty == "hard":
            if self.sadness_level > 0:
                self.sadness_level -= 1
                self.reset_lifespan(0.1)

    def clean(self):
        """"""
        if self.poop_level:
            self.poop_level -= 1
        else:
            raise NoPoopToClean

    def pet(self):
        """"""
        self.check_if_asleep()
        if self.difficulty == "hard":
            if self.sadness_level > 0:
                self.sadness_level -= 1
                self.reset_lifespan(0.1)

    def sleep(self):
        """"""
        if not self.asleep["status"]:
            self.asleep["status"] = True
            self.asleep["time"] = datetime.now()
        else:
            self.asleep["status"] = False
            self.asleep["time"] = None

    def check_if_alive(self) -> bool:
        """"""
        if self.difficulty != "easy":
            self_levels = [self.sadness_level,
                self.poop_level, self.tiredness_level]
            if any(level == 10 for level in self_levels):
                return False
        if not self.lifespan_left:
            return False
        if self.hunger_level == 10:
            return False
        return True

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


def level_change(easy: int, challenging: int, hard: int, difficulty: str) -> bool:
    """"""
    percentage_chance_of_increase = {"easy": easy,
        "challenging": challenging, "hard": hard}
    random_number = randint(0, 100)
    if percentage_chance_of_increase[difficulty] >= random_number:
        return True
    return False


if __name__ == "__main__":
    dog = Pet("test", "hard")