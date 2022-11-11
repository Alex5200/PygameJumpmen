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


def draw_line_obstacle(draw_random_obstacle1, draw_random_obstacle2, draw_random_obstacle3):
    pygame.draw.line(screen, (0, 0, 0),
                     [draw_random_obstacle1, 520],
                     [draw_random_obstacle1 + 10, 520], 20)
    pygame.draw.line(screen, (0, 0, 0),
                     [draw_random_obstacle2, 520],
                     [draw_random_obstacle2 + 10, 520], 20)
    pygame.draw.line(screen, (0, 0, 0),
                     [draw_random_obstacle3, 520],
                     [draw_random_obstacle3 + 10, 520], 20)
    pygame.draw.line(screen, (255, 0, 0),
                     [0, 528],
                     [W, 528], 9)


def random_object(minimal, maximum):
    random.seed(random.randint(minimal, maximum))
    return random.randint(minimal, maximum)


def run():
    db = Database()
    scoregame = 0
    menus = Menu()
    random_obstacle_1 = random_object(100, 400)
    random_obstacle_2 = random_object(500, 800)
    random_obstacle_3 = random_object(1000, 1200)

    position_player = 0
    close_main_menu = False
    player_skin = "1"

    def end_game(in_score_game):
        db.input_data(in_score_game)

    jump_player = 478
    jump_player_press = 420
    while True:

        player = Player(screen, position_player, jump_player, player_skin)
        player_coordinate_x = player.cordinateX()

        start_position_y = (jump_player + 43) >= 520
        print("J:" + str(jump_player + 41.8) + " state " + str(start_position_y))

        if player_coordinate_x == random_obstacle_1 \
                or player_coordinate_x == random_obstacle_2  \
                or player_coordinate_x == random_obstacle_3  \
                and start_position_y:
            end_game(scoregame)
            close_main_menu = False
            scoregame = 0
            position_player = 0
            print("O1 " + str(random_obstacle_1) + " O2 " + str(random_obstacle_2) + " O3 " + str(random_obstacle_3))
            print("X:" + str(player_coordinate_x))



        if 420 <= jump_player <= 478:
            jump_player += 0.25

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    close_main_menu = True

                if not close_main_menu:
                    if event.key == pygame.K_1:
                        player_skin = "1"
                    if event.key == pygame.K_2:
                        player_skin = "2"

                if close_main_menu:
                    if event.key == pygame.K_d:
                        position_player += 20
                    if event.key == pygame.K_a:
                        position_player -= 20
                    if event.key == pygame.K_w and jump_player == 478.25:
                        jump_player = jump_player_press

            if event.type == pygame.QUIT:
                sys.exit()

        if not close_main_menu:
            menus.output(screen)

        if close_main_menu:

            score = Score(str(scoregame))
            score.output(screen)
            if scoregame > 0:
                position_player += 0.7 * scoregame
            else:
                position_player += 0.7

            if position_player >= W:
                scoregame += 1
                position_player = 0
                random_obstacle_1 = random_object(100, 400)
                random_obstacle_2 = random_object(500, 800)
                random_obstacle_3 = random_object(1000, 1200)

            draw_line_obstacle(random_obstacle_1, random_obstacle_2, random_obstacle_3)

        player.output(close_main_menu)
        pygame.display.update()
        pygame.display.flip()


run()
