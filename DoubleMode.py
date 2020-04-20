from base import NinePalaceGame


class DoubleMode(NinePalaceGame):
    def __init__(self):
        super().__init__()
        self.main_game_window.mainloop()

    def player_play(self, i, j):
        if not self.game_is_over and not self.value_group[i][j].get():
            self.value_group[i][j].set(
                self.player1 if self.dominance_on_player1 else self.player2)
            self.dominance_on_player1 = not self.dominance_on_player1

    def button_function(self, i, j):
        self.player_play(i, j)
        self.judge()

    def judge(self):
        if self.check_win('O'):
            self.game_is_over = 1
            self.billboard_value.set('O is win!')
        elif self.check_win('X'):
            self.game_is_over = 1
            self.billboard_value.set('X is win!')
        elif self.check_game_over():
            self.game_is_over = 1
            self.billboard_value.set('Game over!')

    def reset(self):
        super().reset()
        self.dominance_on_player1 = 1


if __name__ == '__main__':
    game = DoubleMode()
