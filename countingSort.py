import time 
from random import randint

def countingSort(array):
	
	maxValue = max(array) + 1	# Finds max value to use for counting array

	# Build counting array
	countArray = [0] * maxValue

	# Stores the count of an item from array in the new count array by incrementing the value by 1
	for item in array: 
		countArray[item] += 1

	# Store a count that we use to iterate over new array 
	count = 0 

	# Iterates over every possible value in the count array 
	for possibleItem in range(maxValue):
		''' Grabs the number from the stored count in countArray 
		for each instance of that number it adds it to the new array. 
		Example Numeric Array: [3,3,1]
		Example Count Array: [0,1,0,2]
		This means that if there are two instances 
		of the number 3, then the 3's will be added on after the other.
		'''
		for j in range(countArray[possibleItem]):
			array[count] = possibleItem
			count += 1 # moves to the next index in the new array so we don't add two elements to one spot

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
	countingSort(arraySmall)

	#Keeps track of elapsed time 
	elapsed_time = time.time() - start_time
	print(elapsed_time)
	print(arraySmall)


test()






