#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird

print "Begin pyAdd"

#Initial Values
count = 0 #Becomes the #of Elements
input = 0 #Will become the added elements.

#Grab Data
count = raw_input()
totalElements = count #Will hold the original item count.
ans = 0			  	  #Will store our total value.

#Performs Average, and Total
while (count > 0):
	n = raw_input()
	ans = float(n) + float(ans)
	count = int(count) - 1

average = float(ans)/float(totalElements)
print "Final Score: " + str(ans)
print "Average was: " + str(average)

