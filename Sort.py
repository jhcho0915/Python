# Sort.py
# Project 1: A Battle of Sorts
# Project 1 22
# CSCI 241

# This program contains two sorting functions: Insertion and Selection
# sort  and generates 30 total timings of a selected number of cells in a given
# array ranging from 1000 to 10,0000, each starting from increasing, decreasing
# and randomly ordered cells.

import time
import random
import copy

##############################################################################
# Define the function for the insertion sort method.
def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur

##############################################################################
# Define the function for the selection sort method.
def selection_sort(arr):
    for i in range (len(arr)):
        minIndx = i
        minVal = arr[i]
        j = i + 1
        while j < len(arr):
            if minVal > arr[j]:
                minIndx = j
                minVal = arr[i]
            j += 1
        temp = arr[i]
        arr[i] = arr[minIndx]
        arr[minIndx] = temp
       
##############################################################################

# Test the insertion and selection sort functions with a variety of input 
# arrays to ensure they are sorted correctly and generate 30 timings.
if __name__ == '__main__':
    
# Use copy from import random to remember the first array listed in the group 
# so that when we used selection sort, it did not pull from the already sorted 
# Insertion sort. This also keeps the data consistent when comparing the two 
# sort methods since the unsorted arrays are the same.
    
    array = [1000, 2500, 5000, 7500, 10000]
    
    # Iterate through each test trial
    for x in range(len(array)):
        numberOfCellsInArray = array[x]
        firstArray = [numberOfCellsInArray]
        
        # Determine how to set up the array: Increasing, Decreasing, and Random.
        for y in range(0,3):
            
            if y == 0:
                # perform increasing arrays and copy first array.
                statement = "Increasing"
                firstArray = [None] * numberOfCellsInArray
                for i in range(len(firstArray)):
                    firstArray[i] = i   
                secondArray = copy.deepcopy(firstArray)
                
            if y == 1:
                # First clear your previous array
                statement = "Decreasing"
                firstArray = [None] * numberOfCellsInArray
                
                # perform decreasing arrays and copy first array.
                for i in range(len(firstArray)):
                    firstArray[i] = len(firstArray) - 1 - i
                secondArray = copy.deepcopy(firstArray)
                
            if y == 2:
                # First clear your previous array.
                statement = "Random"
                firstArray = [None] * numberOfCellsInArray
                
                # perform random arrays and copy first array
                for i in range(len(firstArray)):
                    firstArray[i] = random.randint(1, 999)
                secondArray = copy.deepcopy(firstArray)
            
            # Run sorting method for insertion sort and time the results.
            start = time.clock()
            insertion_sort(firstArray)
            end = time.clock()
            print(str(numberOfCellsInArray) + ' ' + statement + ' Insertion Sort: ' + '{:.20f}'\
                  .format(end-start))
            
            # Run sorting method for selectino sort and time the results.
            start = time.clock()
            selection_sort(secondArray)
            end = time.clock()
            print(str(numberOfCellsInArray) + ' ' + statement + ' Selection Sort: ' + '{:.20f}'\
                  .format(end-start))