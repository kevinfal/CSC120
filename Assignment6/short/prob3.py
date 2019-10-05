"""
    File: prob3.py
    Author: Kevin Falconett
"""

import math

class Ball:
    def __init__(self, color, material, diameter):
        self.color = color
        self.material = material
        self.diameter = diameter
        
    # getters
    def get_color(self):
        return self.color
    def get_material(self):
        return self.material
    def get_diameter(self):
        return self.diameter
    
    
    def get_volume(self):
        """ calculates volume"""
        return math.pi * math.pow(self.diameter/2,3) * 4/3

    def paint(self, new_color):
        """ changes the color of ball"""
        self.color = new_color

    def bounce(self):
        """prints bounce based off material"""
        if self.material.lower() == "stone":
            print("Thud")
        else:
            print("Boing")

    # implementations
    def __str__(self):
        return "Ball(color={}, material={}, diameter={})".format(str(self.color),str(self.material),str(self.diameter))

    def __eq__(self,other):
        this_fields = (self.color,self.material,self.diameter)
        other_fields = (other.color,other.material,other.diameter)
        if self is other:
            return True
        return this_fields == other_fields

