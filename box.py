import copy


class Cell:
    # 单元格左上角坐标 x 值
    x: float
    # 单元格左上角坐标 y 值
    y: float
    # 单元格高度
    height: float
    # 单元格宽度
    width: float
    # 单元格值，默认为 0
    value: int

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.value = 0


class Box:
    # 窗口宽
    window_width: int
    # 窗口高
    window_height: int
    # 行数
    row_num: int
    # 列数
    col_num: int
    cells: [[Cell]]

    def __init__(self, row_num: int, col_num: int, win_width: int, win_height: int):
        self.window_height = win_height
        self.window_width = win_width
        self.row_num = row_num
        self.col_num = col_num
        self.cells: [[Cell]] = []
        for row in range(0, self.row_num):
            tmp: [Cell] = []
            for col in range(0, self.col_num):
                cell = Cell(
                    row * (self.window_width / self.row_num),
                    col * (self.window_height / self.col_num),
                    self.window_width / self.row_num,
                    self.window_height / self.col_num,
                )
                tmp.append(cell)
            self.cells.append(tmp)
        return

    # 获取指定的 cell
    # row、col 允许为负值，负值时将根据地图的连接进行计算得到正值
    def get_cell(self, row: int, col: int) -> Cell:
        if row < 0:
            row = row % self.row_num - 1
        if row >= self.row_num:
            row = row % self.row_num
        if col < 0:
            col = col % self.col_num - 1
        if col >= self.col_num:
            col = col % self.col_num
        return self.cells[row][col]

    # 获取所有单元
    def get_all_cells(self) -> [Cell]:
        cells = []
        for rows in self.cells:
            for cell in rows:
                cells.append(cell)
        return cells

    # 根据自动机规则，刷新状态
    # 返回状态变更了的单元
    def flush(self) -> [Cell]:
        old_box = copy.deepcopy(self)
        # 需要变更状态的单元
        update_cells_index = []
        # 遍历所有单元，更新值
        for row in range(0, self.row_num):
            for col in range(0, self.col_num):
                # 读取周围8个单元值
                cur = old_box.get_cell(row, col)
                top = old_box.get_cell(row - 1, col)
                left = old_box.get_cell(row, col - 1)
                bottom = old_box.get_cell(row + 1, col)
                right = old_box.get_cell(row, col + 1)
                top_left = old_box.get_cell(row - 1, col - 1)
                bottom_left = old_box.get_cell(row + 1, col - 1)
                top_right = old_box.get_cell(row - 1, col + 1)
                bottom_right = old_box.get_cell(row + 1, col + 1)
                # 存活的节点数量
                surviving_count = top.value \
                                  + left.value \
                                  + bottom.value \
                                  + right.value \
                                  + top_left.value \
                                  + bottom_left.value \
                                  + top_right.value \
                                  + bottom_right.value
                if cur.value == 1:
                    if surviving_count < 2:
                        # 生命稀少，挂了
                        update_cells_index.append([row, col])
                    if surviving_count > 3:
                        # 生命数量过多，挂了
                        update_cells_index.append([row, col])
                if cur.value == 0:
                    if surviving_count == 3:
                        # 生命繁衍
                        update_cells_index.append([row, col])
        update_cells = []
        # 执行状态值变更
        for index in update_cells_index:
            if self.cells[index[0]][index[1]].value == 1:
                self.cells[index[0]][index[1]].value = 0
            else:
                self.cells[index[0]][index[1]].value = 1
            update_cells.append(self.cells[index[0]][index[1]])
        return update_cells
