import pygame
from random import randint

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Папа сапёра')


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left=10, top=10, cell_size=30):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pass

    def get_cell(self, mouse_pos):
        for row in range(self.height):
            for cell in range(self.width):
                cell_rect = pygame.Rect(self.left + cell * self.cell_size, self.top + row * self.cell_size,
                                        self.cell_size, self.cell_size)
                if cell_rect.collidepoint(mouse_pos):
                    return cell, row
        return None

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, width, height, mines_count):
        super().__init__(width, height)
        self.mines_count = mines_count
        self.place_mines()
        self.font = pygame.font.Font(None, 50)

    def render(self, screen):
        for row in range(self.height):
            for cell in range(self.width):
                cell_rect = pygame.Rect(self.left + cell * self.cell_size, self.top + row * self.cell_size,
                                        self.cell_size, self.cell_size)
                if self.board[row][cell] == -1:
                    pygame.draw.rect(screen, pygame.Color((96, 7, 105)), cell_rect)
                elif self.board[row][cell]:
                    text = self.font.render(str(self.board[row][cell]) if self.board[row][cell] > 0 else "0",
                                            True, (255, 255, 255))
                    screen.blit(text, (cell_rect.left + 3, cell_rect.top + 3))
                pygame.draw.rect(screen, pygame.Color("white"), cell_rect, 1)

    def place_mines(self):
        for i in range(self.mines_count):
            done = False
            while not done:
                cell = (randint(0, self.width - 1), randint(0, self.height - 1))
                if not self.board[cell[1]][cell[0]]:
                    self.board[cell[1]][cell[0]] = -1
                    done = True

    def get_neighbours(self, cell):
        neighbours = []
        for y in range(self.height):
            for x in range(self.width):
                if abs(cell[1] - y) <= 1 and abs(cell[0] - x) <= 1 and (x != cell[0] or y != cell[1]):
                    neighbours.append((x, y))
        return neighbours

    def open_cell(self, cell):
        if not self.board[cell[1]][cell[0]]:
            neighbours = self.get_neighbours(cell)
            mines_count = len(list(filter(lambda x: self.board[x[1]][x[0]] == -1, neighbours)))
            if mines_count:
                self.board[cell[1]][cell[0]] = mines_count
            else:
                self.board[cell[1]][cell[0]] = -2
                for i in neighbours:
                    if self.board[i[1]][i[0]] == 0:
                        self.open_cell(i)

    def on_click(self, cell):
        if cell:
            self.open_cell(cell)


board = Minesweeper(10, 10, 10)
board.set_view(50, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
