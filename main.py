class Board:
    def __init__(self, weight, height, count_bomb):
        self.weight = weight
        self.height = height
        self.count_bomb = count_bomb
        self.board = [["0" for _ in range(self.weight)] for _ in range(self.height)]
        self.user_board = [["*" for _ in range(self.weight)] for _ in range(self.height)]

    def create_board(self):
        # TODO: Растановка бомб и чисел на поле
        return None

    def open_place(self, x, y):
        # TODO: Открытие клетки
        return None

    def check_bomb(self, x, y):
        # TODO: Поставить метку о бомбе
        return None
