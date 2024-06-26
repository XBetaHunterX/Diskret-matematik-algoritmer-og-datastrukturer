# A is the array, x is the element location which is to be inserted into
def linear_hashing_find_aux(A, x):
    possible = []
    m = len(A)
    for i in range(m):
        for j in range(m):
            position = (i + j) % m
            if A[position] == None and position == x:
                possible.append(i)
            if (A[position] == None and position != x):
                break

    return possible

# A is the array, x is the element location which is to be inserted into
# h1 and h2 are the hash functions (Auxiliary hash functions). Leave the one you have to find as None
def double_hashing_find_aux(A, x, h1, h2):
    possible = []
    m = len(A)

    if (h1 == None):
        for i in range(m):
            for j in range(m):
                position = (i + j * h2) % m
                if A[position] == None and position == x:
                    possible.append(i)
                if (A[position] == None and position != x):
                    break

    elif (h2 == None):
        for i in range(m):
            for j in range(m):
                position = (h1 + j * i) % m
                if A[position] == None and position == x:
                    possible.append(i)
                if (A[position] == None and position != x):
                    break

    return possible


if __name__ == '__main__':
    possible = double_hashing_find_aux([13, 56, None, 32, 91, None, 82,None], 5, 3, None)
    print(possible)