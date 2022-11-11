import pygame


class Player():
    def __init__(self, screen, x, y, player):
        self.screen = screen
        self.image = pygame.image.load('./img/img_players/player' + player + ".png")
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.image.convert()
        self.rect.x = x
        self.rect.y = y
        self.screen.fill((255, 255, 255))

    def output(self, player):
        if player:
            self.image = pygame.transform.scale(self.image, (50, 50))
        self.screen.blit(self.image, self.rect)

    def cordinateX(self):
        return self.rect.x

    def cordinateY(self):
        return self.rect.y
