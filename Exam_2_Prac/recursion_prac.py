




def rev_evens(L):
    if L ==[]:
        return []
    else:
        returned = []
        if L[0] % 2 != 0:
            returned = [L[0]]
        returned.extend(rev_evens(L[1:]))
        return returned


def main():
    x = [1,2,3]
    result = rev_evens(x)
    print(result)


if __name__ == "__main__":
    main()