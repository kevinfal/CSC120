'''
    File: population.py
    Author: Kevin Falconett
    Function: Reads from a dataset with state names and 
        population, adds the numbers up and prints them

    Can be used with pop1.txt without the 3rd column
'''

def sum_pop(fobj):
    """
    extracts population figure from each line in fobj and sums the population figures

    Pararmeters:
        fobj : File object returned by open()

    Returns: 
        int: sum of populaton figures
    """
    value_returned = 0  #value to be returned, total of all populations
    for line in fobj:
        index = 0   #index to search through line
        while(line[index].isalpha() or line[index] == ' '): #character is a space or letter
            index +=1 #move the index past it
        
        temp = line[index: len(line)].strip()   #create a substring from the index and strip it of whitespacee
        value_returned += int(temp) #add the population number to value returned
    return value_returned #return total



def main():
    """
    main function
    """
    #exception handling
    try:
        file = open(input("file: "))
        print(sum_pop(file))
    except: #if the file is invalid, print invalid
        print("invalid file")

if __name__ == '__main__':
    main()
