#Project 1 - Problem #2
#Jeff Patra

test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101], 7:[2,213,3,4]}
optional_remainder = [2,3,4,5]

def num_list(test_dict):
	remainder = []
	for key in test_dict:
		if type(key) == str: #list(string.ascii_uppercase): #Accepts dictionary key if value is string
			print test_dict[key]
		else:
			remainder.append(2)
			print remainder

print num_list(test_dict)