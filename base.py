import tkinter as tk
from functools import partial


class NinePalaceGame:
    main_game_window = tk.Tk()
    player1 = 'O'
    player2 = 'X'
    value_group = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    button_group = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self):
        self.main_game_window.title('main game window')
        self.main_game_window.geometry('400x350')

        self.create_billboard()
        self.create_frm()
        self.create_button_and_value_group()
        self.create_try_again_button()
        self.reset()

    def button_function(self, i, j):
        pass

    def player_play(self, i, j):
        pass

    def computer_play(self):
        pass

    def judge(self):
        pass

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
        self.game_is_over = 0
        self.billboard_value.set('Welcome to nine block game!')
        for i in range(3):
            for j in range(3):
                self.value_group[i][j].set("")

    def create_billboard(self):
        self.billboard_value = tk.StringVar(
            master=self.main_game_window, value='Welcome to nine block game!')
        self.billboard = tk.Label(self.main_game_window, bg='yellow',
                                  width=40, height=5, textvariable=self.billboard_value)
        self.billboard.pack()

    def create_button_and_value_group(self):
        for i in range(3):
            for j in range(3):
                self.value_group[i][j] = tk.StringVar(
                    master=self.main_game_window, value="")
                self.button_group[i][j] = tk.Button(self.frm, textvariable=self.value_group[i][j], width=7, height=3, command=partial(
                    self.button_function, i, j))
                self.button_group[i][j].grid(row=i+1, column=j+1)

    def create_frm(self):
        self.frm = tk.Frame(self.main_game_window)
        self.frm.pack()

    def create_try_again_button(self):
        self.try_again = tk.Button(self.main_game_window, text='Try again',
                                   width=10, height=3, command=partial(self.reset))
        self.try_again.pack(side='bottom')
