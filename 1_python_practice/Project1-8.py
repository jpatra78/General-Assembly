# Problem #8. Three funstions that will clean up a dictionary

#Function 1 cleans dicitonary  where key =string and value != list
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

def string_intlist_cleaner(d): # d is a dictionary
	string_intlist_dict = {k:v for k,v in d.iteritems() if type(k) == str and type(v)!=list} # list comp that removes string and list from dictionary

	return string_intlist_dict

print string_intlist_cleaner(first_dict)

#Function 2 cleans dictionary where key != integer and value != string

def int_string_cleaner(d): # d is a dictionary
	int_string_dict = {k:v for k,v in d.iteritems() if type(k) != int and type(v)!=str} # list comp that removes string and list from dictionary

	return int_string_dict

print int_string_cleaner(second_dict)

#Function 3 cleans dictionary. Accepts two dictionaries. First dictionary cleaned with Function 1. Second dicitonary cleaned with function 2..  Combine the two dictionars.

def dict_cleaner(first_dict, second_dict):
	print first_dict
	print second_dict

	#clean first dict using string_intlist_cleaner function
	clean_dict1 = string_intlist_cleaner(first_dict)
	#clean second dict using int_string_cleaner
	clean_dict2 = int_string_cleaner(second_dict)

	#Combine cleaned dictionaries
	dict3 = clean_dict1.update(clean_dict2)
	print dict3

dict_cleaner(first_dict, second_dict)

