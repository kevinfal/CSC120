"""
    File: pop_chg.py
    Author: Kevin Falconett
    Purpose: Read a File containing state names and populations, 
            then calculate the difference and print out the state(s) with 
            the highest population growth

    To be used with pop1.txt
"""


def GetStates(file):
    """
        Parameters:
            file: txt file from open()
        Return:
            returned (list[List]): returns a list of lists 
                    with a state's name and population change

            returned format: [ [StateName, PopChange] , [] , [] ]
    """

    stateData = []

    for line in file:

        # to store the state's name and pop difference
        tempArr = []

        # if line has a comment '#'
        if "#" in line:
            # skips this iteration
            continue
        index = 0
        while line[index].isalpha() or line[index] == " " or line[index] == ".":
            # character is a space or letter
            index += 1  # move the index past space/letter

        temp = line[index : len(line)].split()
        # creates a substring from the index and strip it of whitespace
        # index 0 will be 2019, index 1 will be 2010

        # getting the state's proper name
        stateName = line[:index]

        # removing empty spaces in the name
        index2 = 0
        endIndex = 0
        while (
            stateName[index2].isalpha()
            or stateName[index2] == " "
            or stateName[index2] == "."
        ):
            # while the character is a letter, space, or .

            # loops until index 2 finds more than 2 spaces in the string,
            # signifying the end of the name
            if stateName[index2] == " " and stateName[index2 + 1] == " ":
                # the current index is a space and the following one is too
                endIndex = index2
                break
            else:
                index2 += 1

        stateName = stateName[:endIndex]
        tempArr.append(stateName)
        # calculating the population change and adding it to list
        # chg = (2019_popn - 2010_popn)/2010_popn
        tempArr.append((int(temp[0]) - int(temp[1])) / int(temp[1]))
        stateData.append(tempArr)

    return stateData


def FindHighest(stateData):
    """
        Parameter: 
            stateData: State Data, 2d list with each list containing a state's name and population change
    """
    highest = []
    if len(highest) == 0:  # highest is empty
        highest.append(stateData[0])
    for state in stateData:
        if state == highest[0][1]:
            # state is exact same as the first state
            continue
        elif state[1] < highest[0][1]:
            # state is less than the current highest
            continue
        # state is greater or higher
        else:
            if state[1] > highest[0][1]:  # state is higher
                highest = []  # reset highest and add the state
                highest.append(state)

            # the state and the current highest are equal and add to highest list
            else:
                highest.append(state)

    # remove duplicates in the list
    highest = RemoveDupes(highest)
    return highest


def RemoveDupes(array):
    """
        Removes duplicates in an array

        Parameters:
            array: any list
        
        Return:
            returned (List): a list without any duplicates
    """
    returned = []
    for x in array:
        # iterate through each element
        # and add them to the returned list if not in already
        if x not in returned:
            returned.append(x)
    return returned


def PrintStates(states):
    """
        Print function to print the states

        Parameters:
            states (List): list of states, 
            can be attained through GetStates() or FindHighest()

        Void
    """
    for state in states:
        state_name = state[0]
        state_change = state[1]
        print("{}: {:f}".format(state_name, state_change))


if __name__ == "__main__":
    """
        Main
    """
    stateData = GetStates(open(input("file: ")))
    highest = FindHighest(stateData)
    PrintStates(highest)
