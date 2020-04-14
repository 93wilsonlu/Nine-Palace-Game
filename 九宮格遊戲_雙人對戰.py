import tkinter as tk
from functools import partial


class NinePalaceGame:
    def __init__(self):
        self.main_game_window = tk.Tk()
        self.main_game_window.title('main game window')
        self.main_game_window.geometry('400x350')
        self.player1 = 'O'
        self.player2 = 'X'

        self.value_group = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.button_group = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.create_billboard()
        self.create_frm()
        self.create_button_and_value_group()
        self.create_try_again_button()
        self.reset()
        self.main_game_window.mainloop()

    def change_text(self, i, j):
        if not self.game_is_over and not self.value_group[i][j].get():
            self.value_group[i][j].set(
                self.player1 if self.dominance_on_player1 else self.player2)
            self.dominance_on_player1 = not self.dominance_on_player1

        self.game_is_over = True
        if self.check_win('O'):
            self.billboard_value.set('O is win!')
        elif self.check_win('X'):
            self.billboard_value.set('X is win!')
        elif self.check_game_over():
            self.billboard_value.set('Game over!')
        else:
            self.game_is_over = False

    def check_game_over(self):
        for i in range(3):
            for j in range(3):
                if not self.value_group[i][j].get():
                    return 0
        return 1

    def check_win(self, target: str) -> bool:
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
        self.dominance_on_player1 = 1
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
                    self.change_text, i, j))
                self.button_group[i][j].grid(row=i+1, column=j+1)

    def create_frm(self):
        self.frm = tk.Frame(self.main_game_window)
        self.frm.pack()

    def create_try_again_button(self):
        self.try_again = tk.Button(self.main_game_window, text='Try again',
                                   width=10, height=3, command=partial(self.reset))
        self.try_again.pack(side='bottom')


if __name__ == '__main__':
    game = NinePalaceGame()
