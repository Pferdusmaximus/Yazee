import pygame, player, game, dice, cup, scorecard, rules

pygame.init()
window = pygame.display.set_mode((1200, 700))

window.fill((74, 154, 69))  # Rot
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
