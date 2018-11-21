# Wren Group

import time 
import random
import copy

# Below are the two sorting methods we used, Insertion and Selection sort.

def insertion_sort(arr):
  for k in range(1, len(arr)):
    cur = arr[k]
    j = k
    while j>0 and arr[j-1]>cur:
      arr[j]=arr[j-1]
      j = j-1
      arr[j] = cur

def selection_sort(arr):
    for i in range(len(arr)):
        max = i
        count = i+1
        
        while (count < len(arr)):
            if arr[count] < arr[i]:
                max = count
                temp = arr[max]
                arr[max] = arr[i]
                arr[i] = temp
            count += 1
#______________________________________________________________________________________

if __name__ == '__main__':

#Below are the 30 individual trials. They are grouped by 1000, 2500, 5000, 7500, 10000.
#The arrays are numbered 1-30 and are grouped two more times -- Once by either Increasing,
#Decreasing, or Random, and then again by Insertion or Selection sort. We imported and
#used Copy to remember the first array listed in the group so when we moved on to
#Selection sort, it did not pull from the already sorted Insertion sort. This also keeps
#the data consistent when comparing the two sort methods since the unsorted arrays are =. 

  array_1 = []
  
  for i in range(0,999):
    array_1.append(i)
  array_2 = copy.copy(array_1)
  
start = time.clock()
insertion_sort(array_1)
end = time.clock()

print('1000 Increasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_2)
end = time.clock()

print('1000 Increasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_3 = []

for i in range(999,0,-1):
  array_3.append(i)
array_4 = copy.copy(array_3)

start = time.clock()
insertion_sort(array_3)
end = time.clock()

print('1000 Decreasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_4)
end = time.clock()

print('1000 Decreasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_5 = []
i = 0
while(i<=1000):
  d = random.randint(1,99)
  array_5.append(d)
  i+=1
  
array_6 = copy.copy(array_5)

start = time.clock()
insertion_sort(array_5)
end = time.clock()

print('1000 Random Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_6)
end = time.clock()

print('1000 Random Selection: ' + '{:.20f}'.format(end-start))

#______________________________________________________________________________________

array_7 = []
  
for i in range(0,2500):
  array_7.append(i)
array_8 = copy.copy(array_7)
  
start = time.clock()
insertion_sort(array_7)
end = time.clock()

print('2500 Increasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_8)
end = time.clock()

print('2500 Increasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_9 = []

for i in range(2500,0,-1):
  array_9.append(i)
array_10 = copy.copy(array_9)

start = time.clock()
insertion_sort(array_9)
end = time.clock()

print('2500 Decreasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_10)
end = time.clock()

print('2500 Decreasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_11 = []
i = 0
while(i<=2500):
  d = random.randint(1,99)
  array_11.append(d)
  i+=1
  
array_12 = copy.copy(array_11)

start = time.clock()
insertion_sort(array_11)
end = time.clock()

print('2500 Random Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_12)
end = time.clock()

print('2500 Random Selection: ' + '{:.20f}'.format(end-start))

#______________________________________________________________________________________

array_13 = []
  
for i in range(0,5000):
  array_13.append(i)
array_14 = copy.copy(array_13)
  
start = time.clock()
insertion_sort(array_13)
end = time.clock()

print('5000 Increasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_14)
end = time.clock()

print('5000 Increasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_15 = []

for i in range(5000,0,-1):
  array_15.append(i)
array_16 = copy.copy(array_15)

start = time.clock()
insertion_sort(array_15)
end = time.clock()

print('5000 Decreasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_16)
end = time.clock()

print('5000 Decreasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_17 = []
i = 0
while(i<=5000):
  d = random.randint(1,99)
  array_17.append(d)
  i+=1
  
array_18 = copy.copy(array_17)

start = time.clock()
insertion_sort(array_17)
end = time.clock()

print('5000 Random Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_18)
end = time.clock()

print('5000 Random Selection: ' + '{:.20f}'.format(end-start))

#______________________________________________________________________________________

array_19 = []
  
for i in range(0,7500):
  array_19.append(i)
array_20 = copy.copy(array_19)
  
start = time.clock()
insertion_sort(array_19)
end = time.clock()

print('7500 Increasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_20)
end = time.clock()

print('7500 Increasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_21 = []

for i in range(7500,0,-1):
  array_21.append(i)
array_22 = copy.copy(array_21)

start = time.clock()
insertion_sort(array_21)
end = time.clock()

print('7500 Decreasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_22)
end = time.clock()

print('7500 Decreasing Selection: ' + '{:.20f}'.format(end-start))

#___________________________________

array_23 = []
i = 0
while(i<=7500):
  d = random.randint(1,99)
  array_23.append(d)
  i+=1
  
array_24 = copy.copy(array_23)

start = time.clock()
insertion_sort(array_23)
end = time.clock()

print('7500 Random Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_24)
end = time.clock()

print('7500 Random Selection: ' + '{:.20f}'.format(end-start))

#______________________________________________________________________________________

array_25 = []
  
for i in range(0,10000):
  array_25.append(i)
array_26 = copy.copy(array_25)
  
start = time.clock()
insertion_sort(array_25)
end = time.clock()

print('10,000 Increasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_26)
end = time.clock()

print('10,000 Increasing Selection: ' + '{:.20f}'.format(end-start))

#_____________________________________

array_27 = []

for i in range(10000,0,-1):
  array_27.append(i)
array_28 = copy.copy(array_27)

start = time.clock()
insertion_sort(array_27)
end = time.clock()

print('10,000 Decreasing Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_28)
end = time.clock()

print('10,000 Decreasing Selection: ' + '{:.20f}'.format(end-start))

#_____________________________________

array_29 = []
i = 0
while(i<=10000):
  d = random.randint(1,99)
  array_29.append(d)
  i+=1
  
array_30 = copy.copy(array_29)

start = time.clock()
insertion_sort(array_29)
end = time.clock()

print('10,000 Random Insertion: ' + '{:.20f}'.format(end-start))

start = time.clock()
selection_sort(array_30)
end = time.clock()

print('10,000 Random Selection: ' + '{:.20f}'.format(end-start))

#______________________________________________________________________________________