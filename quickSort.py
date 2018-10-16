import time 
from random import randint 

def partition(array, left, right):

	i = left -1 # This creates and index to the left of the beginning of the partition 
	pivot = array[right] # For simplicity, the rightmost element is the pivot (remember this is an unsorted list so it is most likely not the max value of the array)

	# Loop: If current element is smaller than pivot, move it up an index
	for index in range(left, right):	# Iterates through the partition
		if array[index] <= pivot: 	# if the item we are at is less than the partition then we want to swap it with the element at i 
			'''
			The variable i keeps track of the latest place that we saw an element less than the parition. 
			For example, 

			Example Array: [1, 5, 3, 4]

			On pass 1: index = 0 and the element is 1.
			This is less than the partition of 6 so we increment i to be 0 as well (remember it was left - 1 before)
			We perform the swap below but both indexes are at 1 so nothing happens 

			On pass 2: index = 1, i = 0 from before
			The item at index 1 is 5 which is greater than the pivot so i is not incremented and there is no swap

			On pass 3: index = 2, i = 0
			This element is 3 which is less than 4 for we trigger the conditional statement. 
			This keeps index at 2 but increments i to 1. 
			There is then a swap for 3 and 5, bringing the array to [1,3,5,4] which sorts this partition (with the exception of the pivot last which we don't sort until the next partition)
			'''

			i = i + 1	# This keeps track of the lates intes

			# swap element at i with element at k 
			temp = array[i]
			array[i] = array[index]
			array[index] = temp

	# When we are done with the loop we swap the pivot so we don't keep sorting on one possible pivot (which could be too high or too low)
	temp2 = array[i + 1]
	array[i + 1] = array[right] 
	array[right] = temp2

	# return a new pivot position that is at the location where we have the split between numbers smaller than the previous pivot on the left and larger on the right of i
	return ( i + 1 )



# Recursive implementation of QuickSort 
def quickSort(array, left, right):

	if left < right: # If they are equal that means we have already paritioned the array low enough

		# Partition index is the number we are going to split on
		partInd = partition(array, left, right)

		quickSort(array, left, partInd - 1) # we sort to the right and left of the partition but not on the partition itself
		quickSort(array, partInd + 1, right)





def test():

	arraySmall = [4, 1, 5, 19, 33, 99, 3, 4, 5, 4]
	arrayMedium = []
	arrayLarge = []

	#Keeps track of start time 
	start_time = time.time()

	#Adds random ints to the medium array
	for i in range(0, 10000):
		arrayMedium.append(randint(0,1000))

	for i in range(0, 100000):
		arrayLarge.append(randint(0,1000000))

	#Calls the sort functions
	quickSort(arraySmall, 0, len(arraySmall) -1)

	#Keeps track of elapsed time 
	elapsed_time = time.time() - start_time
	print(elapsed_time)
	print(arraySmall)


test()




















