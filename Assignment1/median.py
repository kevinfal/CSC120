'''
    File: median.py
    Author: Kevin Falconett
    Function: determine whether a string is even or odd in length and print the middle two characters if even or
        the middle one if odd
'''

if __name__ == "__main__":

    string = input("input: ")

    if(len(string) % 2 == 0 ):#if the length of the string is even
        #string to be printed
        printed = string[(len(string) // 2) - 1] + string[len(string) // 2]
        print(printed) #print middle two characters
    else: #length is odd
        print(string[len(string) // 2]) #print just the middle character
        
