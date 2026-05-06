import player
import pygame

class Game:
    def __init__(self,players, count_turns, window):
        self.player_list = list[player.Player[players]]
        self.count_turns = count_turns
        self.window = window

def game_won():
    pass

def play_turn():
    pass

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True