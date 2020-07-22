import pygame
import sys
import os
from pygame.locals import *
pygame.font.init()

WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BUTTONSIZE = 175
BUTTONGAPSIZE = 20
pygame.display.set_caption("Tic Tac Toe")

# define colors
WHITE = (255, 255, 255)
BLACK = (0  ,   0,   0)
CREAM = (255, 253, 208)
RED =   (255,   0,   0)
CRIMSON = (220, 20, 60)
BGCOLOR = BLACK
TILECOLOR = CREAM

# define the font object used
GAMEFONT = pygame.font.SysFont("comicsansms", 14)

# define margins
XMARGIN = int( (WIDTH - (3 * BUTTONSIZE) - (2 * BUTTONGAPSIZE )) / 2 )
YMARGIN = int( (HEIGHT - (3 * BUTTONSIZE) - (2 * BUTTONGAPSIZE )) / 2 )

# define buttons for gameplay
# top row
TOPLEFTRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
TOPMIDRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
TOPRIGHTRECT = pygame.Rect(XMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), YMARGIN, BUTTONSIZE, BUTTONSIZE)
# middle row
MIDLEFTRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
MIDMIDRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE , BUTTONSIZE, BUTTONSIZE)
MIDRIGHTRECT = pygame.Rect(XMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
# bottom row
BOTLEFTRECT = pygame.Rect(XMARGIN, YMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE)
BOTMIDRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE)
BOTRIGHTRECT = pygame.Rect(XMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), YMARGIN + (2 * BUTTONSIZE) + (2 * BUTTONGAPSIZE), BUTTONSIZE, BUTTONSIZE)
# define x and o


# start main game loop
def main():
# define global variables
    global DISPLAYSURF, board, current_player, game_over, run, moves_count, BGCOLOR
# initializeglobal DISPLAYSURF, board, current_player, game_over, run
    pygame.init()
# create window display
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    DISPLAYSURF.fill(BGCOLOR)
# add caption to window
    pygame.display.set_caption("TicTacToe")
