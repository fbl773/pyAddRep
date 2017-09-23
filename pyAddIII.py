#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird

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
	average = float(sumElements)/len(elemList)
	elemList.sort()
	print "Final Score: " + str(sumElements)
	print "Average was: " + str(average)
	print "median is: " + str((elemList[len(elemList)/2]))
	return


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
	
	
