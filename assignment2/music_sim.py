"""
    File: music_sim.py
    Author: Kevin Falconett
    Purpose: read music scores, create ngrams from them,  
             and return the most similar using their 
             jaccard indices
"""

import ngram_sets as ngsets
import jaccard as jac


def read(filename):
    """
        Reads from the text file, assigns each score to their id
        in a dictionary.

        Parameters:
            filename (string): name of the text file containing scores
        
        Return:
            dict(string:list): dictionary containing each song's id
                            and corresponding score

    """

    songs = {}  # {name: score}
    file = open(filename)
    lines = file.readlines()

    index = 0
    while index < len(lines):
        line = lines[index]

        if "@" in line:
            id = line.split(" ")[1]
            index += 1

            score = lines[index]  # .strip('~')
            songs[id] = score[:-2].split(" ")

        index += 1

    return songs


def convert_ngram(songs, n):
    """
        Converts song's score into ngrams of length n contained
        within tuples inside a set

        Parameters:
            songs (dict{string:list}): holds id of song
                                    and corresponding score as ngrams
            n (int): length of ngrams
        Return:
            dict{string:set}: holds id of song and ngrams
                            as a set of tuples
    """

    songSets = {}

    for song in songs:

        songScore = songs[song][0:-1]
        ngram = set()

        # make set of ngrams
        for start in range(len(songScore)):

            # creates ngram
            added = ngsets.ngram(songScore, start, n)

            if len(added) == 0:
                continue
            else:
                ngram.add(tuple(added))

        songSets[song] = ngram

    return songSets


def mostSimilar(songs):
    """
        Finds the two songs that are the most
        similar according to their jaccard indices

        Parameters:
            songs (dict{string:set}): dictionary with
                         song ids and scores 
                        (after being converted into a set of 
                        tuples)
        Return:
            tuple() containing the highest jaccard
                    index, and the ids of the
                    two songs that produced it
    """

    most = 0
    mostSongs = []

    # compare every song to one another
    for song1 in songs:
        for song2 in songs:

            if song1 == song2:
                continue

            score1 = songs[song1]
            score2 = songs[song2]

            val = jac.jaccard(score1, score2)
            if val > most:
                most = val
                mostSongs = [song1, song2]

    return (most, mostSongs)


def main():

    filename = input("file: ")
    n = int(input("N: "))

    songs = read(filename)
    songs = convert_ngram(songs, n)
    most = mostSimilar(songs)

    score = most[0]
    id_num1 = most[1][0]
    id_num2 = most[1][1]
    print("{} {} {:f}".format(id_num1, id_num2, score))


if __name__ == "__main__":
    main()
