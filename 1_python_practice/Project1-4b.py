#Project1 - Problem 4
#Jeff Patra

import numpy as np

# Provided for loop for i and numbers:
for i in range(5, 15, 2):
	numbers = [x if not x % i == 0 else 0 for x in range(101)]
    

#Function that calculates summary stats for distribution
def summary_stats(i,numbers):
	#num = range(1,number,2)
	diff = len(numbers) - (len(numbers) - i)

	
	print 'The input number i is the %sth number in the range' % (diff) #Not working properly

	if len(numbers) % 2 == 1:
		median = numbers[(len(numbers)+1)/2-1]
	else:
		lower = numbers[len(numbers)/2-1]
		upper = numbers[len(numbers)/2]
		median = numbers[len(numbers)/2]

	print 'The median is: %s' % (median)

	mean = sum(numbers)/len(numbers)
	print 'The mean is: %s' % (mean)


# Call your function here using i and numbers:
print summary_stats(25,numbers)

