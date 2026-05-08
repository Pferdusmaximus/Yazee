import player
import pygame, random

class Game:
    def __init__(self,players, count_turns, window):
        self.player_list = list[player.Player[players]]
        self.count_turns = count_turns
        self.window = window

def game_won():
    pass

def play_turn():
    pass

def actions(dice_list, running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for würfel in dice_list:
                würfel.value = random.randint(1, 6)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            print(mouse_pos)
            for dices in dice_list:
                dices.value = random.randint(1, 6)
    return running