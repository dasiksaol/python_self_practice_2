### Exercise 10: Tic-Tac-Toe Game

# Create a Python class representing a Tic-Tac-Toe game. Implement methods to check for a win, make a move, and display the board.
# box = []
# print(box)
class tictactoe:
    def __init__(self, choice):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.choice = choice
        
    def make_move(self, row, column):
        if self.board[row][column] == " ":
            self.board[row][column] = self.choice
            if self.choice == "X":
                self.choice = "O"
            else:
                self.choice = "X"
        else:
            print("Invalid Move")

    def check_for_win(self):
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
                return True
                
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
                return True
            
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                    return True
                
                elif self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                    return True
            else:
                return False
            
    def show_board(self):
        print(self.board[0], end="\n")
        print(self.board[1], end="\n")
        print(self.board[2], end="\n")

game = tictactoe("X")
game.make_move(0, 1)
game.make_move(0, 2)
game.make_move(0, 0)
game.make_move(2, 2)
game.make_move(2, 0)
game.make_move(1, 2)
game.make_move(1, 1)
game.show_board()
print(game.check_for_win())



# Example usage
# game = TicTacToe()
# game.make_move(0, 0)
# game.make_move(1, 1)
# game.make_move(0, 1)
# game.make_move(2, 2)
# game.make_move(0, 2)
# game.display_board()
# print(game.check_win())