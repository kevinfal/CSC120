"""
    File: prob3.py
    Author: Kevin Falconett
    Purpose:
"""

import math

class Ball:
    def __init__(self, color, material, diameter):
        self.color = color
        self.material = material
        self.diameter = diameter
        
    def get_color(self):
        return self.color
    def get_material(self):
        return self.material
    def get_diameter(self):
        return self.diameter
    
    def get_volume(self):
        return math.pi * math.pow(self.diameter/2,3) * 4/3

    def paint(self, new_color):
        self.color = new_color

    def bounce(self):
        if self.material.lower() == "stone":
            print("Thud")
        else:
            print("Boing")

    def __str__(self):
        return "Ball(color={}, material={}, diameter={})".format(str(self.color),str(self.material),str(self.diameter))

    def __eq__(self,other):
        this_fields = (self.color,self.material,self.diameter)
        other_fields = (other.color,other.material,other.diameter)
        if self is other:
            return True
        return this_fields == other_fields

def main():
    ball = Ball("Mauve", "StOnE", 10)
    ball2 = Ball("Mauve", "StOnE", 100)
    ball2.bounce()

if __name__ == "__main__":
    main()
