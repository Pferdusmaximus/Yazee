class Player:
    def __init__(self, score,name, dices):
        self.score = score
        self.name = name
        self.dices = dices

import pygame

def ask_player_count(window, font):
    selected = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_6:
                    selected = event.key - pygame.K_0
                elif event.key == pygame.K_RETURN and selected is not None:
                    return selected

        window.fill((30, 40, 55))
        title = font.render("Waehle Spielerzahl (1-6)", True, (240, 240, 240))
        window.blit(title, (120, 120))

        current = f"Auswahl: {selected}" if selected is not None else "Auswahl: -"
        txt = font.render(current, True, (180, 255, 180))
        window.blit(txt, (120, 190))

        hint = font.render("Enter zum Starten", True, (220, 220, 220))
        window.blit(hint, (120, 260))

        pygame.display.flip()


def update_score():
    pass

def playing():
    pass

def selection():
    pass
