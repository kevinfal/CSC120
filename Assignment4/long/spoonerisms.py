'''
    File: spoonerisms.py
    Author: Kevin Falconett

'''


def build_dict(filename):
    '''
        Creates a dictionary with words
        mapped to pronounciations

        Parameters:
            filename (str): name of dictionary file

        Returns:
            dict(string: [[str]]), word: pronounciation
    '''
    returned = {}
    file = open(filename)

    for line in file:
        
        line = line.strip('\n')
        if(line == ''):
            continue
        
        line = line.split(' ')
        line.remove('')
        word = line[0]

        if word not in returned:
            # word is not yet an entry
            returned[word] = []
        
        returned[word].append(line[1:])
    

    return returned

def get_phrases():
    '''
        Retrieves inputs until they are invalid
        all inputs are guaranteed to be phrases.

        Returns:
            list[list[string]]: list of lists of strings
                                containing the words in
                                the phrases

    '''
    phrases = []
    remove = '?,!)(.-!@#$%^&*()}{"'

    while True:
        try:
            read = input()

            # cleans up string/phrase
            read = read.strip(remove)
            read = read.upper()
            read = read.split()
            read = strip_phrases(read)

            if len(read) == 0:
                continue

            phrases.append(read)

        except:
            break
    
    return phrases

def strip_phrases(phrase):
    '''
        Strips each element in a list
        of strings

        Parameters:
            phrase (list[str]): list of strings/words
        
        Returns:
            list[str] with each string stripped
            of invalid characters 
            removes ?,!)(.-!@#$;%^&*()}{"
    '''

    remove = '?,!)(.-!@#$;%^&*()}{"'
    returned = []
    for i in range(len(phrase)):

        word = phrase[i]
        word = word.strip(remove)

        returned.append(word)
        
    return returned

def is_valid_word(key, dictionary):
    '''
        Determines whether a key is in
        in a dictionary

        Parameters:
            key (any hashable): key to look for
                                    must be hashable
            dictionary (dict): any dictionary
        Returns:
            True is key is in dictionary
    '''
    return key in dictionary

def spoonerisms(phrase,dictionary,proDictionary):
    '''
        Gets every possible spoonerism from
        a phrase and returns a list of them

        Parameters:
            phrase (list[str]): list of words in a phrase
            dictionary (dict): dictionary with strings/words a
                        keys and lists of pronounciations
                        as values
            proDictionary (dict): dictionary with tuples 
                                  representing phonemes and
                                  lists of words as values

        Returns:
            list[list[string]] - a list of lists containing 
                                 each spoonerism of the phrase
                                 split into each list
    '''
    returned = []

    # first word in phrase to swap
    for wordIndex in range(len(phrase)):
        # second word in phrase to swap
        for wordIndex2 in range(len(phrase)):
            if wordIndex is wordIndex2:
                # word is same (index)
                continue
            
            word1 = phrase[wordIndex]
            word2 = phrase[wordIndex2]
            
            # check if word actually exists in dictionary
            if is_valid_word(word1, dictionary):
                # get list of pronounciations
                phonemes1 = dictionary[word1]
            else:
                continue
            if is_valid_word(word2, dictionary):
                phonemes2 = dictionary[word2]
            else:
                continue
            
            # iterate through word1's pronounciations
            for phonemeslist1 in phonemes1:
                # iterate through word2's pronounciations
                for phonemeslist2 in phonemes2:

                    # iterate through phonemes
                    for phonIndex1 in range(len(phonemeslist1)):
                        for phonIndex2 in range(len(phonemeslist2)):
                            
                            # swap
                            if phonemeslist2[phonIndex2] != phonemeslist1[phonIndex1]:
                                newPhoneme = phonemeslist1.copy()
                                newPhoneme[phonIndex1] = phonemeslist2[phonIndex2]
                                newPhoneme = tuple(newPhoneme)# tuple because lists aren't hashable

                                # same as first replace
                                newPhoneme2 = phonemeslist2.copy()
                                newPhoneme2[phonIndex2] = phonemeslist1[phonIndex1]
                                newPhoneme2 = tuple(newPhoneme2)

                                # find words for these new phonemes
                                if is_valid_word(newPhoneme,proDictionary):
                                    newWords1 = proDictionary[newPhoneme]
                                else:
                                    continue
                                if is_valid_word(newPhoneme2, proDictionary):
                                    newWords2 = proDictionary[newPhoneme2]
                                else:
                                    continue

                                # reconstruct phrase with new words
                                for word1Index in range(len(newWords1)):
                                    for word2Index in range(len(newWords2)):
                                        newPhrase = []
                                        for i in range(len(phrase)):
                                            if i == wordIndex:
                                                newPhrase.append(newWords1[word1Index])
                                            elif i == wordIndex2:
                                                newPhrase.append(newWords2[word2Index])
                                            else:
                                                newPhrase.append(phrase[i])

                                        # add the new phrase to returned
                                        if newPhrase not in returned:
                                            returned.append(newPhrase)
                    
    return returned


