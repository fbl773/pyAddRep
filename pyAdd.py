#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird

print "Begin Adder"

c = 2
n = -1.0
c = raw_input("How many elements?: ")
totalElements = c
ans = 0
while (c > 0):
	n = raw_input("Give Me a number to add: ")
	ans = float(n) + float(ans)
	c = int(c) - int(1)

average = float(ans)/float(totalElements)
print "Final Score: " + str(ans)
print "Average was: " + str(average)
'''
    adsfd
'''
