from pico2d import *

class Block1:
    def __init__(self, x, y):
        self.image = load_image('block1_211x35.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 105.5, self.y + 5, self.x + 105, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Block2:
    def __init__(self, x, y):
        self.image = load_image('block2_90x35.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 45, self.y + 5, self.x + 45, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Block3:
    def __init__(self, x, y, Width):
        self.x, self.y = x, y
        self.W= Width

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.W, self.y + 5, self.x + self.W, self.y + 5

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
