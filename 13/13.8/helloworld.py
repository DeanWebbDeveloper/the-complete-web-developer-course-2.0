#! /usr/bin/Python

print 'Content-type: text/html'
print ''

for i in range(5, 11):
    print i

print "Chris"

foodList = ["pizza", "ice cream", "hot dog"]

for food in foodList:
    print "I like eating " + food + "."

x = 0
while x <= 10:
    print x
    x += 1


    # Dictionary - 4 names (keys) and ages (value) of people
    # Loop which prints . eg. Sam is 7

dict = {}
dict["Chris"] = 25
dict["Kelly"] = 24
dict["Hannah"] = 21
dict["Emma"] = 29

for key, value in dict.items():
    print key + " is " + str(value) + " years old."

for value in dict:
    print value + " is " + str(dict[value]) + " years old."
