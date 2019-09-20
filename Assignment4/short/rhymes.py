'''
    File: rhymes.py
    Author: Kevin Falconett
    Purpose: Finds if two phonemes of
             words are perfect rhymes
'''

def findStress(phonemes):
    '''
        Finds the index of the
        stress phoneme in a list of
        strings (phonemes)

        Parameters:
            list[str]: list of strings that
                       represent phonemes
            
        Returns:
            (int) index of stress phoneme
            in list
        
        Precondition:
            list contains a stress
            phoneme (a string with a
            number).

            Will return None if not
            present
    '''

    for i in range(len(phonemes)):
        for letter in phonemes[i]:

            if not letter.isalpha():
                return i
    return None  # stress is not present

def rhymes(phonemes1, phonemes2):
    '''
        Find if the phonemes 1 and 2
        are perfect rhymes

        Parameters:
            phonemes1 (list[str]): list
                                   of strings representing
                                   phonemes of a word
            phonemes1 (list[str]): list
                                   of strings representing
                                   phonemes
                                
        Returns:
            True if before the stress
            phoneme is different on both
            and after the stress on both
            is the same

            False if before the stress
            phoneme is the same
    '''

    stress1 = findStress(phonemes1)
    stress2 = findStress(phonemes2)
    
    beforeStress1 = phonemes1[:stress1]
    beforeStress2 = phonemes2[:stress2]

    afterStress1 = phonemes1[stress1:]
    afterStress2 = phonemes2[stress2:]

    if beforeStress1 == beforeStress2:
        return False
    
    elif afterStress1 == afterStress2:
        return True

    return False


def main():

    p1 = input('Phonemes 1: ')
    p2 = input('Phonemes 2: ')

    result = rhymes(p1,p2)
    print(result)

if __name__ == '__main__':
    main()