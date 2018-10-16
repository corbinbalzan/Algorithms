import time
from random import randint

def insertionSort(array):

	# iterate over the array by each item 
	# Start at 1 since we can consider the first item to be sorted off the bat 

	for i in range (1, len(array)):
		temp = array[i] 	# Holds the element we are looking at through our interation 
		j = i - 1 	# Keeps track of the item before the index of the array that we are currently at (this item is sorted)

		while (j >= 0 and temp < array[j]):	# iterate while we are above the -1 index and while our current item at index i is less than the array preceding it
			'''
			Example array: [1,5,6,4,6]
			Iteration Example: [1,5,6,4,6] 	
			We are at the index of 3 where the element 4 is. 
			This element is stored in temp so temp = 4. 
			We then do the while loop and see that 4 needs to be moved so 
			we make space by copying the previous element to the 4 spot
			Example: [1,5,6,6,6] The 4 is gone but stored in temp 
			Now we do another iteration [1,5,5,6,6]
			There are now two 5s and the correct amount of 6's
			Now we are at the spot where temp is greater than 1 so 
			we break the loop and assign temp as the next spot over after the loop
			'''
			array[j + 1] = array[j] 	# if the element we are looking at is smaller than its proceeding element, meaning it needs to be sorted, then we make space on the proceeding side
			j = j - 1 	# Move over to observe the next item 

		array[j+1] = temp # places the number we are trying to sort after the number that broke the loop
	return array 

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
	insertionSort(arraySmall)

	#Keeps track of elapsed time 
	elapsed_time = time.time() - start_time
	print(elapsed_time)
	print(arraySmall)


test()






