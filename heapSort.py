'''
Heap sort algorithm

Terminology
    Max Heap:
        A heap/tree where every child has a value less than or 
        equal to its parent. The largest item is at the root.

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
    lastItem = len(L)-1
    while lastItem > 0:
        L[0], L[lastItem] = L[lastItem], L[0]
        lastItem -= 1
        heapify(L, 0, lastItem)


def printTree(L):
    for i, v in enumerate(L):
        print(v, end="   ")
        if log(i+2, 2) == floor(log(i+2, 2)):
            print("")
    print("\n")


def heapify(L: List[int], start: int, end: int) -> None:
    """
    Creates a max heap from an partly sorted array

    The value that is at the root at the start of this function falls to the 
    bottom of the tree, by repeatedly swapping with the largest child to 
    ensure that the resulting heap is a max heap.
    """
    currIndex = start
    while (2*currIndex + 1) < end + 1:       # There is at least one leaf
        leftChildIndex = 2*currIndex + 1
        rightChildIndex = 2*currIndex + 2
        if rightChildIndex < end + 1:
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
    # Note buildMaxHeap should use a similar implementation but we heapify the last parent, and move backwards
    """
    Creates a max heap from an unsorted array

    This function will check every parent and ensure that it is greater  
    than all of its children. Starting with the parent of the last node of the 
    heap, we check whether the max of left and right child is greater than 
    this parent. If it is, then we switch the parent with the larger child.
    """

    for i in range(floor(len(L)/2)):
        heapify(L, floor(len(L)/2)-1-i, len(L)-1)


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
    for _ in range(100):
        L.append(random.randint(0, 1000))
    print("The unsorted array is", end=" ")
    print(L)    
    print("Sorting the array...")
    sort(L)
    print("The sorted array is", end=" ")
    print(L)
    print(f"Sorted = {isNonDescending(L)}")