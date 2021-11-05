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
        return x <= 1

    def screen_bounce(self):
        position = self.get_position()
        y = position.get_y()
        velocity = self.get_velocity()
        dx = velocity.get_x()
        dy = velocity.get_y() 
        if y <= 1 or y >= constants.MAX_Y - constants.DEFAULT_FONT_SIZE:
            dy *= -1
        self.set_velocity(Point(dx, dy))

    def starting_five(self):
        self._position = Point(random.randint(300, 599), random.randint(25, 374))

    def reset(self):
        self._position = Point(constants.MAX_X - 1, random.randint(25, 374))
        self._velocity = Point(random.randint(-2, -1), random.randint(-1, 1))
        self._width = constants.DEFAULT_SQUARE_LENGTH * 5
        self._height = constants.DEFAULT_SQUARE_LENGTH

