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
    'answerGiven': None
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
if form.getvalue('pin1'):
    newRow = ''

    for pin in range(1, mastermindSettings['noOfPins'] + 1):
        newRow += str(form.getvalue('pin' + str(pin)))
    userAnswers['answerGiven'] = newRow





#### Stopped here, set the above (answerGiven) equal to the latest rowself.
#### Put all of this in a definition
#### Check that every iteration adds a new row
#### put in the comparison and while loops for checking





#Create form for user input
print '<form method=\'get\'>'
print '<input name=\'code\' value=' + mastermindSettings['code'] + '>'

for row in range(1, mastermindSettings['noOfRows'] + 1):
    if saved['row' + str(row)]:
        print '<input name="row' + str(row) + '" value="' + saved['row' + str(row)] + '">'

for pin in range(1, mastermindSettings['noOfPins'] + 1):
    print '<select name=\'pin' + str(pin) + '\'>'

    for option in range(1, mastermindSettings['typesOfPins'] + 1):
        print '<option value=' + str(option) + '>' + str(option) + '</option>'

    print '</select>'

print '&nbsp;<input type=\'submit\' value=\'Confirm code\' /></form><br />'
