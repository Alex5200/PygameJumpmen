import pygame

class GameOver:
    def __init__(self, Score):
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        self.text1 = self.font1.render('Game Over ', True, (0, 0, 0))
        self.text2 = self.font1.render('Score: ' + Score, True, (0, 0, 0))

        self.textRect1 = self.text1.get_rect()
        self.textRect2 = self.text2.get_rect()

        self.textRect1.center = (500, 250)
        self.textRect2.center = (500, 200)