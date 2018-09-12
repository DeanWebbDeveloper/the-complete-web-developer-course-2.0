print 'Content-type: text/html'
print ''

import cgi
form = cgi.FieldStorage()

masterMindDict = {
    'code': {
        'pin1': 1,
        'pin2': 2,
        'pin3': 3,
        'pin4': 4
    }
}

row = 1

print '''
    <form method='post'>
        <select name="row''' + str(row) + '''-pin1">
            <option value='1'>1</option>
            <option value='2'>2</option>
            <option value='3'>3</option>
            <option value='4'>4</option>
        </select>
        <select name='pin2'>
            <option value='1'>1</option>
            <option value='2'>2</option>
            <option value='3'>3</option>
            <option value='4'>4</option>
        </select>
        <select name='pin3'>
            <option value='1'>1</option>
            <option value='2'>2</option>
            <option value='3'>3</option>
            <option value='4'>4</option>
        </select>
        <select name='pin4'>
            <option value='1'>1</option>
            <option value='2'>2</option>
            <option value='3'>3</option>
            <option value='4'>4</option>
        </select>

        <input type='submit' value='Confirm' />
    </form>
'''

row += 1

print form