# create game board array tracker
    initialize_game()

    while run: # main game loop

        pygame.time.delay(100)
        show_turn()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    initialize_game()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # top row
                if not game_over:
                    if TOPLEFTRECT.collidepoint(pos) and board[0][0] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[0][0] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, TOPLEFTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, TOPLEFTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[0][0] = 2
                            moves_count += 1
                    if TOPMIDRECT.collidepoint(pos) and board[0][1] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[0][1] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, TOPMIDRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, TOPMIDRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[0][1] = 2
                            moves_count += 1
                    if TOPRIGHTRECT.collidepoint(pos) and board[0][2] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[0][2] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, TOPRIGHTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, TOPRIGHTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[0][2] = 2
                            moves_count += 1
                    # middle row
                    if MIDLEFTRECT.collidepoint(pos) and board[1][0] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[1][0] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, MIDLEFTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, MIDLEFTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[1][0] = 2
                            moves_count += 1
                    if MIDMIDRECT.collidepoint(pos) and board[1][1] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[1][1] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, MIDMIDRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, MIDMIDRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[1][1] = 2
                            moves_count += 1
                    if MIDRIGHTRECT.collidepoint(pos) and board[1][2] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[1][2] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, MIDRIGHTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, MIDRIGHTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[1][2] = 2
                            moves_count += 1
                    # bottom row
                    if BOTLEFTRECT.collidepoint(pos) and board[2][0] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[2][0] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, BOTLEFTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, BOTLEFTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[2][0] = 2
                            moves_count += 1
                    if BOTMIDRECT.collidepoint(pos) and board[2][1] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + BUTTONSIZE + BUTTONGAPSIZE + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[2][1] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, BOTMIDRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, BOTMIDRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[2][1] = 2
                            moves_count += 1
                    if BOTRIGHTRECT.collidepoint(pos) and board[2][2] == 0:
                        if current_player == 'X':
                            # X
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), 6)
                            pygame.draw.line(DISPLAYSURF, CRIMSON, (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3)), (XMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + BUTTONSIZE - (BUTTONSIZE // 3), YMARGIN + (BUTTONSIZE * 2) + (BUTTONGAPSIZE * 2) + (BUTTONSIZE // 3)), 6)
                            current_player = "O"
                            board[2][2] = 1
                            moves_count += 1
                        else:
                            # O
                            pygame.draw.circle(DISPLAYSURF, CRIMSON, BOTRIGHTRECT.center, (BUTTONSIZE // 3) // 2)
                            pygame.draw.circle(DISPLAYSURF, CREAM, BOTRIGHTRECT.center, ((BUTTONSIZE // 3) // 2) - 6)
                            current_player = "X"
                            board[2][2] = 2
                            moves_count += 1

                if check_win(1):
                    show_outcome(winner)
                    game_over = True
                if check_win(2):
                    show_outcome(winner)
                    game_over = True
                if moves_count == 9 and winner == 0:
                    show_outcome(winner)

        pygame.display.update()


def draw_buttons():
    pygame.draw.rect(DISPLAYSURF, CREAM, TOPLEFTRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, TOPMIDRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, TOPRIGHTRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, MIDLEFTRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, MIDMIDRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, MIDRIGHTRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, BOTLEFTRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, BOTMIDRECT)
    pygame.draw.rect(DISPLAYSURF, CREAM, BOTRIGHTRECT)


def terminate():
    pygame.quit()
    sys.exit()


def check_win(player):
    global winner
    # check rows for winner:
    for row in board:
        for value in row:
            if value == player:
                continue
            else:
                break
        else:
            winner = player
            return True

    # check colunms for winner:
    for column in range(3):
        for row in board:
            if row[column] == player:
                continue
            else:
                break
        else:
            winner = player
            return True

    # check left-right diagonal: (0,0),(1,1),(2,2)
    for value in range(3):
        if board[value][value] == player:
            continue
        else:
            break
    else:
        winner = player
        return True

    # check right-left diagonal: (0,2),(1,1),(2,0)
    for value in range(3):
        if board[value][2 - value] == player:
            continue
        else:
            break
    else:
        winner = player
        return True


def initialize_game():
    global board, current_player, game_over, run, winner, moves_count, BGCOLOR
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    draw_buttons()
    run = True
    game_over = False
    current_player = "X"
    winner = 0
    moves_count = 0
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, ((WIDTH // 2) - 50, 0, 100, YMARGIN - 1))


def show_turn():
    global DISPLAYSURF, current_player, GAMEFONT

    xtracker = GAMEFONT.render("X", 1, WHITE)
    xtrackerrect = xtracker.get_rect()
    xtrackerrect.topleft = ((XMARGIN //2 ), HEIGHT - (YMARGIN // 2))

    otracker = GAMEFONT.render("O", 1, WHITE)
    otrackerrect = otracker.get_rect()
    otrackerrect.topleft = ((XMARGIN), HEIGHT - (YMARGIN // 2))

    active_player_background = "X"
    if current_player == "X":
        xbackround = pygame.draw.rect(DISPLAYSURF, RED, xtrackerrect)
        obackground = pygame.draw.rect(DISPLAYSURF, BLACK, otrackerrect)
    else:
        xbackround = pygame.draw.rect(DISPLAYSURF, BLACK, xtrackerrect)
        obackground = pygame.draw.rect(DISPLAYSURF, RED, otrackerrect)

    DISPLAYSURF.blit(xtracker, xbackround)
    DISPLAYSURF.blit(otracker, obackground)


def show_outcome(winning_player):
    global DISPLAYSURF

    XWINNER = GAMEFONT.render("X WINS!", 1, WHITE)
    xwinnerrect = XWINNER.get_rect()
    xwinnerrect.center = ((WIDTH // 2), (YMARGIN // 2))
    OWINNER = GAMEFONT.render("O WINS", 1, WHITE)
    owinnerrect = OWINNER.get_rect()
    owinnerrect.center = ((WIDTH // 2), (YMARGIN // 2))
    TIEDGAME = GAMEFONT.render("IT WAS A TIE", 1, WHITE)
    tiedgamerect = TIEDGAME.get_rect()
    tiedgamerect.center = ((WIDTH // 2), (YMARGIN // 2))

    if winning_player == 1:
        DISPLAYSURF.blit(XWINNER, xwinnerrect)
    elif winning_player == 2:
        DISPLAYSURF.blit(OWINNER, owinnerrect)
    else:
        DISPLAYSURF.blit(TIEDGAME, tiedgamerect)

main()