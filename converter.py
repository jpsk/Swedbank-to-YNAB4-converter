import os, sys, csv, time

err_msg = 'Please provide filename or path'

_input = None
list = [['Date', 'Payee', 'Category', 'Memo', 'Outflow', 'Inflow']]


def get_abs_path(arg):
    if arg[0] == '/':
        return arg
    else:
        return os.getcwd() + '/' + arg


try:
    _input = get_abs_path(sys.argv[1])
except IndexError:
    exit(err_msg)

try:
    _input = csv.reader(open(get_abs_path(_input), 'r'))
    next(_input)
    for row in _input:

        date = row[2].split('-')
        date = date[0] + '/' + date[1] + '/' + date[2]
        payee = ''
        memo = row[4]
        if row[7] == 'K':
            outflow = ''
            inflow = row[5]
        else:
            outflow = row[5]
            inflow = ''

        row = [date, payee, '', memo, outflow, inflow]
        list.append(row)

except FileNotFoundError:
    exit('File not found')


with open('exported_' + time.strftime("%y_%m_%d_%H%M") + '.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(list)
