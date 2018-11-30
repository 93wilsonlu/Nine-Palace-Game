# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:47:45 2018

@author: christine
"""

import random
import tkinter as tk
from functools import partial

main_game_window = tk.Tk()
main_game_window.title('main game window')
main_game_window.geometry('400x350')
main_game_window.withdraw()

#set button text
w = ''
for i in range(1, 10):
    exec('str' + str(i) + ' = tk.StringVar(master = main_game_window, value = w)')

#set main label
lb_str = tk.StringVar(master = main_game_window, value = 'Welcome to nine block game!')
lb = tk.Label(main_game_window, bg = 'yellow', width = 50, height = 5, textvariable = lb_str)
lb.pack()

#set main frame
frm = tk.Frame(main_game_window)
frm.pack()

box = list(range(1, 10))
b = 1
def change_text(string, t):
    global box
    global b
    
    #change button text
    if b != 0:
        if string.get() == 'O' or string.get() == 'X':
            pass
        else:
            string.set(player)
            box.remove(t)
        
    #judge win or loss
    if ((str1.get() == str2.get() == str3.get() == player) or 
        (str4.get() == str5.get() == str6.get() == player) or 
        (str7.get() == str8.get() == str9.get() == player) or 
        (str1.get() == str4.get() == str7.get() == player) or 
        (str2.get() == str5.get() == str8.get() == player) or 
        (str3.get() == str6.get() == str9.get() == player) or 
        (str1.get() == str5.get() == str9.get() == player) or 
        (str3.get() == str5.get() == str7.get() == player)):
        lb_str.set(str(player) + ' is win!')
        b = 0
        
    elif (str1.get() and str2.get() and str3.get() and str4.get() and str5.get() and
          str6.get() and str7.get() and str8.get() and str9.get()):
        lb_str.set('Game over!')
        b = 0
        
    else:
        c = random.choice(box)
        box.remove(c)
        exec('str' + str(c) + '.set(computer)')
        
    if ((str1.get() == str2.get() == str3.get() == computer) or 
        (str4.get() == str5.get() == str6.get() == computer) or 
        (str7.get() == str8.get() == str9.get() == computer) or 
        (str1.get() == str4.get() == str7.get() == computer) or 
        (str2.get() == str5.get() == str8.get() == computer) or 
        (str3.get() == str6.get() == str9.get() == computer) or 
        (str1.get() == str5.get() == str9.get() == computer) or 
        (str3.get() == str5.get() == str7.get() == computer)):
        lb_str.set(str(computer) + ' is win!')
        b = 0
        
    
#set button
n = 0
for i in range(1, 4):
    for j in range(1, 4):
        n += 1
        exec('b' + str(n) + ' = tk.Button(frm, textvariable = str' + str(n) + ', width = 7, height = 3, command = partial(change_text, str' + str(n) + ', ' + str(n) + '))')
        eval('b' + str(n) + '.grid(row = ' + str(i) + ', column = ' + str(j) + ')')

def reset():
    global box
    global b
    lb_str.set('Welcome to nine block game!')
    r = ''
    for a in range(1, 10):
        exec('str' + str(a) + '.set(r)')
    box = list(range(1, 10))
    b = 1
try_again = tk.Button(main_game_window, text = 'Try again', width = 10, height = 3, command = partial(reset))
try_again.pack(side = 'bottom')

choose_one_window = tk.Toplevel(main_game_window)
choose_one_window.title('choose one window')
choose_one_window.geometry('500x500')

label_str = tk.StringVar(master = choose_one_window, value = 'Choose you want')
use_O_or_X = tk.Label(choose_one_window, bg = 'yellow', width = 50, height = 5,
                      textvariable = label_str)
use_O_or_X.pack()

def set_O_or_X(use = None):
    global player
    global computer
    if use == 'X':
        player = 'X'
        computer = 'O'
    elif use == 'O':
        player = 'O'
        computer = 'X'
    choose_one_window.destroy()
    main_game_window.deiconify()
use_O = tk.Button(choose_one_window, text = 'I want use O', width = 40,
                  height = 5, command = partial(set_O_or_X, 'O'))
use_O.pack()
use_X = tk.Button(choose_one_window, text = 'I want use X', width = 40,
                  height = 5, command = partial(set_O_or_X, 'X'))
use_X.pack()

main_game_window.mainloop()
