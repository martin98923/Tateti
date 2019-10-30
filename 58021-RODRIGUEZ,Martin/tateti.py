class TaTeTi():

    def __init__(self, tabla=None):
        if not tabla:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = tabla

    def full(self):
        return " " not in self.board

    def win(self):
        if self.board[0] == self.board[1] and self.board[0] == self.board[2] and self.board[2] != " ":
            return True

        elif self.board[3] == self.board[4] and self.board[3] == self.board[5] and self.board[5] != " ":
            return True

        elif self.board[6] == self.board[7] and self.board[6] == self.board[8] and self.board[8] != " ":
            return True

        elif self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[8] != " ":
            return True

        elif self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[6] != " ":
            return True

        elif self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[6] != " ":
            return True

        elif self.board[1] == self.board[4] and self.board[1] == self.board[7] and self.board[7] != " ":
            return True

        elif self.board[2] == self.board[5] and self.board[2] == self.board[8] and self.board[8] != " ":
            return True

        else:
            return False

    def validate(self, position):
        return self.board[position-1] == " "

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position-1] = piece
        else:
            raise Exception

    def draw_board(self):
        self.display = "\n"
        for num in range(9):
            if self.board[num] != " ":
                self.display += " " + self.board[num] + " "
            else:
                self.display += " " + str(1+num) + " "
            if num == 2 or num == 5:
                self.display += "\n---+---+---\n"
            elif num == 8:
                self.display += "\n"
            else:
                self.display += "|"

        return self.display