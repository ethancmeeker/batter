from game.actor import Actor
from game.point import Point
from game import constants

class BottemWall(Actor):
    def __init__(self):
        super().__init__() 
        self.set_width(constants.MAX_X)
        self.set_height(1)
        self.set_position(Point(0, 10))