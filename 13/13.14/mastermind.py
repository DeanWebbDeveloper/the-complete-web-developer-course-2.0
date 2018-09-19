#! usr/bin/Python


#Setting up html layout
print 'Content-type: text/html'
print ''


#Setting form
import cgi
form = cgi.FieldStorage()

mastermindSettings = {
    'typesOfPins'   :   8,
    'noOfPins'      :   4,
    'noOfRows'      :   10,
    'code'          :   None
}

userAnswers = {
    'answerGiven': None,
    'gameOver': False,
    'gameWon': False
}


#Setting all the rows in the userAnswers
def setRows():
    for row in range(1, mastermindSettings['noOfRows'] + 1):
        userAnswers['row' + str(row)] = None

setRows()


#Set saved variables from formCode
saved = {}
def setSavedFromForm():
    for key in mastermindSettings:
        saved[key] = form.getvalue(key)

    for key in userAnswers:
        saved[key] = form.getvalue(key)

setSavedFromForm()


#If code is present/saved, set the code as the saved code, else make a new one
def checkCodeExists():

    #Setting code as a string
    def setCode():
        mastermindSettings['code'] = ''
        from random import randint
        for pin in range(1, int(mastermindSettings['noOfPins']) + 1):
            mastermindSettings['code'] += str(randint(1, int(mastermindSettings['typesOfPins'])))

    if saved['code']:
        mastermindSettings['code'] = saved['code']
    else:
        setCode()

checkCodeExists()


#If rows are present/saved, set the code to the saved code
def checkRowsExist():
    for row in range(1, mastermindSettings['noOfRows'] + 1):
        if saved['row' + str(row)]:
            userAnswers['row' + str(row)] = saved['row' + str(row)]

checkRowsExist()


#if answer given prior, set as answer given
def setLastAnswerRowGiven():
    if form.getvalue('pin1'):
        newRow = ''

        for pin in range(1, mastermindSettings['noOfPins'] + 1):
            newRow += str(form.getvalue('pin' + str(pin)))
        userAnswers['answerGiven'] = newRow

        for row in range(1, mastermindSettings['noOfRows'] + 1):
            if userAnswers['row' + str(row)] is None:
                userAnswers['row' + str(row)] = userAnswers['answerGiven']
                break

setLastAnswerRowGiven()


#Create form for user input
print '<form method=\'post\'>'
print '<input type="hidden" name=\'code\' value=' + mastermindSettings['code'] + ' />'

for row in range(1, mastermindSettings['noOfRows'] + 1):
    if userAnswers['row' + str(row)]:
        print '<input type="hidden" name="row' + str(row) + '" value="' + userAnswers['row' + str(row)] + '" />'

for pin in range(1, mastermindSettings['noOfPins'] + 1):
    print '<select name=\'pin' + str(pin) + '\'>'

    for option in range(1, mastermindSettings['typesOfPins'] + 1):
        print '<option value=' + str(option) + '>' + str(option) + '</option>'

    print '</select>'

print '&nbsp;<input type=\'submit\' value=\'Confirm code\' /></form><br />'


#Comparing provided answer to code
def checkAnswer(toCheck):
    fullCorrectPins = 0
    halfCorrectPins = 0

    #Give a pin number equal to the number of pins in the code.
    for pinNo in range(0, len(mastermindSettings['code'])):
        #If direct match, fullCorrectPins increases by 1
        if mastermindSettings['code'][pinNo] == list(toCheck)[pinNo]:
            fullCorrectPins += 1
        else:
            #Go through each of the pins given as answer
            for pin in list(toCheck):
                #If matches any other pin, is a match but not by position
                if pin == mastermindSettings['code'][pinNo]:
                    halfCorrectPins += 1
                    break   #break so doesn't keep going if already matches

    for fullCorrectPin in range(1, fullCorrectPins + 1):
        print "&#9673;"

    for halfCorrectPin in range(1, halfCorrectPins + 1):
        print "&#9678;"

    wrongPins = 4 - (fullCorrectPins + halfCorrectPins)

    for wrongPin in range(1, wrongPins + 1):
        print "&#10005;"

    if fullCorrectPins == 4 :
        userAnswers['gameWon'] = True
        userAnswers['gameOver'] = True
#Print the checks
for row in range(1, mastermindSettings['noOfRows'] + 1):
    if userAnswers['row' + str(row)]:
        print "Row " + "%02d" % (row) + ": "
        printCode = userAnswers['row' + str(row)]
        print "&nbsp;&nbsp;&nbsp;" + ("&nbsp;&nbsp;".join(printCode)) + "&nbsp;&nbsp;&nbsp;"
        checkAnswer(userAnswers['row' + str(row)])
        print "<br />"

#End result

if userAnswers['row' + str(mastermindSettings['noOfRows'])]:
    userAnswers['gameOver'] = True

if userAnswers['gameWon'] == True:
    print "<br />You win! The code was " + (" ".join(str(mastermindSettings['code']))) + "!"

if userAnswers['gameOver'] == True and userAnswers['gameWon'] == False:
    print "<br />You lose. The code was " + (" ".join(str(mastermindSettings['code']))) + ". Better luck next time!"
