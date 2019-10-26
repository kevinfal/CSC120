"""
    File: xchg.poy
    Author: Kevin Falconett
"""

def xchg(l):
    if len(l) <= 0:
        return []
    elif len(l) == 1:
        return [l[0]]
    else:
        returned = [l[1],l[0]]
        returned.extend(xchg(l[2:]))
        return returned

if __name__ == "__main__":
    a = [1,2,3]
    print(xchg(a))
    