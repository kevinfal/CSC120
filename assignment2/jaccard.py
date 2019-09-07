'''
    File: Jaccard.py
    Author: Kevin Falconett
    Purpose: Calculate Jaccard Index of two sets

'''

def jaccard(set1, set2):
    '''
        Calculates the jaccard index of two sets

        Parameters:
            set1 (set): set of any kind
            set2 (set): set of any kind

        Returns:
            (float): Jaccard index of the two sets
    '''

    if len(set1) == 0 and len(set2) == 0:
        #if both sets are empty
        return 1.0
        
    intersect = len(set1.intersection(set2))
    #gets how many elements are same

    union = len(set1.union(set2))
    #amouont of unique elements total

    return intersect/union

def main():
    set1 = input("Set 1: ")
    set2 = input("Set 2: ")

    result = jaccard(set1, set2)
    #calculate jaccard Index

    print(result)

if __name__ == '__main__':
    main()
    