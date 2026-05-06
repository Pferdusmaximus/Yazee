import pygame, player, game, dice, cup, scorecard, rules

pygame.init()
pygame.init()
window = pygame.display.set_mode((1200,700))
sc = scorecard.Scorecard()

window.fill((74,154,69))
sc.draw(window)            # ← Instanz-Methode aufrufen
# ... zeichne würfel etc.
spieler = []
dice_list = []
for i in range(5):
    würfel = dice.Dice(
        colour="white",
        value = i+1,
        position=(700 + i*70, 100),
        size=(50, 50)
    )
    dice_list.append(würfel)

# Zeichnen:
for würfel in dice_list:
    würfel.draw(window)
pygame.display.flip()

running = True
while running == True:
    running = game.quit()

pygame.quit()