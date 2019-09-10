"""
    File: ngram_sets.py
    Author: Kevin Falconett
    Purpose: Construct a set of ngrams
"""


def ngram(arglist, startpos, length):
    """
        Returns n-gram from a list of strings

        Arguments:
            arglist (list[String]): list of strings
            startpost (int): 
            length (int): 

        Returns:
            list of strings from index startpos of arglist to approriate length

        Preconditions:
            n >= 0
    """
    if startpos < 0:
        # if starting index is negative, convert it to it's positive index
        startpos += len(arglist)

    if startpos + length <= len(arglist):
        return arglist[startpos : startpos + length]
    else:
        # cannot make an ngram with the indices
        return []


def ngram_sets(string, n):
    """
        Creates a set of ngrams

        Parameters:
            string (str): string
            n (int): length of ngrams
        
        Return:
            set of ngrams
        
        Preconditions:
            n >= 0
    """

    if string == "":
        return "set()"

    string = string.split(" ")
    ngrams = collect(string, n)
    ngrams = convert(ngrams)
    ngrams = set(ngrams)
    return ngrams


def collect(strings, n):
    """
        Parameters:
            strings (list[str]): list of strings
            n (int): length of desired ngrams
        Returns:
            (list) list of all possible ngrams of length n in strings
    """
    returned = []

    for startpos in range(len(strings) * -1, len(strings)):
        # start at negative index to get every possible ngram

        added = ngram(strings, startpos, n)
        # construct ngram

        if len(added) == 0:
            continue
        elif added in returned:
            continue
        returned.append(added)
    return returned

def collectToEnd(strings,n):
    """
        Parameters:
            strings (list[str]): list of strings
            n (int): length of desired ngrams
        Returns:
            (list) list of all possible ngrams of length n in strings
    """
    returned = []

    for startpos in range(0, len(strings)):
        # start at negative index to get every possible ngram

        added = ngram(strings, startpos, n)
        # construct ngram

        if len(added) == 0:
            continue
        elif added in returned:
            continue
        returned.append(added)
    return returned



def convert(ngrams):
    """
        Converts 2d list containing strings (ngrams) to a list containing tuples with 
        the same strings (ngrams)

        Parameters:
            ngrams (list[list][string]): 2d list of lists 
                            containing strings (or ngrams)

        Return:
            list[tuple(string)]: list of tuples containing strings
    """
    returned = []

    for ngram in ngrams:
        returned.append(tuple(ngram))
    return returned


def main():
    string = input("String: ")
    arg = int(input("Arg: "))
    result = ngram_sets(string, arg)
    print(result)


if __name__ == "__main__":
    main()
