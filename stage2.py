import game_framework
from player_object import Player
from monster_object import Monster2
from block import Block2
import stage3
from pico2d import *

name = "Stage2"

globalevents = None
player = None
monster2s = None
blocks = None

def enter():
    global player, stageimage, backimage1, backimage2, monster2s, blocks
    open_canvas(sync = True)
    player = Player()
    monster2s = [Monster2(100, 130)]
    blocks = [Block2(200, 140), Block2(400, 140), Block2(600, 140), Block2(300, 280), Block2(500, 280), Block2(200, 420), Block2(400, 420), Block2(600, 420)]
    backimage1 = load_image('background2_1.png')
    backimage2 = load_image('background2_2.png')
    stageimage = load_image('stage2.png')

def exit():
    global player, stageimage, backimage1, backimage2, monster2s, blocks
    del(monster2s)
    del(player)
    del(blocks)
    del(stageimage)
    del(backimage1)
    del(backimage2)


def update():
    player.update()
    for monster2 in monster2s:
        monster2.update()

def draw():
    clear_canvas()
    backimage1.draw(400, 300)
    backimage2.draw(400, 300)
    stageimage.draw(400, 300)

    player.draw()

    for block in blocks:
        block.draw()

    for monster2 in monster2s:
        monster2.draw()

    update_canvas()

def handle_events():
    global globalevents
    globalevents = get_events()
    print(globalevents)
    for event in globalevents:
        player.handle_event(event)
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_a:
                game_framework.change_state(stage3)
        elif event.type == SDL_QUIT:
            game_framework.quit()