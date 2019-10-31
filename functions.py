def swapPositions(A, pos1, pos2): 
    A[pos1], A[pos2] = A[pos2], A[pos1] 
    return A
def dad(i):
    return int(i/2)

def left(i):
    return int(i*2)

def right(i):
    return int(i*2 + 1)

def max_heapify(A, i, size_heap ):
    l = left(i)
    r = right(i)
    if l <= size_heap and A[l] > A[i] :
        best = l
    else:
        best = i
    
    if r <= size_heap and A[r] > A[best] :
        best = r
    if best != i :
        A = swapPositions(A,i,best)
        max_heapify(A,best,size_heap)
    return A

def build_max_heap(A):
    length = len(A)-1
    size_heap = length
    for i in range(int(length/2), 0, -1):
        max_heapify(A,i,size_heap)
    return length, size_heap

def heapSort(A):
    length, size_heap = build_max_heap(A)
    for i in range(length, 0, -1):
        swapPositions(A,1,i)
        size_heap -= 1
        max_heapify(A,1,size_heap)
    return A