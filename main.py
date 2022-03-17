""" A TicTacToe with machine learning
"""


class TicTacToe():
    """_summary_
    """

    def __init__(self):
        self.board = []
        self.board_width = 3
        self.board_height = 3

    #global board_height, board_width

    def create_board(self):
        """_summary_
        """

        for i in range(self.board_width):
            row = []
            for j in range(self.board_height):
                row.append('▯')
            self.board.append(row)
            print(self.board)

    def win_condition(self):
        """_summary_
        """


if __name__ == "__main__":
    c = TicTacToe()
    c.create_board()
    c.win_condition()
