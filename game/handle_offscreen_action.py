from game import constants, wall_physics
from game import audio_service
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
import pyray
import sys
import time

class HandleOffscreenActions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, wall_physics):
        super().__init__()
        self._wall_physics = wall_physics

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        ball = cast["ball"][0]
        right_side = cast["right_wall"][0]
        left_side = cast["left_wall"][0]
        bottem_side = cast["bottem_wall"][0]
        switch_direction = ball.get_velocity()
        location = ball.get_position()
        new_x = switch_direction.get_x()
        new_y = switch_direction.get_y()
        game_over = location.get_y()
        if self._wall_physics.is_collision(right_side, ball):
            ball.set_velocity(Point(new_x * -1, new_y))
        if self._wall_physics.is_collision(left_side, ball):
            ball.set_velocity(Point(new_x * -1, new_y))
        if self._wall_physics.is_collision(bottem_side, ball):
            ball.set_velocity(Point(new_x, new_y * -1))
        if int(game_over) > constants.MAX_Y - 45:
            ball.set_velocity(Point(0, 0))
            audio_service.play_sound(constants.SOUND_OVER)
            time.sleep(4)
            sys.exit()
