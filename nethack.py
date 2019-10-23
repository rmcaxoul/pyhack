#!/usr/bin/env python3
import curses
"""
Nethack Game
"""
from random import randint
import curses


class World:
    """
    Properties of the environnement
    """
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.plateau = [[0 for _ in range(xsize)] for _ in range(self.ysize)]

    def addroom(self,room):
        for i in range(room.ybottom - room.ytop):
            for j in range(room.xright - room.xleft):
                try:
                    self.plateau[i + room.ytop][j + room.xleft] = 1
                except:
                    continue
    def display(self, plateau):
        for i in range(self.ysize):
            for j in range(self.xsize):
                if plateau[i][j]:print("#",end ='')
                else: print(".", end ='')
            print()



class Room:
    """
    Preperties of a room
    """
    def __init__(self, world):
        self.xleft = randint(0, world.xsize - 3)
        self.xright = randint(self.xleft + 1, self.xleft + 6)
        self.ybottom = randint(5, world.ysize)
        self.ytop = randint(self.ybottom - 5, self.ybottom - 3)

    def __str__(self):
        return str(self.xleft) + " " + str(self.xright) +" "+ str(self.ytop) +" "+ str(self.ybottom)

class coridoor:
    """
    defines the coridoors
    """
    def __init__(self, room1, room2, plateau):
        print(room1)
        print(room2)
        self.start = (room1.xleft + randint(0,room1.xright - room1.xleft),
        room1.ytop + randint(0,room1.ybottom - room1.ytop))
        self.finish = (room2.xleft + randint(0,room2.xright - room2.xleft),
        room2.ytop + randint(0,room2.ybottom - room2.ytop))
        finalcoord =   [min(self.start[0], self.finish[0]),
                        min(self.start[1], self.finish[1]),
                        max(self.start[0], self.finish[0]),
                        max(self.start[1], self.finish[1])]
        self.xlength = finalcoord[2] - finalcoord[0]
        self.ylength = finalcoord[3] - finalcoord[1]
        print(finalcoord)
        for absc in range(finalcoord[0], finalcoord[2]):
            try:plateau[finalcoord[1]][absc] = 1
            except:pass
        for ordo in range(finalcoord[3] - finalcoord[1]):
            try:plateau[ordo][finalcoord[2]] = 1
            except:pass


def main(stdscr):
    """
    Main of program
    """
    world = World(20,20)
    rooms, coridoors = [], []
    for _i_ in range(2):
        room = Room(world)
        rooms.append(room)
        world.addroom(room)
        if _i_ >= 1:
            coridoors.append(coridoor(prevroom, room, world.plateau))
        prevroom = room
    world.display(world.plateau)



stdsrc = curses.initscr()
curses.noecho()
curses.cbreak()
stdsrc.keypad(True)
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
curses.wrapper(main)
main(stdsrc)
curses.nocbreak()
curses.echo()
stdsrc.keypad(False)
curses.endwin()
