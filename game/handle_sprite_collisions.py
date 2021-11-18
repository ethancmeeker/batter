from game import constants, physics_service
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
import sys
import time
import random

class HandleSpriteCollisions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        ball = cast["ball"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]
        switch_direction = ball.get_velocity()
        new_x = switch_direction.get_x()
        new_y = switch_direction.get_y()
        x_possible = [14, 12, 10, 8, 6, 4, 2] 
        y_possible = [2, 4, 6, 8, 10, 12, 14] 
        '''
        This is what I did to make my code my unique. The game would play out exactly
        the same if I didn't do this every single time (unless you lost). This changes
        the direction it bounces off the paddle making things different.'''
        if self._physics_service.is_collision(paddle, ball):
            x_pick = random.choice(x_possible)
            x_spot = x_possible.index(x_pick)
            y_pick = y_possible[x_spot]
            if new_x < 0:
                ball.set_velocity(Point(x_pick, y_pick * -1))
                audio_service.play_sound(constants.SOUND_BOUNCE)
            if new_x > 0:
                ball.set_velocity(Point(x_pick * -1, y_pick * -1))
                audio_service.play_sound(constants.SOUND_BOUNCE)
        for brick in bricks:
            if self._physics_service.is_collision(brick, ball):
                bricks.remove(brick)
                ball.set_velocity(Point(new_x, new_y * -1))
                audio_service.play_sound(constants.SOUND_BOUNCE)
                if len(bricks) == 0:
                    ball.set_velocity(Point(0, 0))
                    audio_service.play_sound(constants.SOUND_WIN)
                    time.sleep(2)
                    print('YOU WIN')
                    sys.exit()


        