'''
    File: spoonerisms.py
    Author: Kevin Falconett

'''


def build_dict(filename):
    returned = {}
    file = open(filename)

    first = True
    for line in file:

        # skips first line
        if first:
            first = False
            continue

        
        line = line.strip('\n')
        if(line == ''):
            continue
        
        line = line.split(' ')
        line.remove('')

        word = line[0]

        returned[word] = line[1:]

    return returned

def get_phrases():
    phrases = []
    remove = '?,"!()-.-'
    while True:
        try:
            read = input()

            read = read.strip(remove)
            read = read.upper()
            read = read.split()
            phrases.append(read)
        except:
            break
    
    return phrases

def spoonerisms(phrase,dictionary,proDictionary):
    returned = []
    # iterate index for first word
    for wordIndex in range(len(phrase)):
        # index for second word
        for wordIndex2 in range(len(phrase)):
            if wordIndex is wordIndex2:
                # word is same
                continue
            

            word1 = phrase[wordIndex]
            word2 = phrase[wordIndex2]

            phonemes1 = dictionary[word1]
            phonemes2 = dictionary[word2]
            

            # iterate inside the phonemes
            for phonIndex1 in range(len(phonemes1)):
                # index of first word's phoneme

                for phonIndex2 in range(len(phonemes2)):
                    # index of second word's phoneme

                    # replace replace phoneme at the
                    # first word with the one from the 
                    # second
                    newPhoneme = phonemes1.copy()

                    newPhoneme[phonIndex1] = phonemes2[phonIndex2]
                    #print("newPhoneme {}".format(newPhoneme))

                    newPhoneme = tuple(newPhoneme) # tuple because lists aren't hashable


                    # same as first replace
                    newPhoneme2 = phonemes2.copy()
                    newPhoneme2[phonIndex2] = phonemes1[phonIndex1]
                    newPhoneme2 = tuple(newPhoneme2)

                    # find words for these new phonemes

                    if newPhoneme in proDictionary:
                        newWords1 = proDictionary[newPhoneme]
                    else:
                        continue
                    if newPhoneme2 in proDictionary:
                        newWords2 = proDictionary[newPhoneme2]
                    else:
                        continue

                    # these will be sets of either one or
                    # multiple words
                    
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
        pronounciation = tuple(dictionary[word])

        if pronounciation in returned.keys():
            # pronounciation has an entry
            returned[pronounciation].append(word)
        else:
            returned[pronounciation] = [word]
        
    return returned


def printOutput(spoonerisms,phrase):
    for x in spoonerisms:
        if x != phrase:
            print(x)

def main():
    #filename = 'PronunciationDictionary.txt'
    filename = input()
    phrases = get_phrases()

    for phrase in phrases:
        phraseJoined = " ".join(phrase)
        print('Phrase: {}'.format(phraseJoined))
        dictionary = build_dict(filename)
        dic2 = build_phonemeDict(dictionary)
        result = spoonerisms(phrase,dictionary,dic2)

        result = joinPhrases(result)
        result = result[1:]
        result = sorted(result)
        printOutput(result,phraseJoined)


       
    




if __name__ == '__main__':
    main()