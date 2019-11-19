"""spoonerisms.py

Author: Russ Lewis

Purpose: Reads in a Pronunciation Dictionary (format-compatible with the
         one provided by CMU) and then a list of phrases.  Builds
         an exhaustive list of all possible Spoonerisms for each phrase.

         In truth, "exhaustive" is too agressive a claim; in fact, this
         is limited to some very particular spoonerisms: those that
         involve swapping individual phonemes between different words in
         the phrase.  It cannot move multiple phonemes, insert or delete.
         It also cannot detect puns, if they are not real words.

         Perhaps worst of all, it doesn't have any filtering to sort out
         minimal changes, which can lead to disappointing results.
"""



import sys



def read_input_file():
    """Prompts the user for a filename.  Then opens the file, parses the
lines (skipping blank lines).  Returns a list of tuples; each tuple is
a spelled word, followed by a pronunciation (where the pronunciation is
a tuple of strings, each string being one phoneme).
"""

    retval = []

    with open(input()) as input_file:
        for line in input_file:
            line = line.strip()
            if line[0] == '#' or len(line) == 0:
                continue

            words = line.split()
            spelled  = words[0]
            phonemes = tuple(words[1:])

            retval.append( (spelled, phonemes) )

    return retval



def build_maps(entries):
    """Given a list of entries (as returned by read_input_file() ),
builds two dictionaries: one that maps spelled words to sets of
pronunciations, and one that maps pronunciations to sets of spelled
words.  None of the returned sets are empty, but many may have only
a single element.
"""

    forward  = {}
    backward = {}

    for spelled,phonemes in entries:
        if spelled not in forward:
            forward[spelled] = set([phonemes])
        else:
            forward[spelled].add(phonemes)

        if phonemes not in backward:
            backward[phonemes] = set([spelled])
        else:
            backward[phonemes].add(spelled)

    return (forward,backward)



def do_spoonerisms(words, forward,backward):
    """Given a phrase and the two dictionaries, parses the phrase, searches for
all possible spoonerisms, and then prints the result.  The input phrase must be
a list of strings, with all of the words pre-strip()ed to remove the
puncuation which the spec requires that we ignore.
"""

    results = set()

    # outer two loops: iterate over all pairs of words in the input, skipping
    # over any words not in the dictionary.
    #
    # Since we will need to modify the input list (by index), the variables
    # here are the indices into the list of words provided as input.
    #
    # Note that since we are looking for pairs from a common data set (the
    # same string of words), the inner loop starts at w1+1, instead of 0.
    # This means we don't have to worry about duplicate operations.

    for w1 in range(len(words)):
        if words[w1] not in forward:
            continue

        for w2 in range(w1+1, len(words)):
            if words[w2] not in forward:
                continue

            # next two loops: for the pair of words chosen, iterate over all
            # combinations of pronunciations (that is, phonemes); each word
            # might have several pronunciations.
            #
            # The variables here are the pronunciations themselves.

            for ph1 in forward[words[w1]]:
                for ph2 in forward[words[w2]]:

                    # next two loops: for the two pronunciations chosen,
                    # choose one phoneme from each word; skip over any
                    # combinations where the chosen phonemes are identical.
                    #
                    # Since we will need to modify the pronunciations, the
                    # indices here are the indices into the respective
                    # pronunciations.
                    #
                    # Note that since the two loops are iterating over
                    # *different* sets, each of them starts at 0 (unlike w2)

                    for i in range(len(ph1)):
                        for j in range(len(ph2)):
                            move1 = ph1[i]
                            move2 = ph2[j]

                            if move1 == move2:
                                continue

                            # build the updated phoneme list for each of the
                            # modified words
                            #
                            # REMEMBER: The syntax (x,) builds a tuple with
                            #           a single element.  We need that so
                            #           that concatenation is legal here.

                            ph_changed1 = ph1[:i]+(move2,)+ph1[i+1:]
                            ph_changed2 = ph2[:j]+(move1,)+ph2[j+1:]

                            # reject any changes which result in either word
                            # not being in the dictionary

                            if ph_changed1 not in backward:
                                continue
                            if ph_changed2 not in backward:
                                continue

                            # last nested loop: for each (modified) phoneme
                            # list, there might be multiple possible spellings.

                            for new_word1 in backward[ph_changed1]:
                                for new_word2 in backward[ph_changed2]:

                                    # update the word list, making the two
                                    # replacements.  Then, add the resulting
                                    # string to our overall list.
                                    #
                                    # I need to honor the 80-character
                                    # line limit.  But a big chain of
                                    # concatenation would be nice here.

                                    words_changed  = words[:w1]
                                    words_changed += [new_word1]
                                    words_changed += words[w1+1:w2]
                                    words_changed += [new_word2]
                                    words_changed += words[w2+1:]
                                    results.add(" ".join(words_changed))

    print("Phrase: " + " ".join(words))
    for line in sorted(results):
        print("  "+line)



def main():
    # this reads the raw data from the file
    entries    = read_input_file()

    # we build two maps (for each version of the dataset): one maps
    # spellings to phonemes (forward), and the other maps phonemes
    # back to spellings (backward)
    (forward   , backward   ) = build_maps(entries)


    for line in sys.stdin:
        # parse the line, splitting the words and removing punctuation
        words = line.upper().split()
        for i in range(len(words)):
            words[i] = words[i].strip(",.;:!?-()'\"")

        if len(words) == 0:
            continue

        do_spoonerisms(words, forward,backward)



main()

