#! /usr/bin/Python

#Setting up html layout
print 'Content-type: text/html'
print ''

#Setting form for Get and Post
import cgi
form = cgi.FieldStorage()

#Dictionary for providing the code and all rows
mastermindDict = {
}

#How to set a random code
def setCode():
    mastermindDict['code'] = []
    from random import randint
    for pin in range(1, 4 + 1):
        mastermindDict['code'].append(randint(1,8))

#Code recorded
formCode = list(form.getvalue('code'))

#If code already exists, set in the dictionary, otherwise set a code
if formCode:
    mastermindDict['code'] = formCode
else:
    setCode()


#Set variables for the answer you give, bools for if the game is won and/or over, and the row value
global yourAnswer
yourAnswer = []

global gameOver
gameOver = False

global gameWin
gameWin = False

global row
row = 1

#compare yourAnswer to the mastermind answer
def checkAnswer():

    global fullCorrectPins
    fullCorrectPins = 0
    global halfCorrectPins
    halfCorrectPins = 0

    #Give a pin number, so pin 1, 2, 3, 4, for direct comparison
    for pinNo in range(0, len(mastermindDict['code'])):
        #If direct match, fullCorrectPins increases by 1
        if mastermindDict['code'][pinNo] == yourAnswer[pinNo]:
            fullCorrectPins += 1
        else:
            #Go through each of the pins given as answer
            for yourPin in yourAnswer:
                #If matches any other pin, is a match but not by position
                if yourPin == mastermindDict['code'][pinNo]:
                    halfCorrectPins += 1
                    break   #break so doesn't keep going if already matches


#Create form for user input
print '<form method=\'get\'>'

print '<input type=\'hidden\' name=\'code\' value=' + str(mastermindDict['code'][0]) + str(mastermindDict['code'][1]) + str(mastermindDict['code'][2]) + str(mastermindDict['code'][3]) + '>'



for pin in range(1, 4 + 1):
    print '<select name=\'pin' + str(pin) + '\'>'

    for option in range(1, 8 + 1):
        print '<option value=' + str(option) + '>' + str(option) + '</option>'

    print '</select>'

print '&nbsp;<input type=\'submit\' value=\'Confirm code\' /></form><br />'


while gameOver == False:

    yourAnswer=[]

    for yourPin in range(1, 4 + 1):
        yourAnswer.append(form.getvalue('pin' + str(yourPin)))

    checkAnswer()

    mastermindDict['row' + str(row)] = yourAnswer

    print 'Row ' + str('%02d' % (row)) + ':&nbsp;&nbsp;&nbsp;' + str(yourAnswer) + '&nbsp;&nbsp;&nbsp;'

    #If any part correct
    if fullCorrectPins > 0:
        for fullCorrectPin in range(0, fullCorrectPins):
            print '&#9679;'

    if halfCorrectPins > 0:
        for halfCorrectPin in range(0, halfCorrectPins):
            print '&#9680;'

    #If any circles not drawn, drawn dotted circle
    if fullCorrectPins + halfCorrectPins < 4:
        for incorrectPin in range (0, (4 - (fullCorrectPins + halfCorrectPins))):
            print '&#9676;'

    print '<br />'

    #If a win, 4 full matches
    if fullCorrectPins == 4:
        print '<br/ >You Win! The code was ' + str(mastermindDict['code'])
        gameOver = True
        gameWin = True
    else:
        if row == 10:
            gameOver = True
            gameWin = False
            print '<br />You lose. The code was ' + str(mastermindDict['code'])

        row += 1


print mastermindDict
