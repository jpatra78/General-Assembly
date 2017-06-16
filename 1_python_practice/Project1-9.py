#Problem 9A - Load, clean and parse data
#Jeff Patra

#Code credited to Srikanta and Mahendra

import pandas as pd 
import csv

#Using pandas to read csv this problem is much easier
#pokedex = pd.read_csv('C:/Users/Jeff Patra/Documents/DSi/Materials/Project1/pokedex_basic.csv')
#print pokedex.head(3)

filepath = 'C:/Users/Jeff Patra/Documents/DSi/Materials/Project1/pokedex_basic.csv'

raw_pd = ''
with open(filepath, 'r') as f:
	raw_pd = f.read()


pokedex = []

for row in raw_pd.splitlines(): #seperates text file by each line
	line = row.split(",")		#Converts line into list
	temp = []
	for item in line:			
		word = item.replace('"','')	#Replaces the "" of each item in the line
		if word.isdigit():			
			temp.append(float(word))
		elif word == '':
			temp.append(word)
		else:
			temp.append(word)	#Appends clean list into temp
	pokedex.append(temp)		#Appends all the clean lines into final list

for s in pokedex:
	print s


#*****************************************************
#Problem 9B - Does the same thing as 9A but with list comprehension

with open(filepath, 'r') as f:
    raw_pd = f.read()
    raw_pd = raw_pd.replace('"','')
    pokedex1 = [[float(word) if word.isdigit() else word if word =='' else word for word in line.split(",")] for line in raw_pd.splitlines()]
    
for p in pokedex1:
	print p