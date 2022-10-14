import unittest
from main import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board_5_x_5 = Board(5, 5, 5)
        self.board_1_x_1 = Board(1, 1, 1)
        self.board_3_x_3 = Board(3, 3, 2)

    def test_board_5_x_5(self):
        a = [["*" for _ in range(5)] for _ in range(5)]
        self.assertEqual(self.board_5_x_5.create_board(), a)

    def test_board_1_x_1(self):
        a = [["*" for _ in range(1)] for _ in range(1)]
        self.assertEqual(self.board_1_x_1.create_board(), a)

    def test_board_3_x_3(self):
        a = [["*" for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.board_3_x_3.create_board(), a)


if __name__ == "__main__":
    unittest.main()
