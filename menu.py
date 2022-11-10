import pygame

pygame.font.init()
pygame.font.get_init()


class Menu:
    def __init__(self):
        self.maxScore = 0

        self.text_surface = None
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        self.font2 = pygame.font.SysFont('freesanbold.ttf', 40)
        self.font3 = pygame.font.SysFont('freesanbold.ttf', 35)

        self.text1 = self.font1.render('Main menu', True, (0, 0, 0))
        self.text2 = self.font2.render('Нажмите на пробел для того что бы начать игру', True, (0, 0, 0))
        self.text3 = self.font3.render('Нажмите на цифру 1 или 2 для того что бы выбрать игрока', True, (0, 0, 0))
        self.text4 = self.font3.render('Ваши лучший результат - ' + str(self.maxScore), True, (0, 0, 0))

        self.textRect1 = self.text1.get_rect()
        self.textRect2 = self.text2.get_rect()
        self.textRect3 = self.text3.get_rect()
        self.textRect4 = self.text4.get_rect()

        self.textRect1.center = (500, 100)
        self.textRect2.center = (500, 150)
        self.textRect3.center = (500, 200)
        self.textRect4.center = (1000, 350)


    def output(self, screen):
        screen.blit(self.text1, self.textRect1)
        screen.blit(self.text2, self.textRect2)
        screen.blit(self.text3, self.textRect3)
        screen.blit(self.text4, self.textRect4)