def joinPhrases(phrases):
    '''
        Joins lists of strings into
        one string for output purposes

        Parameters:
            phrases (list[list[str]]): list of lists
                                       of strings

        Returns:
            list[str] with each string containing the
            elements of the lists of strings in phrases
            joined
    '''
    returned = []
    for phrase in phrases:
        returned.append(" ".join(phrase))
    return returned


def build_phonemeDict(dictionary):
    '''
        Builds a dictionary with pronounciation
        as keys and words as values
        i.e dict(phonemes: words)

        Parameters:
            dictionary (dict): containing words/strings
                               as keys and their pronounciations
                               as the values

        Return:
            dict() - with dictionary's words as values
                     and pronounciations as keys
    '''
    returned = {}

    for word in dictionary:
        for phonemes in dictionary[word]:
            
            # must be a tuple because lists aren't hashable
            pronounciation = tuple(phonemes)

            if pronounciation in returned.keys():
                # pronounciation has an entry
                returned[pronounciation].append(word)
            else:
                returned[pronounciation] = [word]
        
    return returned


def printOutput(spoonerisms):
    '''
        Prints every element in a
        list, but works for any iterable
        
        Parameters:
            spoonerisms list[str]: list of strings can be
                                   any iterable

        Output:
            every element in spoonerisms/iterable
    '''
    for x in spoonerisms:
        if len(x) != 0:
            print(x)

def main():
    '''
        To be used in submission to gradescope.

        Obtains file inputs and phrases, makes
        spoonerisms from those phrases and
        outputs them.
    '''
    filename = input()
    phrases = get_phrases()

    for phrase in phrases:
        if len(phrase) == 0:
            continue
        
        # joined phrase as one string for output
        phraseJoined = " ".join(phrase)

        print('Phrase: {}'.format(phraseJoined))

        dictionary = build_dict(filename)
        dic2 = build_phonemeDict(dictionary)
        result = spoonerisms(phrase,dictionary,dic2)

        # get new phrases in output format
        # and sort
        result = joinPhrases(result)
        result = sorted(result)

        printOutput(result)

def debug():
    '''
        Simulates input of gradescope, enter
        any of the input files and gets the
        proper output
    '''

    inputfile = input("input")
    inputs = open(inputfile)
    dictionaryFile = inputs.readline().strip('\n')
    phrases = []

    
    for line in inputs:
        line = line.strip('?,!)(.-!@#$%^&*()}{"')
        line = line.upper()
        line = line.split()
        line = strip_phrases(line)
        phrases.append(line)

    for phrase in phrases:
        phraseJoined = " ".join(phrase)
        
        if len(phrase) == 0:
            continue
        print('Phrase: {}'.format(phraseJoined))
        
        dictionary = build_dict(dictionaryFile)
        dict2 = build_phonemeDict(dictionary)

        result = spoonerisms(phrase,dictionary,dict2)
        result = joinPhrases(result)
        result = sorted(result)

        printOutput(result)
   
        



if __name__ == '__main__':
    main()
    # debug()