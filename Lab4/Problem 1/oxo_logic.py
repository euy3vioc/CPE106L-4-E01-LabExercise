''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import random
import oxo_data

class OXOGame:
    def __init__(self):
        self.game = list(" " * 9)

    def new_game(self):
        self.game = list(" " * 9)

    def save_game(self):
        oxo_data.saveGame(self.game)

    def restore_game(self):
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.game = game
            else:
                self.new_game()
        except IOError:
            self.new_game()

    def _generate_move(self):
        options = [i for i in range(len(self.game)) if self.game[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self, player):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            if self.game[a] == self.game[b] == self.game[c] == player:
                return True
        return False

    def user_move(self, cell):
        if self.game[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.game[cell] = 'X'
        if self._is_winning_move('X'):
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.game[cell] = 'O'
        if self._is_winning_move('O'):
            return 'O'
        else:
            return ""

    def play_game(self):
        result = ""
        self.new_game()
        while not result:
            print(" {} | {} | {} ".format(self.game[0], self.game[1], self.game[2]))
            print("-----------")
            print(" {} | {} | {} ".format(self.game[3], self.game[4], self.game[5]))
            print("-----------")
            print(" {} | {} | {} ".format(self.game[6], self.game[7], self.game[8]))

            try:
                result = self.user_move(self._generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()

            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(" {} | {} | {} ".format(self.game[0], self.game[1], self.game[2]))
            print("-----------")
            print(" {} | {} | {} ".format(self.game[3], self.game[4], self.game[5]))
            print("-----------")
            print(" {} | {} | {} ".format(self.game[6], self.game[7], self.game[8]))

if __name__ == "__main__":
    game = OXOGame()
    game.play_game()