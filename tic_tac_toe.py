import pygame
import sys
from pygame.locals import *
from Button import Button
import Constans
import time

pygame.init()

window_size = (Constans.WIN_WIDTH, Constans.WIN_HEIGHT)
window = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("TIC TAC TOE")

board = [[Button(0, 40), Button(220, 40), Button(440, 40)],
         [Button(0, 260), Button(220, 260), Button(440, 260)],
         [Button(0, 480), Button(220, 480), Button(440, 480)]]

FPS = 80
fpsClock = pygame.time.Clock()
font_obj = pygame.font.Font('freesansbold.ttf', 32)

Player = "player 2"


def draw():
    for row in board:
        for field in row:
            field.draw(window)


def player(player):
    if player == "player 1":
        Player = "player 2"
    if player == "player 2":
        Player = "player 1"
    return Player


def message(msg, color):
    font = pygame.font.Font('freesansbold.ttf', 60)
    mesg = font.render(msg, True, color)
    window.blit(mesg, [(Constans.WIN_WIDTH / 2) - 200, (Constans.WIN_HEIGHT / 2) - 30])


def winner():
    for row in range(len(board)):
        for field in range(len(board[row])):
            Constans.RED = (0, 0, 255)
            if board[row][0].content == board[row][1].content == board[row][2].content != "":
                message(player(Player) + " won!", Constans.BLUE)
                return True
            elif board[0][field].content == board[1][field].content == board[2][
                field].content != "":
                message(player(Player) + " won!", Constans.BLUE)
                return True
            elif board[0][0].content == board[1][1].content == board[2][2].content != "":
                message(player(Player) + " won!", Constans.BLUE)
                return True
            elif board[0][2].content == board[1][1].content == board[2][0].content != "":
                message(player(Player) + " won!", Constans.BLUE)
                return True
    return False


while True:
    fpsClock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        draw()
        text_surface_obj = font_obj.render(Player + "  ", True, (255, 100, 100), (0, 0, 0))
        text_rect_obj = text_surface_obj.get_rect()
        window.blit(text_surface_obj, text_rect_obj)
        if winner():
            print("winner")
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            for row in range(len(board)):
                for field in range(len(board[row])):
                    if board[row][field].if_clicked(mouse_pos=mouse_position):
                        if board[row][field].content == "":
                            if Player == "player 2":
                                board[row][field].set_content("O")
                            if Player == "player 1":
                                board[row][field].set_content("X")
                            Player = player(Player)

    pygame.display.update()
    pygame.time.Clock().tick