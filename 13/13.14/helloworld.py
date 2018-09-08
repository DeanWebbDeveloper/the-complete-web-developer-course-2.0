#! /usr/bin/Python

print 'Content-type: text/html'
print ''

import cgi
form = cgi.FieldStorage()

#if "name" in form:
#    print form.getvalue("name")
#else:
#    print "no name"


print """
<html>

<head>
    <title>Python Project - Mastermind</title>
</head>

<body>

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

</body>

</html>
"""

if "noOfPins" and "noOfRows" in form:
    noOfPins = int(form.getvalue("noOfPins"))
    noOfRows = int(form.getvalue("noOfRows"))

    print "<h4> Let's Play!</h4>"

    for row in range (1, noOfRows + 1):
        rowActive = true;
        print "Row " + str(row).zfill(2) + ": &nbsp; &#9676; &#9676; &#9676; &#9676;"

        for pins in range(1, noOfPins + 1):
            print "<select>"
            for pinNo in range(1, 8 + 1):
                print "<option value=" + str(pinNo) + ">" + str(pinNo) + "</option>"
            print "</select>"

        print "&nbsp; <input type='submit' value='Confirm' />"
        print "&nbsp; <button>Clear</button>"
        print "<br/>"

else:
    print "Error!"


#TO DO: Take out the settings and build the game, add the settings parameters back inself.
#       Try one row and if not correct pushing a new row
#       If win, change existing h4 to You Win!
#       Look at how to change existing print, possible find an idea and change the innerHTML
