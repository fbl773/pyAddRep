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
		elem = raw_input()
		elemList.append(float(elem))
		ans = float(elem) + float(ans)
		cap = int(cap) - 1
	return elemList

"""
	displayStats(elemList)
	-----------------------
	elemList - a list of all the given elements
	return - nothing.
"""
def getStats(l):
	sumElements=sum(l)
	statStr=""
	statStr += "Summation is: " + str(sumElements)
	statStr += "\nAverage is: " + str(getAverage(l))
	statStr += "\nMedian is: "  + str(getMedian(l))
	statStr +=  "\nVariance is: " + str(getVariance(l))
	statStr +=  "\nStandard Deviation is: " + str(getStdDev(l))
	statStr +=  "\nMean Absolute Deviation: " + str(getMeanDeviance(l))
	statStr +=  "\nRange is: " + str(getRange(l))
	
	return statStr

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
		
"""
	getMedian(l)
	-------------
	l - a list of elements
	return if even, 2 middle most averaged
			else, middle most element
	
"""
def getMedian(l):
	center = len(l)/2 # yes I'm mad i used american "center" not the proper centre, but its written...
	if(len(l)%2 == 0):
		return (float(l[center-1]) + float(l[center]))/2.0
	else:
		return float(l[center])

"""
	makeGrid(l)
	l - a list of elements
	return a string that represents the data as a matrix/list
"""
def makeGrid(l):
	count = 0
	print "lenght of list is: " + str(int(len(l)))
	rowStr  = "\n"
	while (count < len(l)):
		if(count % int(cols) == 0 and count != 0):
			rowStr += '\n'
		rowStr += str(listOfElem[count]) + ' '
		count += 1

	return rowStr

"""
	sortList(l):
	l - a list of elements.
	return a sorted list (hopefully)
"""
def sortList(l):
	l.sort()
	return l



###############################################
print "Begin Adder"

#take data
rows = raw_input()
cols = raw_input()



#Create List and Grab Total
listOfElem = createList(int(rows)*int(cols))
print "unsorted is: " + makeGrid(listOfElem)
print " \nsorted is: " + makeGrid(sortList(listOfElem))
print getStats(listOfElem)



	