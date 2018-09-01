#! /usr/bin/Python

print 'Content-type: text/html'
print ''

age = 25

print age

pi = 3.14

print pi

name = "Chris"

print name

print age / pi

number = "5"

print float(number) * pi

str = "My Name Is "

print str[0]
print str[0:5]
print str[5]

print str + name

myList = ["Chris", "James", "Kelly", "Joseph", "Emma"]

print myList
print myList[1]
print myList[2:4]

myTuple = (1, 2, 3, 4)

print myTuple
print myTuple[3]

myList[2] = 5

print myList

dict = {}
dict["person1"] = "Chris"
dict["person2"] = "James"
dict["person3"] = "Kelly"
dict[1] = "Joseph"
dict[2] = "Emma"

print dict
print dict["person2"]
print dict.keys()
print dict.values()
