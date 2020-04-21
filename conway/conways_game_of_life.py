import pygame


def countNeighbours(matrix, col, row):
    count = 0

    if row != 0:  # left
        if matrix[col][row - 1] == 1:
            count = count + 1

    if row != len(matrix[col])-1:  # right
        if matrix[col][row + 1] == 1:
            count = count + 1

    if col != 0:  # up
        if matrix[col - 1][row] == 1:
            count = count + 1

    if col != len(matrix)-1:  # down
        if matrix[col + 1][row] == 1:
            count = count + 1

    if row != 0 and col != 0:  # up left
        if matrix[col - 1][row - 1] == 1:
            count = count + 1

    if row != len(matrix[col])-1 and col != 0:  # up right
        if matrix[col - 1][row + 1] == 1:
            count = count + 1

    if row != len(matrix[col])-1 and col != len(matrix)-1:  # down right
        if matrix[col + 1][row + 1] == 1:
            count = count + 1

    if row != 0 and col != len(matrix)-1:  # down left
        if matrix[col + 1][row - 1] == 1:
            count = count + 1

    return count


def checkCell(matrix, col, row):
    neighbours = countNeighbours(matrix, col, row)

    if matrix[col][row] == 1:  # if alive
        if neighbours < 2 or neighbours > 3:
            return 0  # death
        else:
            return 1  # nothing happens
    else:  # if dead
        if neighbours == 3:
            return 1  # birth
        else:
            return 0  # nothing happens


def updateMatrix(matrix):
    matrix_new = [[0 for _ in range(len(matrix[0]))]
                  for _ in range(len(matrix))]

    for colnr in range(len(matrix)):
        for rownr in range(len(matrix[colnr])):
            matrix_new[colnr][rownr] = checkCell(matrix, colnr, rownr)
    return matrix_new


DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
GAMEDISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(f"DinoGame")
CLOCK = pygame.time.Clock()
BACKGROUND = pygame.Surface(GAMEDISPLAY.get_size())
BACKGROUND = BACKGROUND.convert()
BACKGROUND.fill(WHITE)
GAME_QUIT = False

GAME_RUNNING = False

MATRIX_COLS = round(DISPLAY_HEIGHT / 10)
MATRIX_ROWS = round(DISPLAY_WIDTH / 10)
matrix_show = [[0 for _ in range(MATRIX_COLS)] for _ in range(MATRIX_ROWS)]
mouse_adding = False
mouse_pressed = False

while not GAME_QUIT:

    GAMEDISPLAY.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # start drawing
            mouse_pressed = True  # keep drawing
            x = round(event.pos[1]/10)  # position rounded
            y = round(event.pos[0]/10)  # position rounded
            if matrix_show[y][x] == 1:  # is cell set
                matrix_show[y][x] = 0  # kill
                mouse_adding = False  # keep removing
            else:
                matrix_show[y][x] = 1  # birth
                mouse_adding = True  # keep birthing
        elif event.type == pygame.MOUSEMOTION:  # mouse was moved
            if mouse_pressed:  # if drawing
                x = round(event.pos[1]/10)  # position rounded
                y = round(event.pos[0]/10)  # position rounded
                # when removing and cell was set
                if matrix_show[y][x] == 1 and mouse_adding == False:
                    matrix_show[y][x] = 0  # kill
                # when drawing and cell was dead
                elif matrix_show[y][x] == 0 and mouse_adding == True:
                    matrix_show[y][x] = 1  # birth
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False  # stop drawing
        elif event.type == pygame.KEYDOWN:
            if event.key == 32:  # spacebar to start and stop
                GAME_RUNNING = not GAME_RUNNING
        else:
            pass
            # print(event)

    if GAME_RUNNING:
        matrix_show = updateMatrix(matrix_show)

    for colnr in range(len(matrix_show)):
        for rownr in range(len(matrix_show[colnr])):
            if matrix_show[colnr][rownr] == 1:
                GAMEDISPLAY.fill(BLACK, (colnr * 10, rownr * 10, 10, 10))

    pygame.display.update()
    if not GAME_RUNNING:  # drawing
        CLOCK.tick(60)
    else:  # running slower to watch
        CLOCK.tick(10)

pygame.quit()
quit()
