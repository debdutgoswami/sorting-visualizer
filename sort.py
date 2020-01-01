def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def bubblesort(A):
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A

def insertionsort(A):
    for i in range(1, len(A)): 
        key = A[i] 

        j = i-1
        while j >=0 and key < A[j] :
            swap(A, j, j+1)
            j -= 1
            yield A

def selectionsort(A):
    for i in range(len(A)-1):
        pos = i
        for j in range(i+1, len(A)):
            if A[j]<A[pos]:
                pos = j
        if pos!=i:
            swap(A, pos, i)
        yield A