#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jaec
"""

def function(tdarr):
    newArray = [[0] * len(tdarr[0]) for i in range(len(tdarr))]
    for row in range(len(tdarr)):
        for col in range(len(tdarr[row])):
            total = 0
            total += tdarr[(row + 1) % len(tdarr)][col] # down
            total += tdarr[(row + len(tdarr) - 1) % len(tdarr)][col] # up
            total += tdarr[row][(col + len(tdarr[row]) - 1) % len(tdarr[row])] # left
            total += tdarr[row][(col + 1) % len(tdarr[row])] # right
            total += tdarr[(row + 1) % len(tdarr)][(col + len(tdarr[row]) - 1) % len(tdarr[row])] # lower left
            total += tdarr[(row + 1) % len(tdarr)][(col + 1) % len(tdarr[row])] # lower right
            total += tdarr[(row + len(tdarr) - 1) % len(tdarr)][(col + len(tdarr[row]) - 1) % len(tdarr[row])] # upper left
            total += tdarr[(row + len(tdarr) - 1) % len(tdarr)][(col + 1) % len(tdarr[row])] # upper right
            newArray[row][col] = total
    
    print(newArray)

array = [[1,2,4,5],[3,2,1,5],[7,8,10,11]]
function(array)

# arr[row][(col + 1) % len(arr)]