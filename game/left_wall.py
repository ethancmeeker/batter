from game.actor import Actor
from game.point import Point
from game import constants

class LeftWall(Actor):
    def __init__(self):
        super().__init__() 
        self.set_width(1)
        self.set_height(constants.MAX_Y)
        self.set_position(Point(2, 0))
