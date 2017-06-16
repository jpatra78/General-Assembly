# Project 1 Problem 1
# Jeff Patra

import string
import numpy as np 


input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

#use split.()

def con_or_vow(input_dict):
#	input_dict = {k.lower(): v for k, v in input_dict.items()} #converts keys to lower case
	dict0={}
	dict1 = {}
	lst1=[]
	string_lower = list(string.ascii_lowercase)
	vowels = list('aeiou')
	consonants = list('bcdfghjklmnpqrstvwxyz')
	
	for key in input_dict:
		if type(key) == str: #and key != key.istitle(): #insert another for loop to get rid of Uppercase
			dict0.update({key:input_dict[key]})
		#print key + " : " + dict0[key]
	print dict0

	for key0 in dict0:
		for ch in key0:
			if ch in vowels:
				#type(input_dict[key])=str
				dict1.update({key0:'consonants'})
				#type(input_dict[key])==str:
			else:
				dict1.update({key0:'vowel'}) #Need to fix the else. outputting Uppercase to vowel
	
	print dict1


print con_or_vow(input_dict)