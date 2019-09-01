'''
    File: soccer.py
    Author: Kevin Falconett
'''

def getData():
    file = open("data.csv")
    ##Year,Matches,Wins,Draws,Losses,Athlete of the year,Scoring leader,No. of goals by leader,Assist leader,No. of assists by leader,Coach,Major tournament result
    #[0] = year
    #[5] = athlete of the year #
    #
    soccerData = {}
    for line in file:
        if('#' in line):
            #if the line is a comment, skip iteration
            continue
        else:
            splitLine = line.split(',')
            year = splitLine[0]
            year = int(year)
            athleteOfYr = splitLine[5]
            soccerData[year] = athleteOfYr
            
    return soccerData

def getBetweenYrs(data,start,stop):
    returned = {}
    for year in range(start,stop):
        returned[year] = data[year]
    return returned

def getHighest(data):
    
    playerWins = {}
    for year in data:

        player = data[year]
        if(player in playerWins):
            playerWins[player].append(year)
        else:
            playerWins[player] = [year]
    
    highest = []

    for player in playerWins:
        if(len(highest) == 0):
            highest.append(player)
        else:
            if(len(playerWins[highest[0]]) == len(playerWins[player])):
                highest.append(player)
            elif(len(playerWins[player]) > len(playerWins[highest[0]])):
                highest = [player]
    return sorted(highest)



if __name__ == '__main__':
    #main

    MAX_YEAR = 2018
    MIN_YEAR = 1985

    soccerData = getData()

    start = input("start: ")
    stop = input("stop: ")
    start = int(start)
    stop = int(stop)

    inRange = (start >= MIN_YEAR and start < MAX_YEAR) and (stop <= MAX_YEAR and stop > MIN_YEAR)
    if(inRange):
        between = getBetweenYrs(soccerData, start, stop + 1)
        highest = getHighest(between)
        for name in highest:
            print(name)
    
    
