import random
import os
import sys
import time
from game import constants
from game import control_actors_actios
from game.director import Director
from game.move_actors_action import MoveActorsAction
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.wall_physics import WallPhysics
from game.audio_service import AudioService
from game.brick import Brick
from game.paddle import Paddle
from game.ball import Ball
from game.handle_offscreen_action import HandleOffscreenActions
from game.handle_sprite_collisions import HandleSpriteCollisions
from game.control_actors_actios import ControlActorsAction
from game.right_wall import RightWall
from game.left_wall import LeftWall
from game.bottem_wall import BottemWall


# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    x = [10, 85, 160, 235, 310, 385, 460, 535, 610, 685, 760]
    y = [20, 70, 120, 170, 220]
    locations = []
    for i in range(len(x)):
        for j in range(len(y)):
           position =  Point(x[i], y[j])
           brick = Brick()
           brick.set_position(position)
           locations.append(brick)

    cast["bricks"] = locations
    # TODO: Create bricks here and add them to the list
    x = int(constants.MAX_X / 3 * 2)
    y = int(constants.MAX_Y / 4 * 2)
    position = Point(x, y)
    ball = Ball()
    ball.set_position(position)
    ball.set_velocity(Point(int(constants.BALL_DX), int(constants.BALL_DY)))
    cast["ball"] = [ball]
    # TODO: Create a ball here and add it to the list

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 50)
    position = Point(x, y)
    paddle = Paddle()
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    right_wall = RightWall()
    left_wall = LeftWall()
    bottem_wall = BottemWall()
    cast["right_wall"] = [right_wall]
    cast["left_wall"] = [left_wall]
    cast["bottem_wall"] = [bottem_wall]
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    wall_physics = WallPhysics()
    audio_service = AudioService()
    move_actors = MoveActorsAction()

    draw_actors_action = DrawActorsAction(output_service)
    handle_offscreen_collisions = HandleOffscreenActions(wall_physics)
    control_actors_action = ControlActorsAction(input_service)
    handle_sprite_collisions = HandleSpriteCollisions(physics_service)


    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors, handle_offscreen_collisions, handle_sprite_collisions]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter")  #There was a semi-colon here not sure if I accidently added it or not.
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()



if __name__ == "__main__":
    main()
