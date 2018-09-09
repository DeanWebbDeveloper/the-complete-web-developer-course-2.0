print 'Content-type: text/html'
print ''

import cgi
form = cgi.FieldStorage()

rowNo = 1
noOfPins = 4

answerRow = []

def makeAnswerRow():
    from random import randint
    for pin in range(1, noOfPins + 1):
        answerRow.append(randint(1,8))

makeAnswerRow()
print answerRow


print '<form>'
for pin in range (1, noOfPins + 1):
    print '<select name="pin' + str(pin) + '">'
    print '<option value="" disabled selected>Select your pin</option>'
    for pinNo in range(1, 8 + 1):
        print '<option value=' + str(pinNo) + '>' + str(pinNo) + '</option>'
    print '</select>'

print '&nbsp; <input type="submit" value="Confirm" />'
print '&nbsp; <button>Clear</button>'
print '</form>'

if form:
    for pin in range(1, int(noOfPins) + 1):
        print form.getvalue('pin' + str(pin));
