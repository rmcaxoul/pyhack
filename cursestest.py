import curses


stdsrc = curses.initscr()
curses.noecho()
curses.cbreak()
stdsrc.keypad(True)
begin_x = 0; begin_y = 0
height = 23; width = 80
win = curses.newwin(height, width, begin_y, begin_x)

#c = stdscr.getch()
print('wq')
curses.nocbreak()
curses.echo()
stdsrc.keypad(False)
curses.endwin()
