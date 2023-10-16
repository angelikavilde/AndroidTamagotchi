from datetime import datetime


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
        self.alive = True
        self.lifespan_left = 10
        self.difficulty = difficulty
        self.poop_level = 0
        self.hunger = 0
        self.asleep = {"time": None, "status": False}
        self.sadness_level = 0


    def reset_lifespan(self):
        """"""
        self.lifespan_left = 10

    def feed(self):
        """"""
        self.reset_lifespan()

    def play(self):
        """"""
        if self.difficulty == "hard":
            self.reset_lifespan()

    def clean(self):
        """"""
        if self.poop_level:
            self.poop_level = 0
        else:
            raise NoPoopToClean

    def pet(self):
        """"""
        if self.difficulty == "hard":
            self.reset_lifespan()

    def sleep(self):
        """"""
        self.asleep["status"] = True
        self.asleep["time"] = datetime.now()
        if self.difficulty != "easy":
            self.reset_lifespan()