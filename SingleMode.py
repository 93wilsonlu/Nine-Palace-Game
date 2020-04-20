import tkinter as tk
from functools import partial
from numpy import random
from base import NinePalaceGame


class SingleMode(NinePalaceGame):
    player1 = player = 'O'
    player2 = computer = 'X'

    def __init__(self):
        self.create_choose_one_window()
        super().__init__()

        self.main_game_window.mainloop()

    def player_play(self, i, j):
        if not self.game_is_over and not self.box[i][j]:
            self.box[i][j] = 1
            self.value_group[i][j].set(self.dominance)
            self.dominance = self.computer
            return 1
        return 0

    def computer_play(self):
        if not self.game_is_over:
            while 1:
                i, j = random.choice(range(3)), random.choice(range(3))
                if not self.box[i][j]:
                    self.box[i][j] = 1
                    self.value_group[i][j].set(self.computer)
                    self.dominance = self.player
                    break

    def judge(self):
        if self.check_win(self.player):
            self.game_is_over = 1
            self.billboard_value.set('Player is win!')
        elif self.check_win(self.computer):
            self.game_is_over = 1
            self.billboard_value.set('Computer is win!')
        elif self.check_game_over():
            self.game_is_over = 1
            self.billboard_value.set('Game over!')

    def reset(self):
        super().reset()
        self.dominance = self.player
        self.box = [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.main_game_window.withdraw()
        self.choose_one_window.update()
        self.choose_one_window.deiconify()

    def button_function(self, i, j):
        if self.player_play(i, j):
            self.judge()
            self.computer_play()
            self.judge()

    def set_O_or_X(self, use):
        self.player = use
        if use == 'X':
            self.computer = 'O'
            self.computer_play()
        else:
            self.computer = 'X'
        self.dominance = self.player
        self.choose_one_window.withdraw()
        self.main_game_window.update()
        self.main_game_window.deiconify()

    def create_choose_one_window(self):
        self.choose_one_window = tk.Toplevel(self.main_game_window)
        self.choose_one_window.title('choose one window')
        self.choose_one_window.geometry('500x500')

        choose_one_window_billboard = tk.StringVar(
            master=self.choose_one_window, value='Choose you want')
        use_O_or_X = tk.Label(self.choose_one_window, bg='yellow', width=50,
                              height=5, textvariable=choose_one_window_billboard)
        use_O_or_X.pack()

        use_O = tk.Button(self.choose_one_window, text='I want use O', width=40,
                          height=5, command=partial(self.set_O_or_X, 'O'))
        use_O.pack()
        use_X = tk.Button(self.choose_one_window, text='I want use X', width=40,
                          height=5, command=partial(self.set_O_or_X, 'X'))
        use_X.pack()


if __name__ == '__main__':
    game = SingleMode()
