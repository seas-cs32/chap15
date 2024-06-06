### chap15/pdb0.py
import sys

def my_pdb(script_fname):
    ''' First attempt at our debugger
        Input:   filename of script to be debugged
        Returns: edited script as list of lines
    '''
    pass  # TO BE WRITTEN

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
        sys.exit('Usage: python3 pdb0.py [script_to_be_debugged]')

    edited_script = my_pdb(fname)

    print_it(edited_script)
    # write_it(edited_script, fname)

if __name__ == '__main__':
    main()