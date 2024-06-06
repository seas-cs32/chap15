### chap15/pdb3.py
import sys
import string

def my_pdb(script_fname):
    ''' First attempt at our debugger
        Input:   filename of script to be debugged
        Returns: edited script as list of lines
    '''
    edited_script = []

    # Read in the original script (as a list of file lines)
    with open(script_fname) as fin:
        edited_script = fin.readlines()

    # Grab line number where we'll place the breakpoint
    breakpt = get_lineno(len(edited_script))

    # Convert breakpoint number into a list index
    breakpt_index = breakpt - 1

    # Add the breakpoint
    # .. grab the whitespace so we get the right indentation
    my_whitespace = ''
    for c in edited_script[breakpt_index]:
        if c in string.whitespace:
            my_whitespace += c
        else:
            break

    breakpt_statement = my_whitespace + \
        f'raise Exception("My breakpoint", {breakpt})\n'

    # .. insert a raise statement as our breakpoint
    edited_script.insert(breakpt_index, breakpt_statement)

    return edited_script

def get_lineno(lines):
    ''' Asks for the user for a line number
        Input:   number of lines in script
        Returns: user's line number
    '''
    while True:
        try:
            lineno = int(input('Line number in script? '))
            if lineno < 0 or lineno >= lines:
                print(f'The number must be in the interval [1,{lines}]')
                continue
            return lineno
        except ValueError:
            print('The line number must be an integer')

def print_it(edited_script):
    ''' Print out edited script with line numbers '''
    cols = len(str(len(edited_script)))
    for i, line in enumerate(edited_script):
        print(f'{i + 1:>{cols}} {line}', end='')

def write_it(edited_script, orig_fname):
    ''' Write edited script to a file with a `-db.py` suffix '''
    output_fname = orig_fname.replace('.py', '-db.py')
    with open(output_fname, 'w') as fout:
        fout.write(''.join(edited_script))
    print(f'Wrote {output_fname}')

def main():
    # Ask for the name of the script to be debugged, unless already provided
    if len(sys.argv) == 1:
        fname = input('What script would you like to debug? ')
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        sys.exit('Usage: python3 pdb3.py [script_to_be_debugged]')

    edited_script = my_pdb(fname)

    # print_it(edited_script)
    # write_it(edited_script, fname)

    # Run the edited script and catch our breakpoint exception.
    # Remember to turn the list of strings into one big string.
    try:
        exec(''.join(edited_script), globals())
    except Exception as msg:
        if msg.args[0] == 'My breakpoint':
            print(f'pdb3: Breakpoint at line {msg.args[1]}')
        else:
            print('pdb3: script died with non-breakpoint exception')
            print(msg)

if __name__ == '__main__':
    main()