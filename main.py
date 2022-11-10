import random
import pygame
import sys
from viewPlayer import Player
from menu import Menu
from textScore import Score
from WorkDatabase import Database

pygame.init()
W = 1200
H = 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Jumpmen")


def run():
    Db = Database
    scoregame = 0
    menus = Menu()
    random.seed(20)
    randObj1 = random.randint(100, 300)
    random.seed(2)
    randObj2 = random.randint(450, 600)
    random.seed(10)
    randObj3 = random.randint(650, 800)

    positionPlayer = 0
    closeMain = False
    playerSkin = "1"

    runloop = True

    jumpPlayer = 478
    jumpPlayerPress = 420
    while runloop:

        player = Player(screen, positionPlayer, jumpPlayer, playerSkin)
        playerCorX = player.cordinateX()
        startPosY = jumpPlayer + 41.5 == 520;

        if playerCorX == randObj1 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0
        elif playerCorX == randObj1 + 10 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0
        elif playerCorX == randObj2 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0
        elif playerCorX == randObj2 + 10 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0
        elif playerCorX == randObj3 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0
        elif playerCorX == randObj3 + 10 and startPosY:
            Db.inputData(scoregame)
            closeMain = False
            scoregame = 0
            positionPlayer = 0

        if 420 <= jumpPlayer <= 478:
            jumpPlayer += 0.5

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    closeMain = True

                if not closeMain:
                    if event.key == pygame.K_1:
                        playerSkin = "1"
                    if event.key == pygame.K_2:
                        playerSkin = "2"

                if closeMain:
                    if event.key == pygame.K_d:
                        positionPlayer += 20
                    if event.key == pygame.K_a:
                        positionPlayer -= 20
                    if event.key == pygame.K_w and jumpPlayer == 478.5:
                        jumpPlayer = jumpPlayerPress

            if event.type == pygame.QUIT:
                sys.exit()

        if not closeMain:
            menus.output(screen)

        if closeMain:

            score = Score(str(scoregame))
            score.output(screen)
            if scoregame > 0:
                positionPlayer += 0.5 * scoregame
            else: positionPlayer += 0.5

            if positionPlayer >= W:
                scoregame += 1
                positionPlayer = 0
                randObj1 = random.randint(200, 800)
                randObj2 = random.randint(200, 800)
                randObj3 = random.randint(200, 800)


            pygame.draw.line(screen, (0, 0, 0),
                             [randObj1, 520],
                             [randObj1 + 10, 520], 20)
            pygame.draw.line(screen, (0, 0, 0),
                             [randObj2, 520],
                             [randObj2 + 10, 520], 20)
            pygame.draw.line(screen, (0, 0, 0),
                             [randObj3, 520],
                             [randObj3 + 10, 520], 20)
            pygame.draw.line(screen, (255, 0, 0),
                             [0,   528],
                             [W, 528], 9)

        player.output(closeMain)
        pygame.display.update()
        pygame.display.flip()


run()
