import pygame

class Scorecard:
    CATEGORIES = [
      "Einser","Zweier","Dreier","Vierer","Fünfer","Sechser",
      "Dreierpasch","Viererpasch","Full House",
      "Kleine Straße","Große Straße","Kniffelchen","Chance"
    ]

    def __init__(self):
        self.scores = {c: None for c in self.CATEGORIES}
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 24)

    def set_score(self, category, value):
        if category in self.scores:
            self.scores[category] = int(value)

    def calculate(self):
        above = sum(v for k,v in self.scores.items() if k in self.CATEGORIES[:6] and v is not None)
        bonus = 35 if above >= 63 else 0
        lower = sum(v for k,v in self.scores.items() if k in self.CATEGORIES[6:] and v is not None)
        self.sum_above = above
        self.bonus = bonus
        self.sum_lower = lower
        self.sum_all = above + bonus + lower

    def draw(self, window, x=20, y=15, w=500, h=None, line_h=40):
        rows = len(self.CATEGORIES) + 3
        if h is None:
            h = rows * line_h
        else:
            line_h = h // rows

        pygame.draw.rect(window, (255,255,255), (x, y, w, h))
        pygame.draw.rect(window, (0,0,0), (x, y, w, h), 2)

        for i, cat in enumerate(self.CATEGORIES):
            val = "" if self.scores[cat] is None else str(self.scores[cat])
            txt = f"{cat}: {val}"
            surf = self.font.render(txt, True, (0,0,0))
            window.blit(surf, (x+8, y + i*line_h + 6))

        self.calculate()
        labels = [("Summe", self.sum_above), ("Bonus", self.bonus), ("Total", self.sum_all)]
        base = y + len(self.CATEGORIES)*line_h
        for j, (label, value) in enumerate(labels):
            surf = self.font.render(f"{label}: {value}", True, (0,0,0))
            window.blit(surf, (x+8, base + j*line_h + 6))