'''
    File: letter_swaps.py
    Author: Kevin Falconett
    Purpose: swaps every possible
             character in a string
'''

def swap(i1,i2,string):
    '''
        Swaps the letters at string[i1]
        and string[i2]

        Parameters:
            i1 (int): first index
            i2 (int): second index
            string (str): string to
                          perform swap
        
        Returned:
            (str) with characters
            swapped

        
    '''
    
    letter1 = string[i1]
    letter2 = string[i2]
    returned = ''

    # reconstructs string, swaps
    # when index is i1 or i2
    for i in range(len(string)):
        if i == i1:
            returned += letter2
        elif i == i2:
            returned += letter1
        else:
            returned += string[i]

    return returned


def letter_swaps(text):
    '''
        gets all possible swaps
        of a string and returns them
        in a list

        Parameters:
            text (str): string to swap

        Returns:
            list[str] containing all
            possible swaps
    '''

    returned = []

    for i1 in range(len(text)):
        for i2 in range(len(text)):

            letter1 = text[i1]
            letter2 = text[i2]

            if letter1 == letter2:
                continue
            
            swapped = swap(i1,i2,text)

            if swapped in returned:
                continue
            else:
                returned.append(swapped)
    
    return sorted(returned)


def main():
    result = letter_swaps(input("Text: "))
    print(result)

if __name__ == '__main__':
    main()