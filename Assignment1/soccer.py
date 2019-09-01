'''
    File: soccer.py
    Author: Kevin Falconett
'''

def getData():
    '''
        Reads data.csv and iterates through each line and
        adds every year and athlete of that year to a dictionary

        Returns: Dictionary containing every year in csv file
            and each athlete of that year
    '''
    file = open("data.csv")

    #dictionary to hold year and name
    soccerData = {}

    for line in file:
        if('#' in line):
            #if the line is a comment, skip iteration
            continue
        else:
            #splits line into a list
            splitLine = line.split(',')
            #we only need indexes 0 (year)
            #and 5 (name)

            year = splitLine[0]
            year = int(year)
            #turn year into an int to make things easier

            athleteOfYr = splitLine[5]
            #add's the year with the athlete's name to the dictionary
            soccerData[year] = athleteOfYr
            
    return soccerData

def getBetweenYrs(data,start,stop):
    '''
        Parameters:
            data (Dictionary): obtained from getData(),
                dictionary of years and athletes of that year
            start (int): starting year obtained from
                input
            stop (int): stop year obtained from input
    '''
    returned = {}
    for year in range(start,stop):
        #iterate through each year between
        returned[year] = data[year]
        #add to a new dictionary

    return returned

def getHighest(data):
    '''
        Finds the players with the most amount of
        athletes of the year and puts them in a
        list
        
        Parameters:
            data (dict): obtained from either getData() or
                getBetweenYrs(), dict of years and athletes
                of those years

        Return:
            Sorted list containing the names of
            the players with the most athletes
            of the year
    '''
    
    
    playerWins = {}
    '''
        This dictionary holds {player: [years]}
    '''

    for year in data:

        #gets the player's name of that year
        player = data[year]
        
        if(player in playerWins):
            #if player is already in playerWins
            playerWins[player].append(year)
            #append to player:[year]
        else:
            #add that player to playerWins
            playerWins[player] = [year]

    #Finding the player(s) with the highest
    #amt of player of the years
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

    #The bounds for years
    MAX_YEAR = 2018
    MIN_YEAR = 1985

    #reads the csv and gets dict of data
    soccerData = getData()

    #collect input and turn into ints
    start = input("start: ")
    stop = input("stop: ")
    start = int(start)
    stop = int(stop)


    if (stop > MAX_YEAR):
        stop = MAX_YEAR


    inRange = (start >= MIN_YEAR and start < MAX_YEAR) and stop > MIN_YEAR
    #start in range and stop is greater than min year

    if(inRange):
        #Only executes if the start and end years are in range

        #dict containing yrs and players between the two years
        #I needed to add 1 to stop because range() isn't inclusive
        between = getBetweenYrs(soccerData, start, stop + 1)
        #finds players with highest # of aotyrs (list)
        highest = getHighest(between)
        for name in highest:
            #prints highest
            print(name)
    
    
