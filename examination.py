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


class Board:
    # создание поля
    def __init__(self, width, height, size, left, top):
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

        self.col_examination = 20
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
                                     (198, 117, 49),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)

                elif self.board[j][i] == 2:
                    pygame.draw.rect(screen,
                                     (203, 49, 55),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)


                elif self.board[j][i] == 3:
                    cell_rect = pygame.Rect(self.left + i * self.cell_size, self.top + j * self.cell_size,
                                            self.cell_size, self.cell_size)
                    text = self.font.render(str(self.board_words[i][j]), True, (255, 255, 255))
                    screen.blit(text, (cell_rect.left + 3, cell_rect.top + 3))

                    pygame.draw.rect(screen,
                                     (60, 63, 65),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)

                else:
                    pygame.draw.rect(screen,
                                     (60, 63, 65),
                                     (self.left + self.cell_size * i,
                                      self.top + self.cell_size * j,
                                      self.cell_size, self.cell_size), 6)

                pygame.draw.rect(screen, (43, 43, 43), (
                    self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size), 3)

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
                    print('kilme')
                    '''KILPROC'''

                self.percent -= self.percent_for_step
                self.percent_for_step += percent_for_step

        elif self.col_examination == self.number_of_cells:
            self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
            if self.coord_loading[0] <= self.number_of_cells:
                self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                if self.coord_loading[0] == self.number_of_cells:
                    print('kilme')
                    '''KILPROC'''

        elif self.col_examination < self.number_of_cells:
            self.percent = self.number_of_cells // self.col_examination
            self.rest_of_step = self.number_of_cells % self.col_examination
            for _ in range(self.percent_3):
                self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
                if self.coord_loading[0] <= self.number_of_cells:
                    self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                    if self.coord_loading[0] == self.number_of_cells:
                        print('kilme')
                        '''KILPROC'''
            if self.col_step_3 < self.rest_of_step:
                self.col_step_3 += 1
                self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
                if self.coord_loading[0] <= self.number_of_cells:
                    self.board[self.coord_loading[1]][self.coord_loading[0]] = cod_examination
                    if self.coord_loading[0] == self.number_of_cells:
                        print('kilme')
                        '''KILPROC'''


o = 0
code = 1  # or 2 if that is error

board = Board(num_cell_x, num_cell_y, cell_size, shift_left, shift_top)
k = 0
running = True
op = False
while running:
    k += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            op = True
            o += 1
            board.loading(o, code)
    screen.fill((43, 43, 43))
    board.render(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
