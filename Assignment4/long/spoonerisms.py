'''
    File: spoonerisms.py
    Author: Kevin Falconett

'''


def build_dict(filename):
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

            read = read.strip(remove)
            read = read.upper()
            read = read.split()
            read = strip_phrases(read)
            if read == '':
                continue
            phrases.append(read)
        except:
            break
    
    return phrases

def strip_phrases(phrase):
    '''

    '''
    remove = '?,!)(.-!@#$;%^&*()}{"'
    returned = []
    for i in range(len(phrase)):
        word = phrase[i]
        word = word.strip(remove)
        #word = word.strip(rem)
        returned.append(word)
        
    return returned

def is_valid_word(phonemes, dictionary):
    return phonemes in dictionary

def spoonerisms(phrase,dictionary,proDictionary):
    returned = []

    for wordIndex in range(len(phrase)):
        for wordIndex2 in range(len(phrase)):
            if wordIndex is wordIndex2:
                # word is same
                continue
            

            word1 = phrase[wordIndex]
            word2 = phrase[wordIndex2]
            
            if is_valid_word(word1, dictionary):
                phonemes1 = dictionary[word1]
            else:
                continue
            if is_valid_word(word2, dictionary):
                phonemes2 = dictionary[word2]
            else:
                continue
            
            for phonemeslist1 in phonemes1:
                for phonemeslist2 in phonemes2:

                    for phonIndex1 in range(len(phonemeslist1)):
                        for phonIndex2 in range(len(phonemeslist2)):

                            #print(phonemeslist2[phonIndex2])
                            if phonemeslist2[phonIndex2] != phonemeslist1[phonIndex1]:
                                newPhoneme = phonemeslist1.copy()
                                newPhoneme[phonIndex1] = phonemeslist2[phonIndex2]
                                newPhoneme = tuple(newPhoneme) # tuple because lists aren't hashable

                                # same as first replace
                                newPhoneme2 = phonemeslist2.copy()
                                newPhoneme2[phonIndex2] = phonemeslist1[phonIndex1]
                                newPhoneme2 = tuple(newPhoneme2)

                            # find words for these new phonemes
                            
                                if is_valid_word(newPhoneme,proDictionary):
                                    newWords1 = proDictionary[newPhoneme]
                                    #print("phoneme1 {} word {}".format(newPhoneme,newWords1))

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
    returned = []
    for phrase in phrases:
        returned.append(" ".join(phrase))
    return returned


def build_phonemeDict(dictionary):
    returned = {}

    for word in dictionary:
        for phonemes in dictionary[word]:

            pronounciation = tuple(phonemes)

            if pronounciation in returned.keys():
                # pronounciation has an entry
                returned[pronounciation].append(word)
            else:
                returned[pronounciation] = [word]
        
    return returned


def printOutput(spoonerisms,phrase):
    for x in spoonerisms:
            print(x)

def main():
    filename = input()
    phrases = get_phrases()

    for phrase in phrases:
        if len(phrase) == 0:
            continue
        phraseJoined = " ".join(phrase)

        print('Phrase: {}'.format(phraseJoined))

        dictionary = build_dict(filename)
        dic2 = build_phonemeDict(dictionary)
        result = spoonerisms(phrase,dictionary,dic2)

        result = joinPhrases(result)
        result = sorted(result)

        printOutput(result, phraseJoined)

def debug():

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

        printOutput(result,phraseJoined)
   
        



if __name__ == '__main__':
    main()
    # debug()