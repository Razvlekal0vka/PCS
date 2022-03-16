import os

import pygame

set_data = []
num_cell_x, num_cell_y, cell_size, shift_left, shift_top, size = 0, 0, 0, 0, 0, 0
set_list = open('data/settings.txt', 'r')
num_line = 0
for line in set_list:
    line = line.replace('\n', '', 1)
    if num_line == 2:
        size = width, heigth = int(list(line.split('*'))[0]), int(list(line.split('*'))[1])
        if line == '800*450':
            cell_size = 30
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -20, -15
        elif line == '1280*720':
            cell_size = 48
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -32, -24
        elif line == '1600*900':
            cell_size = 60
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -40, -30
        elif line == '1920*1080':
            cell_size = 72
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -48, -36
        elif line == '2048*1152':
            cell_size = 77
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -51, -38
        elif line == '3840*2160':
            cell_size = 144
            num_cell_x, num_cell_y = 28, 16
            shift_left, shift_top = -96, -72
        set_data.append(line)
    num_line += 1

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Personal Cloud Sync')
screen.fill((110, 110, 110))
clock = pygame.time.Clock()
k = cell_size / 30


class Board:
    # создание поля
    def __init__(self, width, height, size, left, top, k):
        self.left = 0
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения
        # 0 - ничего не выделяется
        # 1 - оранжевый квадрат загрузки
        # 2 - красный квадрат ошибки в загрузке
        # 3 - клетка в которую записывается текст
        self.board1 = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = left
        self.top = top
        self.cell_size = size
        self.k = 0
        self.k1 = 0
        self.font = pygame.font.SysFont("Comic MS", 20)
        self.coord_loading = [0, 14]

        '--------------------------------------------------------------------------------'
        '--------------------------------------------------------------------------------'
        self.col_examination = 1  # Количество проверок
        '--------------------------------------------------------------------------------'
        '--------------------------------------------------------------------------------'

        self.number_of_cells = self.width - 2
        self.percent, self.rest_of_step = 0, 0
        self.percent_for_step = (self.col_examination / self.number_of_cells) / self.col_examination
        self.percent_3 = self.number_of_cells // self.col_examination
        self.rest_of_step = self.number_of_cells % self.col_examination
        self.col_step_3 = 0

        self.board_words = [[0] * width for _ in range(height)]
        self.letters_ru = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЫыЭэЮюЯя'
        self.letters_en = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        self.letters_sy = '_-ъь[]|/.,<>?&'
        self.letters_nu = '0123456789'

        # Отступы для букв
        self.indents_and_sizes_for_letters_800_450 = {'P': [7, 4], 'e': [8, 4], 'r': [8, 4], 's': [8, 4],
                                                      'o': [8, 4], 'n': [8, 4], 'a': [8, 4], 'l': [11, 4],
                                                      'C': [6, 4], 'u': [7, 4], 'd': [7, 4], 'S': [7, 4],
                                                      'y': [7, 0], 'c': [7, 4], 'razm': 35}
        self.indents_and_sizes_for_letters_1280_720 = {'P': [12, 7], 'e': [13, 7], 'r': [15, 7], 's': [13, 7],
                                                       'o': [13, 7], 'n': [13, 7], 'a': [13, 7], 'l': [18, 7],
                                                       'C': [10, 7], 'u': [12, 7], 'd': [12, 7], 'S': [12, 7],
                                                       'y': [12, 0], 'c': [12, 7], 'razm': 56}
        self.indents_and_sizes_for_letters_1600_900 = {'P': [15, 9], 'e': [16, 9], 'r': [19, 9], 's': [16, 9],
                                                       'o': [16, 9], 'n': [16, 9], 'a': [16, 9], 'l': [23, 9],
                                                       'C': [12, 9], 'u': [15, 9], 'd': [15, 9], 'S': [15, 9],
                                                       'y': [15, 0], 'c': [15, 9], 'razm': 70}
        self.indents_and_sizes_for_letters_1920_1080 = {'P': [18, 11], 'e': [19, 11], 'r': [23, 11], 's': [19, 11],
                                                        'o': [19, 11], 'n': [19, 11], 'a': [19, 11], 'l': [28, 11],
                                                        'C': [14, 11], 'u': [18, 11], 'd': [23, 11], 'S': [18, 11],
                                                        'y': [18, 0], 'c': [18, 11], 'razm': 84}
        self.indents_and_sizes_for_letters_2048_1152 = {'P': [19, 11], 'e': [20, 11], 'r': [24, 22], 's': [20, 11],
                                                        'o': [20, 11], 'n': [20, 11], 'a': [20, 11], 'l': [29, 11],
                                                        'C': [15, 11], 'u': [19, 11], 'd': [19, 11], 'S': [19, 11],
                                                        'y': [19, 0], 'c': [19, 11], 'razm': 89}
        self.indents_and_sizes_for_letters_3840_2160 = {'P': [36, 22], 'e': [38, 22], 'r': [46, 22], 's': [38, 22],
                                                        'o': [38, 22], 'n': [38, 22], 'a': [38, 22], 'l': [56, 22],
                                                        'C': [28, 22], 'u': [36, 22], 'd': [46, 22], 'S': [36, 22],
                                                        'y': [36, 0], 'c': [36, 22], 'razm': 168}
        self.colors = [(60, 63, 65), (60, 63, 65), (60, 63, 65), (60, 63, 65), (60, 63, 65), (43, 43, 43),
                       (198, 117, 49)]

        '''записываем слова'''
        name = ['Personal', 'Cloud', 'Sync']
        for _ in range(1, 9):
            self.board[1][_] = 3
            self.board_words[_][1] = name[0][_ - 1]
        for _ in range(1, 6):
            self.board[2][_] = 3
            self.board_words[_][2] = name[1][_ - 1]
        for _ in range(1, 5):
            self.board[3][_] = 3
            self.board_words[_][3] = name[2][_ - 1]

        self.code = 'load1'
        self.kil_code = ''

        """Интересные факты"""
        # [размер надписи, x0, y0, x1, y1, цвет надписи, цвет фона, время показывания, x смешение, y смещение, текстъ]
        self.interesting_facts = [[35, 1, 13, 6, 13, (21, 176, 151), (60, 63, 65), 5, 13, 4,
                                   'Neuro studio'],
                                  [30, 1, 13, 21, 13, (255, 131, 96), (60, 63, 65), 2, 6, 6,
                                   'Идея о этом проекте пришла нам еще в середине 2021 года.'],
                                  [30, 1, 12, 17, 13, (212, 180, 131), (60, 63, 65), 5, 7, 6,
                                   'Do you know how many man/hours it took to write',
                                   'this program?']
                                  ]
        self.text_code, self.text_code_start_stop, self.text_code_change = 0, '', 1
        self.colors_facts = [(43, 43, 43), (60, 63, 65)]
        self.counter_fact = 0
        self.time_between_facts = 2
        self.count_text = 0

        self.k = k  # подобия разрешений относительно 800*450

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
                                     self.colors[6],
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)
                    pygame.draw.rect(screen, (43, 43, 43), (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                        self.cell_size), 3)

                elif self.board[j][i] == 2:
                    pygame.draw.rect(screen,
                                     (203, 49, 55),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)
                    pygame.draw.rect(screen, (43, 43, 43), (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                        self.cell_size), 3)


                elif self.board[j][i] == 3:
                    shift_left, shift_down, size = 0, 0, self.cell_size
                    if self.cell_size == 60:
                        shift_left = self.indents_and_sizes_for_letters_1600_900[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_1600_900[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_1600_900['razm']
                    elif self.cell_size == 48:
                        shift_left = self.indents_and_sizes_for_letters_1280_720[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_1280_720[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_1280_720['razm']
                    elif self.cell_size == 30:
                        shift_left = self.indents_and_sizes_for_letters_800_450[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_800_450[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_800_450['razm']
                    elif self.cell_size == 72:
                        shift_left = self.indents_and_sizes_for_letters_1920_1080[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_1920_1080[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_1920_1080['razm']
                    elif self.cell_size == 77:
                        shift_left = self.indents_and_sizes_for_letters_2048_1152[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_2048_1152[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_2048_1152['razm']
                    elif self.cell_size == 144:
                        shift_left = self.indents_and_sizes_for_letters_3840_2160[str(self.board_words[i][j])][0]
                        shift_down = self.indents_and_sizes_for_letters_3840_2160[str(self.board_words[i][j])][1]
                        size = self.indents_and_sizes_for_letters_3840_2160['razm']
                    if 2 <= i <= 4 and j == 3:
                        RGB = self.colors[0]
                    elif (i == 1 and j == 2) or (1 <= i <= 4 and j == 1) or (i == 1 and j == 3):
                        RGB = self.colors[1]
                    elif 2 <= i <= 5 and j == 2:
                        RGB = self.colors[2]
                    elif 5 <= i <= 9 and j == 1:
                        RGB = self.colors[3]
                    else:
                        RGB = self.colors[4]
                    cell_rect = pygame.Rect(self.left + i * self.cell_size, self.top + j * self.cell_size,
                                            self.cell_size, self.cell_size)
                    if self.code == 'load1' or self.code == 'kil_end' or self.code == 'end':
                        pygame.draw.rect(screen,
                                         RGB,
                                         (self.left + self.cell_size * i,
                                          self.top + self.cell_size * j,
                                          self.cell_size, self.cell_size), 6)
                    elif self.code == 'load2' or self.code == 'kil':
                        pygame.draw.rect(screen,
                                         RGB,
                                         (self.left + self.cell_size * i,
                                          self.top + self.cell_size * j,
                                          self.cell_size, self.cell_size), 0)
                    else:
                        pygame.draw.rect(screen,
                                         (255, 255, 255),
                                         (self.left + self.cell_size * i,
                                          self.top + self.cell_size * j,
                                          self.cell_size, self.cell_size), 0)
                    self.font = pygame.font.Font(None, size)
                    text = self.font.render(str(self.board_words[i][j]), True, self.colors[5])
                    screen.blit(text, (cell_rect.left + shift_left, cell_rect.top + shift_down))

                    pygame.draw.rect(screen, (43, 43, 43), (
                        self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                        self.cell_size), 3)
                else:
                    if 0 <= self.text_code < len(self.interesting_facts):
                        if self.interesting_facts[self.text_code][1] <= i <= self.interesting_facts[self.text_code][
                            3] and self.interesting_facts[self.text_code][2] <= j <= \
                                self.interesting_facts[self.text_code][4]:
                            if self.text_code_change == 1 or self.text_code_change == 5 or self.text_code_change == 6 or self.text_code_change == 666:
                                pygame.draw.rect(screen,
                                                 self.colors_facts[1],
                                                 (self.left + self.cell_size * i,
                                                  self.top + self.cell_size * j,
                                                  self.cell_size, self.cell_size), 6)
                                pygame.draw.rect(screen, (43, 43, 43), (
                                    self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                                    self.cell_size), 3)
                            elif self.text_code_change == 2 or self.text_code_change == 3 or self.text_code_change == 4:
                                pygame.draw.rect(screen,
                                                 self.colors_facts[1],
                                                 (self.left + self.cell_size * i,
                                                  self.top + self.cell_size * j,
                                                  self.cell_size, self.cell_size), 0)
                                if self.interesting_facts[self.text_code][2] != self.interesting_facts[self.text_code][
                                    4]:
                                    for e in range(self.interesting_facts[self.text_code][2],
                                                   self.interesting_facts[self.text_code][4] + 1):
                                        if i == self.interesting_facts[self.text_code][3]:
                                            i = 1
                                            cell_rect = pygame.Rect(self.left + i * self.cell_size,
                                                                    self.top + e * self.cell_size,
                                                                    self.cell_size, self.cell_size)
                                            self.font = pygame.font.Font(None, int(self.k * self.interesting_facts[
                                                self.text_code][0]))
                                            text = self.font.render(
                                                str(self.interesting_facts[self.text_code][10 + self.count_text]), True,
                                                self.colors_facts[0])
                                            screen.blit(text, (
                                            cell_rect.left + int(self.k * self.interesting_facts[self.text_code][8]),
                                            cell_rect.top + int(self.k * self.interesting_facts[self.text_code][9])))
                                            self.count_text += 1
                                            i = self.interesting_facts[self.text_code][3]
                                    self.count_text = 0
                                else:
                                    if i == self.interesting_facts[self.text_code][3]:
                                        i = 1
                                        cell_rect = pygame.Rect(self.left + i * self.cell_size,
                                                                self.top + j * self.cell_size,
                                                                self.cell_size, self.cell_size)
                                        self.font = pygame.font.Font(None, int(self.k * self.interesting_facts[self.text_code][0]))
                                        text = self.font.render(
                                            str(self.interesting_facts[self.text_code][10 + self.count_text]), True,
                                            self.colors_facts[0])
                                        screen.blit(text, (cell_rect.left + int(self.k * self.interesting_facts[self.text_code][8]),
                                                           cell_rect.top + int(self.k * self.interesting_facts[self.text_code][9])))
                                        i = self.interesting_facts[self.text_code][3]
                        else:
                            pygame.draw.rect(screen,
                                             (60, 63, 65),
                                             (self.left + self.cell_size * i,
                                              self.top + self.cell_size * j,
                                              self.cell_size, self.cell_size), 6)

                            pygame.draw.rect(screen, (43, 43, 43), (
                                self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                                self.cell_size), 3)
                    else:
                        pygame.draw.rect(screen,
                                         (60, 63, 65),
                                         (self.left + self.cell_size * i,
                                          self.top + self.cell_size * j,
                                          self.cell_size, self.cell_size), 6)

                        pygame.draw.rect(screen, (43, 43, 43), (
                            self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                            self.cell_size), 3)

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
                self.board[cell_coords[1]][cell_coords[0]] = 666

    def loading(self, step_examination, cod_examination):
        if self.col_examination > self.number_of_cells:
            col_examination = self.col_examination
            self.percent += (step_examination / col_examination - self.percent)
            percent_for_step = (self.col_examination / self.number_of_cells) / self.col_examination

            if self.percent >= self.percent_for_step:
                self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
                if self.coord_loading[0] <= self.number_of_cells:
                    self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                if self.percent >= 1:
                    self.kil_code = 'kil'
                    self.text_code_start_stop = 'kil'
                    self.text_code_change = 4

                self.percent -= self.percent_for_step
                self.percent_for_step += percent_for_step

        elif self.col_examination == self.number_of_cells:
            self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
            if self.coord_loading[0] <= self.number_of_cells:
                self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                if self.coord_loading[0] == self.number_of_cells:
                    self.kil_code = 'kil'
                    self.text_code_start_stop = 'kil'
                    self.text_code_change = 4

        elif self.col_examination < self.number_of_cells:
            self.percent = self.number_of_cells // self.col_examination
            self.rest_of_step = self.number_of_cells % self.col_examination
            for _ in range(self.percent_3):
                self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
                if self.coord_loading[0] <= self.number_of_cells:
                    self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                    if self.coord_loading[0] == self.number_of_cells:
                        self.kil_code = 'kil'
                        self.text_code_start_stop = 'kil'
                        self.text_code_change = 4

            if self.col_step_3 < self.rest_of_step:
                self.col_step_3 += 1
                self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
                if self.coord_loading[0] <= self.number_of_cells:
                    self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                    if self.coord_loading[0] == self.number_of_cells:
                        self.kil_code = 'kil'
                        self.text_code_start_stop = 'kil'
                        self.text_code_change = 4

    def color_change(self, sc):
        if self.code == 'load1' and sc >= 60:
            colors_start = [(43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43)]
            r, g, b = self.colors[0]
            r1, g1, b1 = colors_start[0]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[0] = r, g, b

            r, g, b = self.colors[1]
            r1, g1, b1 = colors_start[1]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[1] = r, g, b

            r, g, b = self.colors[2]
            r1, g1, b1 = colors_start[2]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[2] = r, g, b

            r, g, b = self.colors[3]
            r1, g1, b1 = colors_start[3]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[3] = r, g, b

            r, g, b = self.colors[4]
            r1, g1, b1 = colors_start[4]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[4] = r, g, b

            r, g, b = self.colors[5]
            r1, g1, b1 = colors_start[5]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[5] = r, g, b
            if sc >= 90:
                self.code = 'load2'
        if self.code == 'load2':
            colors_start = [(80, 140, 76), (181, 158, 62), (132, 78, 126), (198, 117, 49), (76, 80, 82),
                            (255, 255, 255)]
            r, g, b = self.colors[0]
            r1, g1, b1 = colors_start[0]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[0] = r, g, b

            r, g, b = self.colors[1]
            r1, g1, b1 = colors_start[1]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[1] = r, g, b

            r, g, b = self.colors[2]
            r1, g1, b1 = colors_start[2]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[2] = r, g, b

            r, g, b = self.colors[3]
            r1, g1, b1 = colors_start[3]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[3] = r, g, b

            r, g, b = self.colors[4]
            r1, g1, b1 = colors_start[4]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[4] = r, g, b

            r, g, b = self.colors[5]
            r1, g1, b1 = colors_start[5]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[5] = r, g, b

            if self.colors[3] == colors_start[3]:
                self.code = 'kil'
                self.text_code_start_stop = 'start'

        elif self.kil_code == 'kil' and self.code == 'kil':
            colors_end = [(43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43), (43, 43, 43)]
            r, g, b = self.colors[0]
            r1, g1, b1 = colors_end[0]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[0] = r, g, b

            r, g, b = self.colors[1]
            r1, g1, b1 = colors_end[1]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[1] = r, g, b

            r, g, b = self.colors[2]
            r1, g1, b1 = colors_end[2]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[2] = r, g, b

            r, g, b = self.colors[3]
            r1, g1, b1 = colors_end[3]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[3] = r, g, b

            r, g, b = self.colors[4]
            r1, g1, b1 = colors_end[4]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[4] = r, g, b

            r, g, b = self.colors[5]
            r1, g1, b1 = colors_end[5]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b > b1:
                b -= 2
            self.colors[5] = r, g, b

            if self.colors[5] == colors_end[5]:
                self.code = 'kil_end'

        elif self.code == 'kil_end':
            colors_start = [(60, 63, 65), (60, 63, 65), (60, 63, 65), (60, 63, 65), (60, 63, 65), (43, 43, 43),
                            (60, 63, 65)]
            r, g, b = self.colors[0]
            r1, g1, b1 = colors_start[0]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[0] = r, g, b

            r, g, b = self.colors[1]
            r1, g1, b1 = colors_start[1]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[1] = r, g, b

            r, g, b = self.colors[2]
            r1, g1, b1 = colors_start[2]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[2] = r, g, b

            r, g, b = self.colors[3]
            r1, g1, b1 = colors_start[3]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[3] = r, g, b

            r, g, b = self.colors[4]
            r1, g1, b1 = colors_start[4]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[4] = r, g, b

            r, g, b = self.colors[5]
            r1, g1, b1 = colors_start[5]
            if r < r1:
                r += 2
            if g < g1:
                g += 2
            if b < b1:
                b += 2
            self.colors[5] = r, g, b

            r, g, b = self.colors[6]
            r1, g1, b1 = colors_start[6]
            if r > r1:
                r -= 2
            if g > g1:
                g -= 2
            if b < b1:
                b += 2
            self.colors[6] = r, g, b

            if colors_start[6] == self.colors[6] and self.text_code_change == 666:
                self.code = 'end'
                self.kil()

    def background_change(self):
        pass

    def kil(self):
        os.system('PCS.py')
        '''kil'''
        pass

    def change_of_interesting_facts(self, ch_f):
        if self.text_code_start_stop == 'kil' or self.text_code_start_stop == 'start':
            if self.text_code_change == 1:
                colors_start = [(43, 43, 43), (43, 43, 43)]
                r, g, b = self.colors_facts[0]
                r1, g1, b1 = colors_start[0]
                if r > r1:
                    r -= 1
                if g > g1:
                    g -= 1
                if b > b1:
                    b -= 1
                self.colors_facts[0] = r, g, b

                r, g, b = self.colors_facts[1]
                r1, g1, b1 = colors_start[1]
                if r > r1:
                    r -= 1
                if g > g1:
                    g -= 1
                if b > b1:
                    b -= 1
                self.colors_facts[1] = r, g, b
                if self.colors_facts[1] == colors_start[1]:
                    self.text_code_change = 2

            elif self.text_code_change == 2:
                color_text, color_background = self.interesting_facts[self.text_code][5], \
                                               self.interesting_facts[self.text_code][6]
                r, g, b = self.colors_facts[0]
                r1, g1, b1 = color_text
                if self.text_code != 0:
                    if r < r1:
                        r += 1
                    if g < g1:
                        g += 1
                    if b < b1:
                        b += 1
                else:
                    if r > r1:
                        r -= 1
                    if g < g1:
                        g += 1
                    if b < b1:
                        b += 1
                self.colors_facts[0] = r, g, b

                r, g, b = self.colors_facts[1]
                r1, g1, b1 = color_background
                if r < r1:
                    r += 1
                if g < g1:
                    g += 1
                if b < b1:
                    b += 1
                self.colors_facts[1] = r, g, b

                if self.colors_facts[0] == color_text:
                    self.text_code_change = 3

            elif self.text_code_change == 3:
                if ch_f == 60:
                    if self.counter_fact < self.interesting_facts[self.text_code][7]:
                        self.counter_fact += 1
                    else:
                        self.counter_fact = 0
                        self.text_code_change = 4

            elif self.text_code_change == 4:
                colors_end = [(43, 43, 43), (43, 43, 43)]
                r, g, b = self.colors_facts[0]
                r1, g1, b1 = colors_end[0]
                if self.text_code != 0:
                    if r > r1:
                        r -= 1
                    if g > g1:
                        g -= 1
                    if b > b1:
                        b -= 1
                else:
                    if r < r1:
                        r += 1
                    if g > g1:
                        g -= 1
                    if b > b1:
                        b -= 1
                self.colors_facts[0] = r, g, b

                r, g, b = self.colors_facts[1]
                r1, g1, b1 = colors_end[1]
                if r > r1:
                    r -= 1
                if g > g1:
                    g -= 1
                if b > b1:
                    b -= 1
                self.colors_facts[1] = r, g, b

                if self.colors_facts[0] == colors_end[0]:
                    if self.kil_code == 'kil':
                        self.text_code_change = 666
                    else:
                        self.text_code_change = 5

            elif self.text_code_change == 5:
                colors_start = [(43, 43, 43), (60, 63, 65)]
                r, g, b = self.colors_facts[0]
                r1, g1, b1 = colors_start[0]
                if r < r1:
                    r += 1
                if g < g1:
                    g += 1
                if b < b1:
                    b += 1
                self.colors_facts[0] = r, g, b

                r, g, b = self.colors_facts[1]
                r1, g1, b1 = colors_start[1]
                if r < r1:
                    r += 1
                if g < g1:
                    g += 1
                if b < b1:
                    b += 1
                self.colors_facts[1] = r, g, b

                if colors_start[1] == self.colors_facts[1]:
                    self.text_code_change = 6

            elif self.text_code_change == 6:
                if ch_f == 60:
                    if self.counter_fact < self.time_between_facts:
                        self.counter_fact += 1
                    else:
                        self.counter_fact = 0
                        self.text_code_change = 1

                        '''Выбор факта'''
                        if self.text_code == len(self.interesting_facts) - 1:
                            self.text_code = 0
                        else:
                            self.text_code += 1

                        self.colors_facts[1] = self.interesting_facts[self.text_code][6]
                        self.colors_facts[0] = self.interesting_facts[self.text_code][5]

            elif self.text_code_change == 666:
                colors_start = [(43, 43, 43), (60, 63, 65)]
                r, g, b = self.colors_facts[0]
                r1, g1, b1 = colors_start[0]
                if r < r1:
                    r += 2
                if g < g1:
                    g += 2
                if b < b1:
                    b += 2
                self.colors_facts[0] = r, g, b

                r, g, b = self.colors_facts[1]
                r1, g1, b1 = colors_start[1]
                if r < r1:
                    r += 2
                if g < g1:
                    g += 2
                if b < b1:
                    b += 2
                self.colors_facts[1] = r, g, b


chang_fact = 0
code = 1  # or 2 if that is error
step_code = 0

board = Board(num_cell_x, num_cell_y, cell_size, shift_left, shift_top, k)
k = 0
running = True
op = False
while running:
    chang_fact += 1
    if step_code < 180:
        step_code += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            op = True
            k += 1
            board.loading(k, code)
    if chang_fact % 61 == 0:
        chang_fact = 0
    board.change_of_interesting_facts(chang_fact)
    board.color_change(step_code)
    screen.fill((43, 43, 43))
    board.render(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
