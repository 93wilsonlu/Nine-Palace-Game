# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:47:45 2018

@author: christine
"""

import tkinter as tk
from functools import partial


player1 = 'O'
player2 = 'X'
        
#main_game_window
main_game_window = tk.Tk()
main_game_window.title('main game window')
main_game_window.geometry('400x350')

w = ''
#set button text
for i in range(1, 10):
    exec('str' + str(i) + ' = tk.StringVar(master = main_game_window, value = w)')

#set main label
lb_str = tk.StringVar(master = main_game_window, value = 'Welcome to nine block game!')
lb = tk.Label(main_game_window, bg = 'yellow', width = 40, height = 5, textvariable = lb_str)
lb.pack()

#set main frame
frm = tk.Frame(main_game_window)
frm.pack()

t = 0
b = 1
def change_text(string):
    global t
    global b
    
    #change button text
    if b != 0:
        if string.get() == 'O' or string.get() == 'X':
            pass
        else:
            if t == 0:
                string.set(player1)
                t = 1
            elif t == 1:
                string.set(player2)
                t = 0
    
    #judge win or loss
    if ((str1.get() == str2.get() == str3.get() == 'O') or 
        (str4.get() == str5.get() == str6.get() == 'O') or 
        (str7.get() == str8.get() == str9.get() == 'O') or 
        (str1.get() == str4.get() == str7.get() == 'O') or 
        (str2.get() == str5.get() == str8.get() == 'O') or 
        (str3.get() == str6.get() == str9.get() == 'O') or 
        (str1.get() == str5.get() == str9.get() == 'O') or 
        (str3.get() == str5.get() == str7.get() == 'O')):
        lb_str.set('O is win!')
        b = 0
        
    elif ((str1.get() == str2.get() == str3.get() == 'X') or 
        (str4.get() == str5.get() == str6.get() == 'X') or 
        (str7.get() == str8.get() == str9.get() == 'X') or 
        (str1.get() == str4.get() == str7.get() == 'X') or 
        (str2.get() == str5.get() == str8.get() == 'X') or 
        (str3.get() == str6.get() == str9.get() == 'X') or 
        (str1.get() == str5.get() == str9.get() == 'X') or 
        (str3.get() == str5.get() == str7.get() == 'X')):
        lb_str.set('X is win!')
        b = 0
        
    elif (str1.get() and str2.get() and str3.get() and str4.get() and str5.get() and
          str6.get() and str7.get() and str8.get() and str9.get()):
        lb_str.set('Game over!')
        b = 0

#set button
n = 0
for i in range(1, 4):
    for j in range(1, 4):
        n += 1
        exec('b' + str(n) + ' = tk.Button(frm, textvariable = str' + str(n) + ', width = 7, height = 3, command = partial(change_text, str' + str(n) + '))')
        eval('b' + str(n) + '.grid(row = ' + str(i) + ', column = ' + str(j) + ')')
        
def reset():
    global t
    global b
    
    t = 0
    b = 1
    lb_str.set('Welcome to nine block game!')
    r = ''
    for i in range(1, 10):
        eval('str' + str(i) + '.set(r)')
        
try_again = tk.Button(main_game_window, text = 'Try again', width = 10, height = 3, command = partial(reset))
try_again.pack(side = 'bottom')
main_game_window.mainloop()
