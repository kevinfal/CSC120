"""
    File: battleship.py
    Author: Kevin Falconett
    Purpose: Proves the classes Board, Pos, and Ship. Board represents
             a game board, Pos represents a set or coordinates, and 
             ship represents a list of coordinates (ships)
"""


class Board:
    def __init__(self,size):
        self.size = size
        self.map = self.construct_map()
        self.ships = []

    def construct_map(self):
        """
            
        """
        returned = []
        for x in range(self.size):
            returned.append([])
        return self.fill_map(returned)

    
    def fill_map(self, map):
        for row in map:

            for i in range(self.size):
                row.append('.')
        return map
    

    def add_ship(self,ship,position):
        # right now the ship's positions are in the
        # cartesian grid format
        for i in range(len(ship.shape)):
            pos = ship.shape[i]
            pos.x += position.x
            pos.y += position.y
            
            pos = self.translate_coords(pos)
            print(pos)
            ship.shape[i] = pos
        
        added = []
        for pos in ship.shape:
            x = pos.x
            y = pos.y
            self.map[x][y] = ship.name_char
            added.append(self.map[x][y])

        self.ships.append(added)


    def translate_coords(self,pos):
        return Pos(pos.y, pos.x)


    def __str__(self):
        spacer = '   '

        # making the top and bottom border
        top_bot = spacer +'+'
        top_bot += '-'*(self.size * 2)+'-+\n'
        returned = top_bot

        # for numbering
        returned += self.make_rows_str()
    
        returned += top_bot

        # fill the bottom numbering
        bot1,bot2 = self.bot_nums_str()

        if self.size > 10:
            returned += bot1 + bot2
        else:
            returned += bot2
        return returned

    def bot_nums_str(self):
        """
            Makes the bottom rows for the Battleships
        """
        nums = []
        bot1 = "     "
        bot2 = "     "

        for i in range(self.size):
            nums.append(i)

        for num in nums:
            if num < 10:
                bot1 += "  "
                bot2 += str(num) + ' '
            else:
                str_ver = str(num)
                bot1 += str_ver[0] + ' '
                bot2 += str_ver[1] + ' '
        
        return (bot1+'\n', bot2)

    def make_rows_str(self):
        """
            Makes the rows for __str___
        """
        count_down = self.size - 1
        returned = ""
        for x in self.map:
            if count_down > 9:
                returned += str(count_down)+' | ' +' '.join(x) +' |' +"\n"
            else:
                returned += " " +str(count_down) +' | ' +' '.join(x) +' |' +"\n"
            count_down -=1
        
        return returned

    def print(self):
        print(self)

class Ship:
    def __init__(self,name,shape):
        self.name = name
        self.name_char = name[0].upper()
        self.shape = shape
    def Print(self):
        pass

class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def rotate(self,rot):
        assert rot > 0

        if rot == 0:
            return self
        x = self.x
        y = self.y
        
        if rot == 1:  # 90 degrees
            new_y = self.x * -1
            new_x =  self.y
            self.y = new_y
            self.x = new_x
        elif rot == 2:  # 180 degrees
            new_x = self.x * -1
            new_y = self.y * -1
            # y stays the same
            self.x = new_x
            self.y = new_y
        elif rot == 3:  # 270 degrees
            new_y = self.x
            new_x = self.y * -1
            self.y = new_y
            self.x = new_x

        return self

    def __str__(self):
        return str(self.x) +' , ' + str(self.y)


def rotate_shape(shape, rot):
    """Given a shape and a rotation amount (0 through 3, inclusive) return the
       shape after every point has been rotated around the origin.  Note that
       the 'rot' field here has the same semantics as the 'rot' field of the
       Pos.rotate() method: namely, that the value represents how many 90-degree
       clockwise turns to perform.
    """

    if rot == 0:
        return shape

    retval = []
    for pos in shape:
        retval.append(pos.rotate(rot))
    return retval

def Carrier(rot):
    return Ship("Aircraft Carrier",
            rotate_shape([Pos(0,0), Pos(1,0), Pos(2,0), Pos(3,0), Pos(4,0)], rot))

def Basic(rot):
    return Ship("Basic",
            rotate_shape([Pos(0,0)], rot))


def main():
    x = Board(5)
    new = Basic(0)
    x.add_ship(new,Pos(0,0))
    print(x)


if __name__ == "__main__":
    main()