"""Script for creating a pet"""

from datetime import datetime, timedelta
from time import sleep
from random import randint


class NoPoopToClean(Exception):
    """Error class for attempting to clean non
    existent poop"""
    def __init__(self, message="No poop to clean!"):
        super().__init__(message)


class PetAsleep(Exception):
    """Error class for attempting to interact with an
    asleep pet"""
    def __init__(self, message="Cannot interact with a sleeping pet!"):
        super().__init__(message)


class UnwantedInteraction(Exception):
    """Error class for attempting to interact when interaction
    is unwanted by the pet"""
    def __init__(self, message="Your pet does not want this interaction right now!"):
        super().__init__(message)


class Pet:
    """Class for a pet"""

    def __init__ (self, name, difficulty):

        self.name = name
        self.difficulty = difficulty
        self.poop_level = 0
        self.hunger_level = 0
        self.asleep = {"time": None, "status": False}
        self.sadness_level = 0
        self.tiredness_level = 0


    def interact(self):
        """Function to interact with a pet
        that decreases its sadness level if the pet
        is awake"""
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
        """Function to feed to pet"""
        check_if_asleep(self)
        if self.hunger_level > 0:
            self.hunger_level -= 1
        else:
            raise UnwantedInteraction

    def play(self):
        """Function to play with a pet"""
        self.interact()

    def clean(self):
        """Function to clean pet's poop"""
        if self.poop_level:
            self.poop_level -= 1
        else:
            raise NoPoopToClean

    def pet(self):
        """Function to pet the pet"""
        self.interact()

    def change_sleep_state(self):
        """Function to change the sleep
        state of the pet"""
        if not self.asleep["status"]:
            if self.tiredness_level == 0:
                raise UnwantedInteraction
            self.asleep["status"] = True
            self.asleep["time"] = datetime.now()
        else:
            self.asleep["status"] = False
            self.asleep["time"] = None

    def poop(self):
        """Function for the pet to poop"""
        if not self.asleep["status"]:
            if level_change(easy=25, challenging=50, hard=90, difficulty=self.difficulty):
                self.poop_level += 1

    def hunger(self):
        """Function to change pet's hunger"""
        if not self.asleep["status"]:
            if level_change(easy=30, challenging=60, hard=100, difficulty=self.difficulty):
                self.hunger_level += 1
        else:
            if level_change(easy=10, challenging=20, hard=35, difficulty=self.difficulty):
                self.hunger_level += 1

    def boredom(self):
        """Function to raise boredom levels of the pet"""
        if not self.asleep["status"]:
            if level_change(easy=15, challenging=40, hard=80, difficulty=self.difficulty):
                self.sadness_level += 1
        else:
            if level_change(easy=5, challenging=10, hard=25, difficulty=self.difficulty):
                self.sadness_level += 1

    def tiredness(self):
        """Function to increase the tiredness levels of the pet"""
        if not self.asleep["status"]:
            if level_change(easy=10, challenging=30, hard=60, difficulty=self.difficulty):
                self.tiredness_level += 1


def sleep_tracker(pet: Pet) -> None:
    """Calculates the hours slept for the pet"""
    if pet.asleep["status"]:
        time_now = datetime.now()
        if time_now >= pet.asleep["time"] + timedelta(hours=1):
            pet.asleep["time"] = time_now
            pet.tiredness_level -= 1
        if pet.tiredness_level == 0:
            pet.change_sleep_state()
            #send notification about it being awake


def check_if_asleep(pet: Pet) -> None:
    """Raises an error if the pet is asleep"""
    if pet.asleep["status"]:
        raise PetAsleep


def level_change(easy: int, challenging: int, hard: int, difficulty: str) -> bool:
    """Verifies if the selected level should be raised for a pet's feeling"""
    percentage_chance_of_increase = {"easy": easy,
        "challenging": challenging, "hard": hard}
    random_number = randint(0, 100)
    if percentage_chance_of_increase[difficulty] >= random_number:
        return True
    return False


def check_if_alive(pet: Pet) -> bool:
    """Verifies if the pet is still alive"""
    self_levels = [pet.sadness_level,
            pet.poop_level, pet.tiredness_level]
    if pet.difficulty == "hard":
        if any(level == 16 for level in self_levels):
            return False
    if pet.difficulty == "challenging":
        if any(level == 24 for level in self_levels):
            return False
    if pet.hunger_level == 10:
        return False
    return True


if __name__ == "__main__":
    dog = Pet("test", "hard")
    while (check_if_alive(dog)):
        sleep(3600)
        dog.poop()
        dog.hunger()
        dog.boredom()
        dog.tiredness()
        sleep_tracker(dog)