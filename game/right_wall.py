from game.actor import Actor
from game.point import Point
from game import constants

class RightWall(Actor):
    def __init__(self):
        super().__init__() 
        self.set_width(1)
        self.set_height(constants.MAX_Y)
        self.set_position(Point(constants.MAX_X - 2, 0))
