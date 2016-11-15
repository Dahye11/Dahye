import sys
sys.path.append('../LabsAll/Labs')

import game_framework
import random
from pico2d import *

start = None

class Monster1:
    image = None
    cnt = 0

    LEFT_RUN, RIGHT_RUN = 1, 0

    def handle_left_run(self):
        self.cnt += 1
        self.x -= 10
        self.run_frames += 1
        if self.cnt > 19:
            self.state = self.RIGHT_RUN
            self.cnt = 0



    def handle_right_run(self):
        self.cnt += 1
        self.x += 10
        self.run_frames -= 1
        if self.cnt > 19:
            self.state = self.LEFT_RUN
            self.cnt = 0


    handle_state = {
                LEFT_RUN : handle_left_run,
                RIGHT_RUN : handle_right_run,
    }

    def update(self):
        self.frame = (self.frame + 1) % 12
        self.handle_state[self.state](self)

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        if self.image == None:
            self.image = load_image('monster1.PNG')

    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 46, 40, 46, self.x, self.y)


class Monster2:
    image = None

    LEFT_RUN, RIGHT_RUN = 1, 0


    def handle_left_run(self):
        self.x -= 1
        self.run_frames += 1
        if self.x < 100:
            self.state = self.RIGHT_RUN
            self.x = 100



    def handle_right_run(self):
        self.x += 1
        self.run_frames -= 1
        if self.x > 700:
            self.state = self.LEFT_RUN
            self.x = 700


    handle_state = {
                LEFT_RUN : handle_left_run,
                RIGHT_RUN : handle_right_run,
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        self.dirY = 1
        if self.image == None:
            self.image = load_image('monster2.PNG')

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.state * 46, 50, 46, self.x, self.y)
