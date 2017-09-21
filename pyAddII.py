#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird

print "Begin Adder"

#take data
rows = raw_input("")
cols = raw_input("")
totalElements = int(rows) * int(cols)
count = totalElements

#create list
ans = 0
elemList = []
while (count > 0):
	elem = raw_input("")
	elemList.append(float(elem))
	ans = float(elem) + float(ans)
	count = int(count) - int(1)

#digest list
average = float(ans)/float(totalElements)
elemList.sort()
print "Final Score: " + str(ans)
print "Average was: " + str(average)
print "median is: " + str((elemList[len(elemList)/2]))


#Construct Grid
print "Sorted grid of " + str(totalElements) + " is: "

count = 0
rowStr  = ""
while (count < (int(totalElements))):
	if(count % int(cols) == 0 and count != 0):
		rowStr += '\n'
	rowStr += str(elemList[count]) + ' '
	count += 1

print rowStr
	
	
