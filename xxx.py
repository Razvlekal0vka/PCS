def loading(self, step_examination):
    number_of_cells = self.number_of_cells
    col_examination = self.col_examination
    self.percent += (step_examination / col_examination - self.percent)
    self.percent_for_step = col_examination / number_of_cells

    print(self.percent_for_step)
    print(self.percent)

    if self.percent >= self.percent_for_step:
        self.percent -= self.percent_for_step
        self.coord_loading = [self.coord_loading[0] + 1, self.coord_loading[1]]
        if self.coord_loading[0] <= 26:
            self.board[self.coord_loading[1]][self.coord_loading[0]] = 1
        if self.coord_loading[0] == 26:
            pass
            '''KILPROC'''