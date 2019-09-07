"""
    File: ngram.py
    Author: Kevin Falconett
    Purpose: Construct a list of ngrams
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


def main():
    list = input("list:")
    start = input("start")
    length = input("length")
    post = ngram(list, start, length)
    print(post)


if __name__ == "__main__":
    main()
