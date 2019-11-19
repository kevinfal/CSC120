"""
    File: battleship.py
    Author: Kevin Falconett
    Purpose:
"""


class Board:
    def __init__(self,size):
        self.size = size
        self.map = self.construct_map()

    def construct_map(self):
        returned = []
        for x in range(self.size):
            returned.append([])
        return returned

    def add_ship(self,ship,position):
        


class ship:
    def __init__(self,name,ship):
        self.name = name
        self.ship = ship
    def Print(self):
        pass

class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def rotate(self,rot):
        pass