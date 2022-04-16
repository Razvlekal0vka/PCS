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


class Command_line:
    def __init__(self, width, height, size, left, top, k):
        self.left = 0
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения

        # значения по умолчанию
        self.left = left
        self.top = top
        self.cell_size = size

        self.letters_ru = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЫыЭэЮюЯя'
        self.letters_en = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        self.letters_sy = '_-ъь[]|/.,<>?&'
        self.letters_nu = '0123456789'

        self.k = k  # подобия разрешений относительно 800*450

        self.font = pygame.font.SysFont("Comic MS", 20)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pass


command_line = Command_line(num_cell_x, num_cell_y, cell_size, shift_left, shift_top, k)
running = True
op = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # command_line.get_click(event.pos)
            # op = True
            # k += 1
            # command_line.loading(k, code)
    screen.fill((43, 43, 43))
    command_line.render(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
