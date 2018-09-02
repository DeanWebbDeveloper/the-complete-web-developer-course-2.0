#! /usr/bin/Python

print 'Content-type: text/html'
print ''

for i in range(5, 11):
    print i

print "Chris"

text = "James"

if text == "Chris" or text == "James":
    print "Hello " + text
else:
    print "I don't know you"

# Create a program which displays the first 50 prime numbers

number = int(2)

for i in range (2, number):
    j = float(1)

    isPrimeCount = int(0)

    while j <= i and isPrimeCount < 3:
        if i % j == 0:
            isPrimeCount += 1
        j += 1

    if isPrimeCount == 2:
        print str(i) + " is a prime number."


# Tutor's code

numberOfPrimes = 0
number = 2

while numberOfPrimes < 50:
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False

    if isPrime == True:
        print number
        numberOfPrimes += 1

    number += 1
