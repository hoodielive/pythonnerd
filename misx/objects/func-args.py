def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")
banner("Sun, Moon and Stars", "*")

import time 

def show_default(arg=time.ctime()):
    print(arg)

show_default() # never progresses because def binds the function
               # will only run once

def add_spam(menu = []):
    menu.append("spam")
    return menu

add_spam('avacado')
add_spam('avacado')

def add_spam_better_way(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

add_spam_better_way('avacado')
add_spam_better_way('avacado')


