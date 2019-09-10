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

        if '@' in line:
            id = line.split(' ')[1]
            index +=1
            score = lines[index]
            songs[id] = score[:-2].split(' ')
        

        index+=1
    
    return songs



def convert_ngram(songs,n):
    '''
        converts song's score into ngrams
    '''

    songSets = {}
    
    for song in songs:
        
        songScore = songs[song][0:-1] # set(ngsets.ngram(songs[song],0,n))
        ngram = set()
        #make set of ngrams
        for start in range(len(songScore)):
            added = ngsets.ngram(songScore,start,n)
            if len(added) == 0:
                continue
            else:
                ngram.add(tuple(added))
                

        songSets[song] = ngram
    return songSets

def mostSimilar(songs):
    '''
        Finds songs that are most similar
    '''
    most = 0
    mostSongs = []

    for song1 in songs:
        for song2 in songs:
            
            if song1 == song2:
                continue
            
            score1 = songs[song1]
            score2 = songs[song2]
            val = jac.jaccard(score1,score2)
            if val > most:
                most = val
                mostSongs = [song1,song2]

    return (most,mostSongs)


def printDict(dic):

    for x in dic:
        print(x)
        print(dic[x])



def main():

    filename = input("file: ")    
    n = int(input("N: "))
    #filename = 'data.txt'
    #n = 4

    songs = read(filename)
    songs = convert_ngram(songs,n)
    most = mostSimilar(songs)
    
    score = most[0]
    id_num1 = most[1][0]
    id_num2 = most[1][1]

    print("{} {} {:f}".format(id_num1, id_num2, score))


if __name__ == '__main__':
    main()