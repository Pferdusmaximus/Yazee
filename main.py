import pygame, player, game, dice, cup, scorecard, rules, random
pygame.init()
font = pygame.font.SysFont(None, 45)
window = pygame.display.set_mode((1200,700))
sc = scorecard.Scorecard()    

throw_warning = False     
spieler = []
dice_list = []
for i in range(5):
    würfel = dice.Dice(
        colour="white",
        value = 0,
        position=(700 + i*70, 100),
        size=(50, 50)
    )
    dice_list.append(würfel)

running = True
player_count = player.ask_player_count(window, font)
if player_count is None:
    pygame.quit()
    raise SystemExit

spieler = [f"Spieler{i+1}" for i in range(player_count)]
print("Spieler:", spieler)

while running:
    running = game.actions(dice_list, running)
    window.fill((74,154,69))
    sc.draw(window)

    need_roll = any(w.value == 0 for w in dice_list)
    if need_roll:
        if not throw_warning:
            info_text = font.render("Würfel mit leertaste", True, (169, 255, 197))
            window.blit(info_text, (700, 170))
    else:
        for w in dice_list:
            w.draw(window)
    pygame.display.flip()


pygame.quit()