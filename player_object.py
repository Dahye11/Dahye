from pico2d import *
from game_framework import *

class Player:
    image = None
    MOVE, DIR, ATTACK, STAND, JUMP = False, False, False, True, False

    RIGHT_STAND, LEFT_STAND, RIGHT_ATTACK, LEFT_ATTACK, RIGHT_DIE, LEFT_DIE, RIGHT_WALK, LEFT_WALK = 0, 1, 2, 3, 4, 5, 6, 7

    def handle_left_die(self):
        pass

    def handle_left_walk(self):
        pass

    def handle_left_attack(self):
        pass

    def handle_left_stand(self):
        pass

    def handle_right_die(self):
        pass

    def handle_right_walk(self):
        pass

    def handle_right_attack(self):
        pass

    def handle_right_stand(self):
        pass

    handle_state = {
                LEFT_WALK : handle_left_walk,
                RIGHT_WALK : handle_right_walk,
                LEFT_DIE : handle_left_die,
                RIGHT_DIE : handle_right_die,
                LEFT_ATTACK : handle_left_attack,
                RIGHT_ATTACK : handle_right_attack,
                LEFT_STAND : handle_left_stand,
                RIGHT_STAND: handle_right_stand,
    }

    def update(self):
        if self.MOVE:
            if self.DIR:
                self.x -= 5
                self.state = self.LEFT_WALK
            else:
                self.x += 5
                self.state = self.RIGHT_WALK
            self.walk_frames = (self.walk_frames + 1) % 5

        if self.ATTACK:
            if self.DIR:
                self.state = self.LEFT_ATTACK
            else:
                self.state = self.RIGHT_ATTACK
            self.attack_frames = (self.attack_frames + 1) % 8

        if self.STAND:
            if self.DIR:
                self.state = self.LEFT_STAND
            else:
                self.state = self.RIGHT_STAND
            self.stand_frames = (self.stand_frames + 1) % 3

        if self.JUMP:
            if self.DIR:
                self.state = self.LEFT_WALK
            else:
                self.state = self.RIGHT_WALK
            self.y += self.jump/15
            self.jump -= self.down
            self.walk_frames = (self.walk_frames + 1) % 5

        if self.attack_frames == 7:
            self.ATTACK = False
            self.STAND = True
        self.handle_state[self.state](self)
        delay(0.04)

    def __init__(self):
        self.x, self.y = 70, 50
        self.walk_frames = 0
        self.die_frames = 0
        self.attack_frames = 0
        self.stand_frames = 0
        self.frame = 0
        self.state = self.RIGHT_STAND
        self.jump = 155
        self.down = 5
        if self.image == None:
            self.image = load_image('player.png')

    def draw(self):
        if self.state == self.LEFT_WALK:
            self.image.clip_draw(self.walk_frames * 54, self.state * 52, 54, 52, self.x, self.y)
        elif self.state == self.RIGHT_WALK:
            self.image.clip_draw(self.walk_frames * 54, self.state * 52, 54, 52, self.x, self.y)
        elif self.state == self.LEFT_ATTACK:
            self.image.clip_draw(self.attack_frames * 54, self.state * 52, 54, 50, self.x, self.y)
        elif self.state == self.RIGHT_ATTACK:
            self.image.clip_draw(self.attack_frames * 54, self.state * 52, 54, 50, self.x, self.y)
        elif self.state == self.LEFT_STAND:
            self.image.clip_draw(self.stand_frames * 54, self.state * 52, 54, 52, self.x, self.y)
        elif self.state == self.RIGHT_STAND:
            self.image.clip_draw(self.stand_frames * 54, self.state * 52, 54, 52, self.x, self.y)

    def get_bb(self):
        return self.x - 27, self.y - 26, self.x + 27, self.y + 26

    def stop(self):
        self.jump = 0

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.MOVE = True
            self.DIR = False
            self.STAND = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.MOVE = True
            self.DIR = True
            self.STAND = False
        elif (event.type, event.key) ==  (SDL_KEYUP, SDLK_RIGHT):
            self.MOVE = False
            self.DIR = False
            self.STAND = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.MOVE = False
            self.DIR = True
            self.STAND = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.ATTACK = True
            self.STAND = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.JUMP = True
            self.jump = 155
