import pygame
pygame.font.init()
pygame.font.get_init()

class Score():
    def __init__(self, score):
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        self.text1 = self.font1.render('Level: ' + score, True, (0, 0, 0))
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (500, 250)

    def output(self, screen):
        screen.blit(self.text1, self.textRect1)