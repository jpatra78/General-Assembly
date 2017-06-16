#Project1 - Problem 4
#Jeff Patra

#Function that calculates summary stats for distribution

def summary_stats(i,number):
	num = range(1,number,2)
	diff = len(num) - (len(num) - i)

	print num
	if diff == 1:
		print 'The number %s is the %sst number between 1 and %s' % (i, diff, number)
	elif diff == 2:
		print 'The number %s is the %snd number between 1 and %s' % (i, diff, number)
	elif diff == 3:
		print 'The number %s is the %srd number between 1 and %s' % (i, diff, number)
	else: 
		print 'The number %s is the %sth number between 1 and %s' % (i, diff, number)

	if len(num) % 2 == 1:
		median = num[(len(num)+1)/2-1]
	else:
		lower = num[len(num)/2-1]
		upper = num[len(num)/2]
		median = num[len(num)/2]

	print 'The calculated median between 1 and %s is: %s' % (number, median)

	mean = sum(num)/len(num)
	print 'The calculated mean between 1 and %s is: %s' % (number, mean)

print summary_stats(1,15)

