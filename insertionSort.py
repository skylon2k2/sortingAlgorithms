'''
Insertion sort algorithm

Run this in the terminal:
    ./insertionSort.py
'''

from typing import List


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
    
    sortedIndex = 1     # Everything is sorted, upto but not including sortedIndex
    currIndex = 1       # The index of the item currently being sorted

    while sortedIndex < len(L):
        while currIndex > 0 and L[currIndex] < L[currIndex - 1]:
            L[currIndex], L[currIndex - 1] = L[currIndex - 1], L[currIndex]
            currIndex -= 1
        sortedIndex += 1
        currIndex = sortedIndex


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
    for _ in range(10):
        L.append(random.randint(0, 1000))
    print("The unsorted array is", end=" ")
    print(L)    
    print("Sorting the array...")
    sort(L)
    print("The sorted array is", end=" ")
    print(L)
    print(f"Sorted = {isNonDescending(L)}")

            