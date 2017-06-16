#Project 1 - Problem 3
#Jeff Patra

list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]
#list3 = zip(list1, list2)
multiplied =[]
#print list3

def while_loop(list1,list2):
	print 'List 1 is: %s' %list1
	print 'List 2 is: %s' %list2

	x=0
	results = []

	while x <= len(list1):
		x +=1
		print 'Iteration: %s' %x

		for value1, value2 in zip(list1,list2):
			multiplied.append(value1*value2*2)
			if multiplied < 300:
				break

		print multiplied
		print 'Function complete'


		#
		#for a in list1:
		#	for b in list2:
		#		multiplied.append(a * b)
		#print multiplied


print while_loop(list1,list2)
