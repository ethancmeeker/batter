from game.actor import Actor
import pyray

class WallPhysics:
    """
    Used for actions relating to Physics, such as determining collisions.
    """
    def __init__(self):
        pass

    def is_collision(self, first, second):
        """
        Returns true if the two items are currently intersecting.
        """
        x1 = first.get_position().get_x()
        y1 = first.get_position().get_y()
        width1 = first.get_width()
        height1 = first.get_height()

        rectangle1 = pyray.Rectangle(x1, y1, width1, height1)

        x2 = second.get_position().get_x()
        y2 = second.get_position().get_y()
        width2 = second.get_width()
        height2 = second.get_height()

        rectangle2 = pyray.Rectangle(x2, y2, width2, height2)

        return pyray.check_collision_recs(rectangle1, rectangle2)