"""
    File: prob2.py
    Author: Kevin Falconett
"""

def bounds(num):
    """ checks if number is within bounds"""
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num

class Color:
    def __init__(self,r,g,b):
        self.r = bounds(r)
        self.g = bounds(g)
        self.b = bounds(b)
    def __str__(self):
        return("rgb({},{},{})".format(self.r,self.g,self.b))
    def html_hex_color(self):
        """ returns rbg value of color"""
        return("#{:02X}{:02X}{:02X}").format(self.r,self.g,self.b)
    def get_rgb(self):
        return (self.r,self.g,self.b)
    def set_rgb(self,r,g,b):
        self.r = bounds(r)
        self.g = bounds(g)
        self.b = bounds(b)
    def remove_red(self):
        """removes all red from color"""
        self.r = 0
    def set_standard_color(self,name):
        """sets the color to a standard one i.e Red"""
        name = name.upper()

        if name == "RED":
            self.set_rgb(255,0,0)
        elif name == "YELLOW":
            self.set_rgb(255, 255, 0)
        elif name == "WHITE":
            self.set_rgb(255,255,255)
        elif name == "BLACK":
            self.set_rgb(0,0,0)
        else:
            print("ERROR: Color.set_standard_color(): Invalid color name: {}"
            .format(name))
    

    