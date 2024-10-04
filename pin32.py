### chap15/pin32.py
import sys
import string

def insert_print(edited_script, breakpt_index, ws):
    '''Inserts a user-defined print statement in `edited_script`,
       which is a list of Python statements, at the index
       specified, and with the indentation from `ws`.
    '''
    # Ask for the print-statement argument
    printarg = input("What is print's argument? ")

    print_statement = ws + f'print(f"{printarg}")\n'

    # Insert our print statement
    edited_script.insert(breakpt_index, print_statement)

def my_pin(script_fname, insert_code):
    '''Adds code at a user-specified line number.
        Inputs:  filename of script to be debugged
                 function responsible for inserted code
        Returns: edited script as list of lines where
                 each line ends in a newline character
    '''

    # Read in the original script (as a list of file lines)
    with open(script_fname) as fin:
        edited_script = fin.readlines()

    # Grab line number where we'll place some new code
    breakpt = get_lineno(len(edited_script))

    # Convert breakpoint number into a list index
    breakpt_index = breakpt - 1

    # Compute the leading whitespace at `breakpt_index`
    my_whitespace = ''
    for c in edited_script[breakpt_index]:
        if c in string.whitespace:
            my_whitespace += c
        else:
            break

    insert_code(edited_script, breakpt_index, my_whitespace)

    return edited_script

def get_lineno(lines):
    ''' Asks the user for a line number
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
    ''' Write edited script to a file with a `-pin.py` suffix '''
    output_fname = orig_fname.replace('.py', '-pin.py')
    with open(output_fname, 'w') as fout:
        fout.write(''.join(edited_script))
    print(f'Wrote {output_fname}')

def main():
    # Ask for the name of the script to be debugged, unless already provided
    if len(sys.argv) == 1:
        fname = input('What script would you like to instrument? ')
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        sys.exit('Usage: python3 pin32.py [script_to_be_instrumented]')

    edited_script = my_pin(fname, insert_print)

    # print_it(edited_script)
    # write_it(edited_script, fname)

    # Run the instrumented script
    exec(''.join(edited_script), globals())
    
    print('pin32: All done!')

if __name__ == '__main__':
    main()