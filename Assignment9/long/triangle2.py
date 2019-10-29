

def triangle2(n):
    if n <= 0:
        return []
    else:
        returned = [fill(1 + sum_num(n -1),n)]
        returned = (triangle2(n-1)) + returned

        return returned

def sum_num(n):
    if n <= 1:
        return n
    else:
        return n + sum_num(n - 1)


def fill(start, n):
    if n <= 0:
        return []
    else:
        returned = [start]
        returned.extend(fill(start + 1, n - 1))
        
        return returned
