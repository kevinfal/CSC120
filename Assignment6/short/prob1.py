"""
    File: prob1.py
    Author: Kevin Falconett
"""

class Simplest:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third
    def get_first(self):
        return self.first
    def get_second(self):
        return self.second
    def get_third(self):
        return self.third
    
    def rotate(self):
        """moves all elements of rotate"""
        temp = self.first
        self.first = self.second
        self.second = self.third
        self.third = temp

class Band:
    def __init__(self, singer):
        self.singer = singer
        self.drummer = None
        self.guitars = []

    # getters
    def get_singer(self):
        return self.singer
    def get_drummer(self):
        return self.drummer
    def get_guitars(self):
        return self.guitars

    #setters
    def set_singer(self, new_singer):
        self.singer = new_singer
    def set_drummer(self, new_drummer):
        self.drummer = new_drummer
    def add_guitar(self, new_guitar):
        self.guitars.append(new_guitar)
    
    def play_music(self):
        """plays music"""
        if self.singer == "Frank Sinatra":
            print("Do be do be do")
        elif self.singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")

        if self.drummer is not None:
            print("Bang bang bang!")
        
        for guitar in self.guitars:
            print("Strum!")

        