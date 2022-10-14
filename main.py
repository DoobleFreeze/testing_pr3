import random


class Board:
    def __init__(self, weight, height, count_bomb):
        self.weight = weight
        self.height = height
        self.count_bomb = count_bomb
        self.board = [[0] * self.weight for _ in range(self.height)]
        self.user_board = [["*"] * self.weight for _ in range(self.height)]

    def create_board(self):
        # TODO: Растановка бомб и чисел на поле
        count_bomb = self.count_bomb
        while count_bomb != 0:
            x = random.randint(0, self.weight - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == 0:
                self.board[y][x] = "b"
                count_bomb -= 1
        for j in range(self.height):
            for i in range(self.weight):
                if self.board[j][i] != "b":
                    if i - 1 >= 0 and j - 1 >= 0 and self.board[j - 1][i - 1] == "b":
                        self.board[j][i] += 1
                    if j - 1 >= 0 and self.board[j - 1][i] == "b":
                        self.board[j][i] += 1
                    if i + 1 < self.weight and j - 1 >= 0 and self.board[j - 1][i + 1] == "b":
                        self.board[j][i] += 1
                    if i - 1 >= 0 and self.board[j][i - 1] == "b":
                        self.board[j][i] += 1
                    if i + 1 < self.weight and self.board[j][i + 1] == "b":
                        self.board[j][i] += 1
                    if i - 1 >= 0 and j + 1 < self.height and self.board[j + 1][i - 1] == "b":
                        self.board[j][i] += 1
                    if j + 1 < self.height and self.board[j + 1][i] == "b":
                        self.board[j][i] += 1
                    if i + 1 < self.weight and j + 1 < self.height and self.board[j + 1][i + 1] == "b":
                        self.board[j][i] += 1
        return self.user_board

    def check_board(self):
        return self.board

    def open_place(self, x, y):
        # TODO: Открытие клетки
        return None

    def check_bomb(self, x, y):
        # TODO: Поставить метку о бомбе
        return None
