import game_framework
from player_object import Player
from monster_object import Monster1
from block import Block1
import stage2
from pico2d import *
from collision import *

name = "Stage1"

globalevents = None
player = None
monster1s = None
blocks = None

def enter():
    global player, backimage, stageimage, monster1s, blocks
    open_canvas(sync = True)
    player = Player()
    monster1s = [Monster1(150, 170), Monster1(500, 170), Monster1(300, 310), Monster1(150, 450), Monster1(500, 450)]
    blocks = [Block1(250, 140), Block1(600, 140), Block1(400, 280), Block1(250, 420), Block1(600, 420)]
    backimage = load_image('background1.png')
    stageimage = load_image('stage1.png')

def exit():
    global player, backimage, stageimage, monster1s, blocks
    del(player)
    del(monster1s)
    del(backimage)
    del(stageimage)
    del(blocks)

def update():
    player.update()
    for monster1 in monster1s:
        monster1.update()

    for block in blocks:
        if collide(player, block):
            player.stop()

def draw():
    clear_canvas()
    backimage.draw(400, 300)
    stageimage.draw(400, 300)

    for block in blocks:
        block.draw()

    for monster1 in monster1s:
        monster1.draw()

    for block in blocks:
        block.draw_bb()

    player.draw()

    update_canvas()

def handle_events():
    global globalevents
    globalevents = get_events()
    for event in globalevents:
        player.handle_event(event)
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_a:
                game_framework.change_state(stage2)
        elif event.type == SDL_QUIT:
            game_framework.quit()