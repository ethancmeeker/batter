from game.actor import Actor
from game.point import Point
from game import constants

class Brick(Actor):
    def __init__(self):
        super().__init__() 
        self.set_image(constants.IMAGE_BRICK)
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
