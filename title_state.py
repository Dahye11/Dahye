import game_framework
from pico2d import *
import stage1

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                game_framework.change_state(stage1)
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass






