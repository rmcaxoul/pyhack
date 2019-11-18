#!/usr/bin/env python3
from time import sleep
import curses

from curses import wrapper

def adds(stdscr, x, y):
    stdscr.addstr(x,y,"hi")

def main(stdscr):
    # Clear screen
    stdscr.clear()
    adds(stdscr, 1 , 1)
    stdscr.refresh()
    stdscr.addstr(8,9,'tesdt')
    sleep(3)
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
