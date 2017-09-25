#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird
import math

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
def displayStats(l):
	sumElements=sum(l)
	l.sort()
	print "Final Score: " + str(sumElements)
	print "Average was: " + str(getAverage(l))
	print "Median is: "  + str(int(l[(len(l)/2)]))
	print "Variance is: " + str(getVariance(l))
	print "Standard Deviation is: " + str(getStdDev(l))
	print "Mean Absolute Deviation: " + str(getMeanDeviance(l))
	print "Range is: " + str(getRange(l))
	
	return 

"""
	getRange(l)
	-----------------
	l - a list of elements
	return - the difference between the largest and smallest elements
"""
def getRange(l):
	l.sort()
	return float(abs(l[len(l)-1] - l[0]))

"""
	getMeanDeviance(l)
	l - a list of elements
	return - whatever the f a mean Deviance is. (sum of the difference)^2
	"""
def getMeanDeviance(l):
	meanDevList = [] # will hold the modified elements
	avg = getAverage(l)
	numElems = len(l)
	for e in l:
		modMe = e
		meanDevList.append((abs(float(modMe-avg))))

	return (float(1.0/len(l)) * sum(meanDevList))

"""
	variance(l)
	l - a list of elements
	return - the variance of the data set!
"""
def getVariance(l):
	variedList = [] # will hold the modified elements
	avg = getAverage(l)
	numElems = len(l)
	for e in l:
		modMe = e
		variedList.append((float(modMe-avg) * (float(modMe-avg))))
		
	return (float(1.0/len(l)) * sum(variedList))
		
"""
	getStdDev(l)
	--------------
	l - a list of elements
	return - the Standard Deviation
"""
def getStdDev(l):
	return math.sqrt(getVariance(l))
		
	
###############################################
print "Begin Adder"

#take data
rows = raw_input("please input rows: ")
cols = raw_input("please input cols: ")
totalElements = int(rows) * int(cols)



#Create List and Grab Total
listOfElem = createList(totalElements)

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

#digest list
displayStats(listOfElem)	
	