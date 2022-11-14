import pygame
import pygame.font
import pygame.draw

class InputBox:

    def display_box(screen, message):
        font_object = pygame.font.Font(None, 24)
        W = 200
        H = 300
        pygame.draw.rect(screen, (255, 255, 255),(W,H,200, 20), 0)
        pygame.draw.rect(screen, (0, 0, 0),(W - 2,H - 2,204, 24), 1)
        if len(message) != 0:
            screen.blit(font_object.render(message, 1, (0, 0, 0)),(W,H))
