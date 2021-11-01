from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        position = Point(0, 370)
        self.set_position(position)
        self.set_text(f"")

    def print_letter(self, letter):
        if letter != None:
            print(letter)