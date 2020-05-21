def init_field(size, empty_sign):
    field = []
    for _row in range(size):
        row = []
        for _column in range(size):
            row.append(empty_sign)
        field.append(row)
    return field


class Game:
    def __init__(self, field, signs):
        self.field = field
        self.sign_x = signs[0]
        self.sign_o = signs[1]
        self.curr_sign = self.sign_x
        self.size = len(field[0])
        self.empty_field = field[0][0]

    def print_field(self):
        print('---------')
        for row in self.field:
            field_line = ''
            for sign in row:
                field_line = field_line + sign + ' '
            print('|', field_line.strip(), '|')
        print('---------')

    def update_field(self, coordinates):
        correct_coordinates = self.check_coordinates(coordinates)
        if correct_coordinates:
            self.field[correct_coordinates[0]][correct_coordinates[1]] = self.curr_sign
            self.curr_sign = self.next_sign()
        return correct_coordinates

    def check_coordinates(self, coordinates):
        for coordinate in coordinates:
            if not coordinate.isnumeric():
                print('You should enter numbers!')
                return []
            if not (1 <= int(coordinate) <= self.size):
                print(f'Coordinates should be from 1 to {self.size}!')
                return []
        column = int(coordinates[0]) - 1
        row = -int(coordinates[1])
        if self.field[row][column] in [self.sign_x, self.sign_o]:
            print('This cell is occupied! Choose another one!')
            return []
        return [row, column]

    def next_sign(self):
        if self.curr_sign == self.sign_x:
            return self.sign_o
        return self.sign_x

    def row_points(self, sign):
        win_point = 0
        for row in self.field:
            if all([sign == point for point in row]):
                win_point += 1
        return win_point

    def column_points(self, sign):
        win_point = 0
        self.print_field()
        for index in range(self.size):
            column = []
            for row in self.field:
                column.append(row[index])
            if all([sign == point for point in column]):
                win_point += 1
        return win_point

    def axis_points(self, sign):
        win_point = 0
        axis = []
        for index in range(self.size):
            axis.append(self.field[index][index])
        if all([sign == point for point in axis]):
            win_point += 1

        axis = []
        column = 0
        row = self.size - 1
        for index in range(self.size):
            axis.append(self.field[row][column])
            column += 1
            row -= 1
        if all([sign == point for point in axis]):
            win_point += 1
        return win_point

    def win_points(self, sign):
        return self.row_points(sign) + self.column_points(sign) + self.axis_points(sign)

    def result(self):
        free_space = any([point == self.empty_field for row in self.field for point in row])
        win_points_x = self.win_points(self.sign_x)
        win_points_o = self.win_points(self.sign_o)

        if win_points_x == 0 and win_points_o == 0 and not free_space:
            print('Draw')
            return True
        elif win_points_x == 1 and win_points_o == 0:
            print(self.sign_x, 'wins')
            return True
        elif win_points_x == 0 and win_points_o == 1:
            print(self.sign_o, 'wins')
            return True
        else:
            print('Impossible')
        return False


game = Game(init_field(3, '_'), ['X', 'O'])
while True:
    game.print_field()

    while True:
        move = input('Enter coordinates: ').split()
        if game.update_field(move):
            break

    if game.result():
        break
