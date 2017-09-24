#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird

"""
	getAverage(l)
	l - a list of elements
	return sum(l)
"""
def getAverage(l):
	return sum(l)/len(l)

"""
	createList(cap)
	-----------------
	cap - an integer variable that represents the #of elements
	return - The input elements collected into a list.
"""
def createList(cap):
	ans = 0
	elemList = []
	while (cap > 0):
		elem = raw_input("enter element: ")
		elemList.append(float(elem))
		ans = float(elem) + float(ans)
		cap = int(cap) - int(1)
	return elemList

"""
	displayStats(elemList)
	-----------------------
	elemList - a list of all the given elements
	return - nothing.
"""
def displayStats(elemList):
	sumElements=sum(elemList)
	elemList.sort()
	print "Final Score: " + str(sumElements)
	print "Average was: " + str(getAverage(elemList))
	print "Median is: "  + str(int(elemList[(len(elemList)/2)]))
	return 







"""
	variance(l)
	l - a list of elements
"""

def getVariance(l):
	variedList = [] # will hold the modified elements
	avg = getAverage(l)
	numElems = len(l)
	for e in l:
		modMe = e
		print "Element to Be Modifed: " + str(modMe)
		variedList.append((float(modMe-avg) * (float(modMe-avg))))
	
	print "varied List contains " + str(variedList)
# 	print "sum of varied list was: " + str(sum(variedList))
# 	print "the length of the list is: " + str(len(l))
# 	print "and is to be multiplied by: " + str(float(1.0/len(l)))
	
	return (float(1.0/len(l)) * sum(variedList))
	
	
	
###############################################
print "Begin Adder"

#take data
rows = raw_input("please input rows: ")
cols = raw_input("please input cols: ")
totalElements = int(rows) * int(cols)



#Create List and Grab Total
listOfElem = createList(totalElements)

#digest list
displayStats(listOfElem)
 
 

#Construct Grid
print "Sorted grid of " + str(totalElements) + " is: "

count = 0
rowStr  = ""
while (count < (int(totalElements))):
	if(count % int(cols) == 0 and count != 0):
		rowStr += '\n'
	rowStr += str(listOfElem[count]) + ' '
	count += 1

print rowStr
	
	
test = raw_input("calculate variance? (y/n)")

if test is 'y':
	print "variance is: " + str(getVariance(listOfElem))
else:
	print "bummer"
	
	
	