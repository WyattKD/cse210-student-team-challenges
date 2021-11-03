from game.actor import Actor
from game.point import Point
from game.constants import *

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        position = Point(0, MAX_Y - 30)
        self.set_position(position)
        self.set_text(f"")

    def update_buffer(self, letter):
        text = self.get_text()
        if letter != None:
            text += str(letter)
        self.set_text(text)

    def check_for_match(self, word):
        text = self.get_text()
        if word in text:
            self.set_text(f"")
            return True
        else:
            return False