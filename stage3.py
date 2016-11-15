import game_framework
from player_object import Player
from monster_object import Monster1, Monster2
from block import Block3
from pico2d import *

name = "Stage3"

globalevents = None
player, monster1s, monster2s, blocks = None, None, None, None

def handle_events():
    global globalevents
    globalevents = get_events()
    for event in globalevents:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_QUIT:
            game_framework.quit()

def enter():
    global player, backimage, stageimage, monster1s, monster2s, blocks
    open_canvas()
    player = Player()
    blocks = [Block3(100,200,100)]
    monster1s = [Monster1(100, 300)]
    monster2s = [Monster2(300, 100)]
    backimage = load_image('background3.png')
    stageimage = load_image('stage3.png')

def exit():
    global player, backimage, stageimage, monster1s, monster2s, blcok
    del (player)
    del (monster1s)
    del (monster2s)
    del (blocks)
    del (backimage)
    del (stageimage)

def update():
    player.update(globalevents)
    for monster1 in monster1s:
        monster1.update(globalevents)
    for monster2 in monster2s:
        monster2.update(globalevents)
    delay(0.1)


def draw():
    clear_canvas()
    backimage.draw(400, 300)
    stageimage.draw(400, 300)
    player.draw()
    for block in blocks:
        block.draw()
    for monster1 in monster1s:
        monster1.draw()
    for monster2 in monster2s:
        monster2.draw()
    update_canvas()







