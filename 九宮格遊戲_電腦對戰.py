import tkinter as tk
from functools import partial
from numpy import random


class NinePalaceGame:
    def __init__(self):
        self.main_game_window = tk.Tk()
        self.main_game_window.title('main game window')
        self.main_game_window.geometry('400x350')

        self.button_group = [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.value_group = [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.player = 'O'
        self.computer = 'X'

        self.create_choose_one_window()
        self.create_billboard()
        self.create_frm()
        self.create_button_and_value_group()
        self.reset()
        self.create_try_again_button()
        self.main_game_window.mainloop()

    def player_play(self, i, j):
        if not self.game_is_over and not self.box[i][j]:
            self.box[i][j] = 1
            self.value_group[i][j].set(self.dominance)
            self.dominance = self.computer

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

    def check_game_over(self):
        for i in range(3):
            for j in range(3):
                if not self.value_group[i][j].get():
                    return 0
        return 1

    def check_win(self, target):
        for i in range(3):
            if self.value_group[i][0].get() == self.value_group[i][1].get() == self.value_group[i][2].get() == target:
                return 1
            if self.value_group[0][i].get() == self.value_group[1][i].get() == self.value_group[2][i].get() == target:
                return 1

        if self.value_group[0][0].get() == self.value_group[1][1].get() == self.value_group[2][2].get() == target:
            return 1
        elif self.value_group[0][2].get() == self.value_group[1][1].get() == self.value_group[2][0].get() == target:
            return 1
        return 0

    def reset(self):
        self.dominance = self.player
        self.game_is_over = False
        self.billboard_value.set('Welcome to nine block game!')
        self.box = [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.value_group[i][j].set("")

        self.main_game_window.withdraw()
        self.choose_one_window.update()
        self.choose_one_window.deiconify()

    def create_billboard(self):
        self.billboard_value = tk.StringVar(
            master=self.main_game_window, value='Welcome to nine block game!')
        self.billboard = tk.Label(self.main_game_window, bg='yellow',
                                  width=40, height=5, textvariable=self.billboard_value)
        self.billboard.pack()

    def button_function(self, i, j):
        self.player_play(i, j)
        self.judge()
        self.computer_play()
        self.judge()

    def create_button_and_value_group(self):
        for i in range(3):
            for j in range(3):
                self.value_group[i][j] = tk.StringVar(
                    master=self.main_game_window, value="")
                self.button_group[i][j] = tk.Button(
                    self.frm, textvariable=self.value_group[i][j], width=7, height=3, command=partial(self.button_function, i, j))
                self.button_group[i][j].grid(row=i+1, column=j+1)

    def create_frm(self):
        self.frm = tk.Frame(self.main_game_window)
        self.frm.pack()

    def create_try_again_button(self):
        self.try_again = tk.Button(self.main_game_window, text='Try again',
                                   width=10, height=3, command=partial(self.reset))
        self.try_again.pack(side='bottom')

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
    game = NinePalaceGame()
