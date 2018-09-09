#! /usr/bin/Python

#Setting up html layout
print 'Content-type: text/html'
print ''

import cgi
form = cgi.FieldStorage()


#Game settings (Row & no of pins)
print """
<h2>Mastermind</h2>

<h4>Game Settings:</h4>
<form id='noOfPinsForm' method='post'>
    <label for='noOfPins'>How many pins do you want to play with?</label>
    <select name='noOfPins'>
        <option value=4>4</option>
        <option value=6>6</option>
        <option value=8>8</option>
    </select>
    <br />
    <br />
    <label for='noOfRows'>How many rows do you want to play?</label>
    <select name='noOfRows'>
        <option value=10>10</option>
        <option value=15>15</option>
        <option value=20>20</option>
    </select>
    <br />
    <br />
    <input type='submit' value='Start game!' />
</form>
"""

noOfPins = int(form.getvalue("noOfPins"))
noOfRows = int(form.getvalue("noOfRows"))
noOfPinTypes = 8;


#Answer row
answerRow = []

def setAnswer():
    from random import randint
    for pin in range(1, noOfPins + 1):
        answerRow.append(randint(1,int(noOfPinTypes)))

if "answerRow" not in form:
    setAnswer()
    #set answerRow in form variable here

print answerRow
#If set, play
if "noOfPins" and "noOfRows" in form:

    print "<h4> Let's Play!</h4>"

    row = 1

    #Setup one selection
    print "<form method='post' name=row" + str(row) + ">"
    for pins in range(1, noOfPins + 1):
        print "<select>"
        for pinNo in range(1, int(noOfPinTypes) + 1):
            print "<option value=" + str(pinNo) + ">" + str(pinNo) + "</option>"
        print "</select>"
    print "&nbsp; <input type='submit' value='Confirm' /></form><br/><br/>"

    print form

    row += 1

    #Print Row answers
    for row in range (1, noOfRows + 1):
        print "Row " + str(row).zfill(2)

        for pins in range(1, noOfPins + 1):
            print "&#9676;"

        print "<br/>"

else:
    print "Error!"


#TO DO: Take out the settings and build the game, add the settings parameters back inself.
#       Try one row and if not correct pushing a new row
#       If win, change existing h4 to You Win!
#       Look at how to change existing print, possible find an idea and change the innerHTML
