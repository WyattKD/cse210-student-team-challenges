import random
import time
from game import constants
from game.actor import Actor
from game.point import Point

<<<<<<< HEAD

=======
>>>>>>> ff46d4c616f16f110eae0d8fecec875b4c3393a2
class Word(Actor):

    def __init__(self):
        self.reset()
        self._position = Point(constants.MAX_X - 1, random.randint(25, 374))
        self._velocity = Point(0, -5)
        self._width = constants.DEFAULT_SQUARE_LENGTH
        self._height = constants.DEFAULT_SQUARE_LENGTH
    
    def get_points(self):
        return self._points

    def get_word(self, text):
        text = random.choice(open("words.txt").readline())
        self.set_text(text)
    
    def reset(self):
        self._points = 4
        x = random.randint(1, 599)
        y = random.randint(1, 399)
        position = Point(x, y)
        self.set_position(position)
        self.set_text(f"{self._points}")

