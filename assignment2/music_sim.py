'''
    File: music_sim.py
    Author: Kevin Falconett

'''

import ngram_sets as ngsets
import jaccard as jac


def read(filename):

    songs = {} #{name: score}
    file = open(filename)
    lines = file.readlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        id = 0
        score = ''

        if '@' in line:
            id = line.split(' ')[1]
            index +=1
            score = lines[index]
            songs[id] = score[:-2]
        

        index+=1


    for x in songs:
        print(songs[x])

def main():

    #filename = input("file: ")
    filename = "data.txt"
    #ngram_sz = input("N: ")

    read(filename)

if __name__ == '__main__':
    main()