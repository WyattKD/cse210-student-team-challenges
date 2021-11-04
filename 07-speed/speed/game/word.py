import random
import time
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):

    def __init__(self):
        self.reset()
        self.get_word()
    
    def get_points(self):
        text = self.get_text
        points = len(text)
        return points

    def get_word(self):
        text = random.choice(open("words.txt").read().split())
        self.set_text(text)

    def is_off_screen(self):
        position = self.get_position()
        x = position.get_x()
        return x <= 0

    def starting_five(self):
        self._position = Point(random.randint(300, 599), random.randint(25, 374))

    def reset(self):
        self._position = Point(constants.MAX_X - 1, random.randint(25, 374))
        self._velocity = Point(-1, 0)
        self._width = constants.DEFAULT_SQUARE_LENGTH * 5
        self._height = constants.DEFAULT_SQUARE_LENGTH

