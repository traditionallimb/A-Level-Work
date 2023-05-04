
def mergeSort(array):
	if len(array) > 1:
		midpoint = len(array) // 2  # gets midpoint of the array with integer division
		rSplit = array[midpoint:]  # splits array in relation to the midpoint
		lSplit = array[:midpoint]
		print(f"Left split: {lSplit}\nRight Split: {rSplit}")

		mergeSort(rSplit)  # runs this subroutine within itself to split the lists more
		mergeSort(lSplit)

		rSplitTracker = lSplitTracker = arrayTracker = 0  # just simple number trackers

		# until the end of either rSplit or lSplit is reached, pick the larger among the elements and then place them
		# in the correct position in array
		while rSplitTracker < len(rSplit) and lSplitTracker < len(lSplit):
			if rSplit[rSplitTracker] < lSplit[lSplitTracker]:
				array[arrayTracker] = rSplit[rSplitTracker]
				rSplitTracker += 1
			else:
				array[arrayTracker] = lSplit[lSplitTracker]
				lSplitTracker += 1
			arrayTracker += 1

		# when elements have been run out of in the rSplit and lSplit lists it picks up the remaining elements and then
		# places them in array
		while rSplitTracker < len(rSplit):
			array[arrayTracker] = rSplit[rSplitTracker]
			rSplitTracker += 1
			arrayTracker += 1

		while lSplitTracker < len(lSplit):
			array[arrayTracker] = lSplit[lSplitTracker]
			lSplitTracker += 1
			arrayTracker += 1


def printList(array):
	for i in range(len(array)):
		print(array[i], end=" ")
	print()


sortList = [7, 5, 9, 13, 25, 2, 1, 8, 25, 13, 6]
mergeSort(sortList)
printList(sortList)
