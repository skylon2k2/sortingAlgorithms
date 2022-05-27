'''
Heap sort algorithm

Terminology
    Max Heap:
        A heap/tree where every child has a value less than or 
        equal to its parent. The largest item is at the root.

                       217, 
        375,                           784, 
   287,         172,             557,         948, 
986, 661,   410


           0
    1             2
 3     4       5     6
7 8   9

          12
  9       10      11
0 1 2   3 4 5   6 7 8

          1
  |       |        |
  2       3        4
| | |   | | |   |  |  |
5 6 7   8 9 10  11 12 13


Run this in the terminal:
    ./heapSort.py
'''

from typing import List
from math import floor, log

def sort(L: List[int]) -> None:
    '''
    Pre:
        `L` is a list of integers.
        len(L) >= 0.
    Post:
        Nothing is returned.

    `L` is sorted in non-descending order, and
    there is nothing returned.
    The parameter `L` should be sorted by the end of the function.

    '''
    buildMaxHeap(L)
    printTree(L)
    lastItem = len(L)-1
    while lastItem > 0:
        L[0], L[lastItem] = L[lastItem], L[0]
        lastItem -= 1
        heapify(L, lastItem+1)


def printTree(L):
    for i, v in enumerate(L):
        print(v, end="   ")
        if log(i+2, 2) == floor(log(i+2, 2)):
            print("")
    print("\n")


def heapify(L: List[int], L_length: int) -> None:
    """
    Creates a max heap from an partly sorted array

    The value that is at the root at the start of this function falls to the 
    bottom of the tree, by repeatedly swapping with the largest child to 
    ensure that the resulting heap is a max heap.
    """
    currIndex = 0
    while (2*currIndex + 1) < L_length:       # There is at least one leaf
        leftChildIndex = 2*currIndex + 1
        rightChildIndex = 2*currIndex + 2
        if rightChildIndex < L_length:
            if max(L[2*currIndex + 1], L[2*currIndex + 2]) > L[currIndex]:       # There are two leaves (easier way is to check parity of len(L), but this is more readable)
                if L[leftChildIndex] >= L[rightChildIndex]:
                    L[currIndex], L[leftChildIndex] = L[leftChildIndex], L[currIndex]
                    currIndex = leftChildIndex
                else:
                    L[currIndex], L[rightChildIndex] = L[rightChildIndex], L[currIndex]
                    currIndex = rightChildIndex
            else:
                break
        else: # There is one leaf
            if L[2*currIndex + 1] > L[currIndex]:
                L[currIndex], L[leftChildIndex] = L[leftChildIndex], L[currIndex]
                currIndex = leftChildIndex
            else:
                break


def buildMaxHeap(L: List[int]) -> None:
    """
    Creates a max heap from an unsorted array

    This function will check every parent and ensure that it is greater  
    than all of its children. Starting with the parent of the last node of the 
    heap, we check whether the max of left and right child is greater than 
    this parent. If it is, then we switch the parent with the larger child.
    """
    if len(L) < 2:
        return None
    currIndex = floor(len(L)/2)-1        # Index of current parent, initialized to final parent
    # If len(L) is even, the last parent has only one child
    if len(L)%2 == 0:       # One child for last parent
        if L[len(L)-1] > L[currIndex]:
            L[len(L)-1], L[currIndex] = L[currIndex], L[len(L)-1]
        currIndex -= 1
    print("after len(L)%2==0\n")
    printTree(L)
    while currIndex >= 0:
        print("\t", currIndex)
        if max(L[(2*currIndex) + 1], L[(2*currIndex) + 2]) > L[currIndex]:
            if L[2*currIndex + 1] > L[2*currIndex + 2]:
                L[2*currIndex + 1], L[currIndex] = L[currIndex], L[2*currIndex + 1]
            else:
                L[2*currIndex + 2], L[currIndex] = L[currIndex], L[2*currIndex + 2]
        currIndex -= 1


def isNonDescending(L: List[int]) -> bool:
    '''
    Pre:
        `L` is a list of integers.
        len(L) >= 0.
    Post:
        Return True if `L` is in non-descending order.
        Otherwise, return False.
    
    Check if `L` is sorted in non-descending order.
    '''
    for i in range(len(L) - 1):  # Upto but not including the last item
        if L[i] > L[i+1]:
            return False
    return True

if __name__ == '__main__':

    import random
    
    print("\tTESTING...\nCreating array...")
    L = []
    for _ in range(7):
        L.append(random.randint(0, 1000))
    print("The unsorted array is", end=" ")
    print(L)    
    print("Sorting the array...")
    sort(L)
    print("The sorted array is", end=" ")
    print(L)
    print(f"Sorted = {isNonDescending(L)}")