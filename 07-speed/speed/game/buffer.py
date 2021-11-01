from game.actor import Actor
from game.point import Point

class Buffer(Actor):

    def __init__(self):
        super().__init__()
        position = Point(0, 370)
        self.set_position(position)
        self.set_text(f"")

    def update_buffer(self, letter):
        text = self.get_text()
        if letter != None:
            text += str(letter)
        self.set_text(text)