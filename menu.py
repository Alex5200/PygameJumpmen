import pygame
from WorkDatabase import Database

pygame.font.init()
pygame.font.get_init()


class Menu:
    def __init__(self):
        Db = Database()
        self.maxScore = Db.output_data()
        self.max_score_name = Db.output_max_score_name()

        self.text_surface = None
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        self.font2 = pygame.font.SysFont('freesanbold.ttf', 40)
        self.font3 = pygame.font.SysFont('freesanbold.ttf', 24)

        self.text1 = self.font1.render('Main menu', True, (0, 0, 0))
        self.text2 = self.font2.render('Нажмите на пробел для того что бы начать игру', True, (0, 0, 0))
        self.text3 = self.font3.render('Нажмите на цифру 1 или 2 для того что бы выбрать игрока', True, (0, 0, 0))
        self.text4 = self.font3.render('Ваш лучший результат - Имя: '+ str(self.max_score_name)+", очки: " + str(self.maxScore[0]), True, (0, 0, 0))
        self.text5 = self.font3.render('Топ 2 - ' + str(self.maxScore[2]), True, (0, 0, 0))
        self.text6 = self.font3.render('Топ 3 - ' + str(self.maxScore[3]), True, (0, 0, 0))
        self.text7 = self.font3.render('Топ 4 - ' + str(self.maxScore[4]), True, (0, 0, 0))
        self.text8 = self.font3.render('Топ 5 - ' + str(self.maxScore[5]), True, (0, 0, 0))

        self.textRect1 = self.text1.get_rect()
        self.textRect2 = self.text2.get_rect()
        self.textRect3 = self.text3.get_rect()
        self.textRect4 = self.text4.get_rect()
        self.textRect5 = self.text4.get_rect()
        self.textRect6 = self.text4.get_rect()
        self.textRect7 = self.text4.get_rect()
        self.textRect8 = self.text4.get_rect()


        self.textRect1.center = (500, 100)
        self.textRect2.center = (500, 150)
        self.textRect3.center = (500, 200)
        self.textRect4.center = (1000, 350)
        self.textRect5.center = (1000, 400)
        self.textRect6.center = (1000, 450)
        self.textRect7.center = (1000, 500)
        self.textRect8.center = (1000, 550)



    def output(self, screen):
        Db = Database()
        self.maxScore = Db.output_data()
        screen.blit(self.text1, self.textRect1)
        screen.blit(self.text2, self.textRect2)
        screen.blit(self.text3, self.textRect3)
        screen.blit(self.text4, self.textRect4)
        screen.blit(self.text5, self.textRect5)
        screen.blit(self.text6, self.textRect6)
        screen.blit(self.text7, self.textRect7)
        screen.blit(self.text8, self.textRect8)
