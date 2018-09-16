#! usr/bin/Python


#Setting up html layout
print 'Content-type: text/html'
print ''


#Setting form
import cgi
form = cgi.FieldStorage()


#Set in game variables, in a dictionary
mastermindSettings = {
    'typesOfPins'   :   8,
    'noOfPins'      :   4,
    'noOfRows'      :   10,
    'code'          :   []
}


#Set saved variables
code = form.getvalue('code')
noOfPins = form.getvalue('noOfPins')
noOfRows = form.getvalue('noOfRows')
savedUserAnswers = form.getvalue('userAnswers')



#Setting code definition as a list
def setCode():
    mastermindSettings['code'] = []
    from random import randint
    for pin in range(1, int(mastermindSettings['noOfPins']) + 1):
        mastermindSettings['code'].append(randint(1, int(mastermindSettings['typesOfPins'])))

#If code exists, put in settings, otherwise create a code
if code:
    mastermindSettings['code'] = list(code)
else:
    setCode()



#Establish the user input
userAnswers = {
    'rowCode': '',
    'row1': 2135,
    'row2': 3456
}

#If user has input previous answers, put them back into userAnswers
if savedUserAnswers:
    userAnswers = eval(savedUserAnswers)

#Create string of the row
if form.getvalue('pin1'):
    userAnswers['rowCode'] = None
    for pin in range(1, mastermindSettings['noOfPins'] + 1):
        userAnswers['rowCode'] += str(form.getvalue('pin' + str(pin)))

    int(userAnswers['rowCode'])

#print userAnswers

#Convert array to string for input value
codeInputValue = ''.join(str(pin) for pin in mastermindSettings['code'])

#Convert nested array for userAnswers to string for input codeInputValue
userAnswersInputValue = str(userAnswers)
#','.join(str(''.join([str(pin) for pin in row])) for row in userAnswers)


#Create form for user input
print '<form method=\'get\'>'
print '<input name=\'code\' value=' + codeInputValue + '>'
print '<input name=\'userAnswers\' value=\"' + userAnswersInputValue + '\">'

for pin in range(1, mastermindSettings['noOfPins'] + 1):
    print '<select name=\'pin' + str(pin) + '\'>'

    for option in range(1, mastermindSettings['typesOfPins'] + 1):
        print '<option value=' + str(option) + '>' + str(option) + '</option>'

    print '</select>'

print '&nbsp;<input type=\'submit\' value=\'Confirm code\' /></form><br />'


#Comparing provided answer to code
def checkAnswer():
    fullCorrectPins = 0
    halfCorrectPins = 0

    #Give a pin number equal to the number of pins in the code.
    for pinNo in range(0, len(mastermindSettings['code'])):
        #If direct match, fullCorrectPins increases by 1
        if mastermindSettings['code'][pinNo] == userAnswers[-1]:
            fullCorrectPins += 1
        else:
            #Go through each of the pins given as answer
            for pin in userAnswers[-1]:
                #If matches any other pin, is a match but not by position
                if pin == mastermindSettings['code'][pinNo]:
                    halfCorrectPins += 1
                    break   #break so doesn't keep going if already matches

checkAnswer()
