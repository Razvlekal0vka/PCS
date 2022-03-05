print('Start examination.py')

import pygame
import copy
import random

pygame.init()
size = width, heigth = 290, 290
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Дедушка - сапёр')
screen.fill((110, 110, 110))


class Board:
    # создание поля
    def __init__(self, width, height):
        self.left = 0
        self.cell_size = 0
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board1 = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.k = 0
        self.k1 = 0
        self.font = pygame.font.SysFont("Comic MS", 20)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                if self.board[j][i] == 1:
                    pygame.draw.rect(screen,
                                     (149, 0, 255),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 0)

                elif self.board[j][i] != 0:
                    num = self.board1[j][i]
                    screen.blit(self.font.render(str(num), 1, (50, 250, 50)), (self.left + self.cell_size * i,
                                                                               self.top + self.cell_size * j))

                pygame.draw.rect(screen,
                                 (0, 0, 0),
                                 (self.left + self.cell_size * i,
                                  self.top + self.cell_size * j,
                                  self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if self.width <= cell_x or cell_x < 0 or self.height <= cell_y or cell_y < 0:
            return
        return cell_x, cell_y

    def on_click(self, cell_coords):
        if cell_coords:
            if self.board[cell_coords[1]][cell_coords[0]] == 0:
                self.k = 2
                self.board[cell_coords[1]][cell_coords[0]] = 2
        print(cell_coords)
        board.update(cell_coords)

    def update(self, ck):
        temp_board = copy.deepcopy(self.board)
        temp_board1 = copy.deepcopy(self.board)
        for i in range(self.width):
            for j in range(self.height):
                x1, y1 = i - 1, j - 1
                x2, y2 = i + 1, j + 1

                #

                neib = 0

                if y1 >= 0:
                    if self.board[y1][i] != 2:
                        neib += self.board[y1][i]

                if y2 <= self.height - 1:
                    if self.board[y2][i] != 2:
                        neib += self.board[y2][i]

                if x1 >= 0:
                    if self.board[j][x1] != 2:
                        neib += self.board[j][x1]

                if x2 <= self.width - 1:
                    if self.board[j][x2] != 2:
                        neib += self.board[j][x2]

                if y1 >= 0 and x1 >= 0:
                    if self.board[y1][x1] != 2:
                        neib += self.board[y1][x1]

                if y1 >= 0 and x2 <= self.width - 1:
                    if self.board[y1][x2] != 2:
                        neib += self.board[y1][x2]

                if y2 <= self.height - 1 and x1 >= 0:
                    if self.board[y2][x1] != 2:
                        neib += self.board[y2][x1]

                if y2 <= self.height - 1 and x2 <= self.width - 1:
                    if self.board[y2][x2] != 2:
                        neib += self.board[y2][x2]

                temp_board1[j][i] = neib
        for i in range(self.width):
            for j in range(self.height):
                self.board1[j][i] = temp_board1[j][i]

    def opp(self):
        for _ in range(random.randint(2, 15)):
            cell_coords = (random.randint(0, 8), random.randint(0, 8))
            if cell_coords:
                self.board[cell_coords[1]][cell_coords[0]] = 1


board = Board(9, 9)
running = True
op = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if not op:
            board.opp()
            op = True
    screen.fill((10, 10, 10))
    board.render(screen)
    pygame.display.flip()
pygame.quit()