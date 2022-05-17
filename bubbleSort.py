'''
Bubble sort algorithm

Run this in the terminal:
    ./bubbleSort.py
'''

from typing import List


def sort(L: List[int]) -> None:
    '''
    Pre:
        `L` is a list of integers.
        len(L) > 0.
    Post:
        Nothing is returned.

    `L` is sorted in non-descending order, and
    there is nothing returned.
    The parameter `L` should be sorted by the end of the function.
    '''

    noProblem = False
    while not noProblem:
        noProblem = True
        for i in range(len(L) - 1):  # Upto but not including the last element
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                noProblem = False


def isSorted(L: List[int]) -> bool:
    '''
    Pre:
        `L` is a list of integers.
        len(L) > 0.
    Post:
        Return True if `L` is in non-descending order.
        Otherwise, return False.
    
    Check if `L` is sorted in non-descending order.
    '''

    for i in range(len(L) - 1):  # Upto but not including the last element
        if L[i] > L[i+1]:
            return False
    return True

if __name__ == '__main__':

    import random
    
    print("Creating array...")
    L = []
    for _ in range(10):
        L.append(random.randint(0, 1000))
    print("The unsorted array is", end=" ")
    print(L)    
    print("Sorting the array...")
    sort(L)
    print("The sorted array is", end=" ")
    print(L)
    print(f"isSorted = {isSorted(L)}")

            
