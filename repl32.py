### chap15/repl32.py
import sys
from pin32 import my_pin, print_it, write_it

def insert_repl(edited_script, breakpt, ws):
    """ Insert code to create a read-eval-print loop

        while True:
            p = input("repl> ")
            if p == "#q":
                break
            print(eval(p))
    """
    s = ws + 'while True:\n'
    edited_script.insert(breakpt, s)
    s = ws + ' '*4 + 'p = input("repl> ")\n'
    edited_script.insert(breakpt + 1, s)
    s = ws + ' '*4 + 'if p == "#q":\n'
    edited_script.insert(breakpt + 2, s)
    s = ws + ' '*8 + 'break\n'
    edited_script.insert(breakpt + 3, s)
    s = ws + ' '*4 + 'print(eval(p))\n'
    edited_script.insert(breakpt + 4, s)


def main():
    # Ask for the name of the script to be debugged, unless already provided
    if len(sys.argv) == 1:
        fname = input('What script would you like to instrument? ')
    elif len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        sys.exit('Usage: python3 repl32.py [script_to_be_instrumented]')

    # Call our instrumentation routine
    edited_script = my_pin(fname, insert_repl)

    # print_it(edited_script)
    # write_it(edited_script, fname)

    # Run the instrumented script
    exec(''.join(edited_script), globals())

    print('repl32: All done!')

if __name__ == '__main__':
    main()