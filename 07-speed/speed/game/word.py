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
        return self._points

    def get_word(self):
        text = random.choice(open("words.txt").readline())
        self.set_text(text)
    
    def reset(self):
        self._position = Point(constants.MAX_X - 1, random.randint(25, 374))
        self._velocity = Point(0, -5)
        self._width = constants.DEFAULT_SQUARE_LENGTH
        self._height = constants.DEFAULT_SQUARE_LENGTH

